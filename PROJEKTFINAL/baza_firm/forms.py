import django.forms as forms
from .models import Company, CategoryServices, Comments, City, Stationary
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class AddCompanyForm(forms.Form):
    name = forms.CharField(label="Nazwa firmy")
    description = forms.CharField(label="Opis firmy")
    contact = forms.EmailField(label="Email do firmy")
    services = forms.ModelChoiceField(queryset=CategoryServices.objects.all(), label='W jakiej branży działa firma')
    city = forms.ModelChoiceField(queryset=City.objects.all(), label='Wybierz miasto gdzie firma urzęduje')
    have_stationary = forms.ModelChoiceField(queryset=Stationary.objects.all(), label='Czy firma ma punkt stacjonarny?')

class CompanySearchForm(forms.Form):
    name = forms.CharField(label="Nazwa")

class AddCommentForm(forms.Form):
    company_name = forms.ModelChoiceField(queryset=Company.objects.all(), label='Wybierz firmę')
    author_name = forms.CharField(label="Imię")
    comment = forms.CharField(label="Komentarz")


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

