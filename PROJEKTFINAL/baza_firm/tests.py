from django.test import TestCase
import pytest
from .models import Company
from .views import AddCompanyView
# Create your tests here.

#dodawnie firmy
@pytest.mark.django_db
def test_AddCompanyView(self):
    response = self.post('/add-company/', {'name': 'Test', 'description': 'testowy opis', 'contact': 'twest@tes.pl', 'services': '', 'city': '', 'have_stationary': 'TAK'})
    assert Company.objects.filter(name='Test')

# @pytest.mark.django_db
# def test_AddCommentView(company):
#     test_company = Company.objects.create(name = 'Tstowa firma', description= 'testowy opis', contact='twest@tes.pl', services='Marketing', city='Warszawa', atribute='Firma zarządzania przez kobietę')
#     response = company.post()
