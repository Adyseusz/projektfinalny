from django.test import TestCase
import pytest
from .models import Company, Comments
from django.contrib.auth.models import User

# Create your tests here.

@pytest.mark.django_db
def test_AddCompanyView(client, basicuser, city, service, stationary, attributes):
    client.force_login(basicuser)
    response = client.post('/add-company/', {'name': "Test", 'description': 'testowy opis', 'contact': 'twest@tes.pl', 'city': city.id, 'services': service.id, 'have_stationary': stationary.id, 'attribute_company': attributes.id})
    assert response.status_code == 302

    assert Company.objects.get(name="Test")

@pytest.mark.django_db
def test_AddCommentView(client, basicuser, test_company):
    client.force_login(basicuser)
    response = client.post('/add_comment/', {'company_name': test_company.id, 'author_name': 'testowy autor', 'comment': 'Komentarz'})
    assert response.status_code == 302
    assert Comments.objects.filter(company_name=test_company.id)

@pytest.mark.django_db
def test_search(client, test_company):
    response = client.post('/search-company/', {'name': 'tes'})

    assert Company.objects.get(name__icontains='tes')



#sprawdzenie czy niezalogowany użytkownik może dodać komentarz (tylko zalogowani użytkownicy mogą dodać komentarz)
@pytest.mark.django_db
def test_add_comment(client):
    response = client.post('/add_comment/', {'company_name': 'Google', 'author_name': 'testowy autor', 'comment': 'Komentarz'})
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_company_without_login(client, city, service, stationary, attributes):
    response = client.post('/add-company/', {'name': "Test", 'description': 'testowy opis', 'contact': 'twest@tes.pl', 'city': city.id, 'services': service.id, 'have_stationary': stationary.id, 'attribute_company': attributes.id})
    assert response.status_code == 302
#
@pytest.mark.django_db
def test_company_delete(client, basicuser, test_company):
    client.force_login(basicuser)

    response = client.post(f'/company/delete/{test_company.id}/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_company_delete_super(client, superuser, test_company):
    client.force_login(superuser)

    response = client.post(f'/company/delete/{test_company.id}/')
    print(response.content)

    assert len(Company.objects.filter(name='Test')) == 0
    assert response.status_code == 302



