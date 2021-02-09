from django.test import TestCase
import pytest
from .models import Company, Comments

# Create your tests here.

@pytest.mark.django_db
def test_AddCompanyView(client):
    response = client.post('/add-company/', {'name': 'Test', 'description': 'testowy opis', 'contact': 'twest@tes.pl', 'services': 'S', 'city': 'Warsa', 'have_stationary': 'TAK'})
    assert response.status_code == 302
    assert Company.objects.filter(name='Test')

# @pytest.mark.django_db
# def test_AddCommentView(client_with_authorised_user):
#     response = client_with_authorised_user.post('/add-comment/', {'company_name': 'Google', 'author_name': 'testowy autor', 'comment': 'Komentarz'})
#     assert response.status_code == 302
#     assert Comments.objects.filter(company_name='Google')
#

#sprawdzenie czy zwykły użytkownik może usunąć firmę
@pytest.mark.django_db
def test_delete_company(client):
    response = client.post('/company/delete/12')
    assert response.status_code == 302

#sprawdzenie czy niezalogowany użytkownik może dodać komentarz (tylko zalogowani użytkownicy mogą dodać komentarz)
@pytest.mark.django_db
def test_add_comment(client):
    response = client.post('/add_comment/', {'company_name': 'Google', 'author_name': 'testowy autor', 'comment': 'Komentarz'})
    assert response.status_code == 302



@pytest.mark.django_db
def test_add_company_without_login(client):
    response = client.get('/add-company/')
    assert response.status_code == 302


