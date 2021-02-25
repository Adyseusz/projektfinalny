import pytest
import django.test
import datetime

from django.contrib.auth.models import User

from baza_firm.models import Company, City, CategoryServices, Stationary, AttributesCompany


@pytest.fixture
def client():
    return django.test.Client()

@pytest.fixture
def city():
    return City.objects.create(city_name='Warszawa')

@pytest.fixture
def service():
    return CategoryServices.objects.create(service='Marketing')

@pytest.fixture
def stationary():
    return Stationary.objects.create(stationary_point='Tak')

@pytest.fixture
def attributes():
    return AttributesCompany.objects.create(atribute_choice='Kierowana przez kobietę')



@pytest.fixture
def test_company():
    return Company.objects.create(name='test', description='Test, test', contact='a@test.pl')


@pytest.fixture
def basicuser():
    return User.objects.create_user(username='testowy')

@pytest.fixture
def superuser():
    return User.objects.create_superuser(username='admin')