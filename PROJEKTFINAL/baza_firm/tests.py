from django.test import TestCase
import pytest
from .models import Company, Comments

# Create your tests here.


@pytest.mark.django_db
def test_AddCompanyView(client):
    response = client.post('/add-company/', {'name': 'Test', 'description': 'testowy opis', 'contact': 'twest@tes.pl', 'services': '', 'city': '', 'have_stationary': 'TAK'})
    assert Company.objects.filter(name='Test')

@pytest.mark.django_db
def test_AddCommentView(Comments):
    response = Comments.objects.create(company_name='Google', author_name= 'testowy autor', comment='Komentarz')
    assert Comments.objects.filter(company_name='Google')
