from django.shortcuts import render, redirect
from django.views import View
from .forms import AddCompanyForm, CompanySearchForm, AddCommentForm
from .models import Company, CategoryServices, Comments, City, Stationary
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


# Funkcja wyświetlająca stronę główną
def Index(request):
    """
    Jest to funkcja wyświetlająca stronę główną aplikacji BAZA FIRM

    Korzysta z szablonu html zlokalizowanego w templates/index.html

    Ten szablon jest również podstawą do wszystkich pozostałych.
    """
    return render(request, "index.html")

# Klasa, która odpowiada za wyświetlanie się wszystkich firm
class CompanyListView(View):
    """
    Klasa odpowiadająca za wyświetlanie wszystkich firm i przekazująca ją do szablonu
    all.company.html
    Firmy zawarte są w kontekście 'company'
    """
    def get(self, request):
        company = Company.objects.all()
        return render(request, "allcompany.html", context={"company": company})




class AddCompanyView(LoginRequiredMixin, View):
    """
    Ta klasa odpowiada za dodawanie firm do bazy.

    Aby móc dodać firmę należy być zalogowanym za co odpowiada funkcja LoginRequiredMixin

    Firma po dodaniu wszystkich pól
    name
    descriptions
    contact
    services
    city
    have_stationary

    tworzy nowy url /company/(id nowo stworzonej firmy)

    Wszystkie firmy znajduja się pod adresem /company-list
    """
    def get(self, request):
        form = AddCompanyForm()
        return render(request, 'addcompany.html', {'form': form})

    def post(self, request):
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            new_company = Company.objects.create(name=form.cleaned_data['name'], description=form.cleaned_data['description'], contact=form.cleaned_data['contact'], services=form.cleaned_data['services'], city=form.cleaned_data['city'], have_stationary=form.cleaned_data['have_stationary'])


            return redirect(f'/company/{new_company.id}')
        else:
            return render(request, 'addcompany.html', {'form': form})

# Wyszukiwanie firm przez formularz
class CompanySearchView(View):
    """
    Klasa CompanySearchView pozwala wyszukiwać firmy przez formularz

    Po wpisaniu 3 znaków otrzymujemy znalezione wszystkie firmy odpowiadające znakom.

    """

    def get(self, request):
        form = CompanySearchForm()
        return render(request, 'search.html', {'form': form})

    def post(self, request):
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            company_found = Company.objects.filter(name__icontains=form.cleaned_data['name'])
            print(company_found)
            return render(request, 'search.html', {'form': form, 'company': company_found})
        else:
            return render(request, 'search.html', {'form': form})


class CompanyView(View):
    """
    Widok CompanyView wyświetla stronę firmy z przekazaniem wszystkich danych przez formularz na stronie
    add-company/
    Szablon storny znajduje sie w templates/company
    """
    def get(self, request, company_id):
        company = Company.objects.get(id=company_id)
        contact = Company.objects.all()
        comments = Comments.objects.filter(company_name=company)
        city = City.objects.all()
        stationary = Stationary.objects.all()
        return render(request, 'company.html', {'company': company,
                                                'contact': contact, 'company_id': company_id, 'city': city, 'comments': comments, 'stationary': stationary})


class DeleteCompanyView(PermissionRequiredMixin, View):
    """
    Widok DeleteCompanyView odpowiada za usunięcie firmy.
    Usunąć firmę można poprzez /company/delete/(ID FIRMY)

    Widok jest jednak chroniony PermissionRequiredMixin i usunąć może ją tylko superuser.
    """
    permission_required = 'baza_firm_app.delete'
    def get(self, request, new_company_id):
        company = Company.objects.get(id=new_company_id)
        company.delete()
        return redirect('company-list')

    def post(self, request):
        company = Company.objects.get(id=new_company_id)
        company.delete()
        return redirect('company-list')



class SignUpView(generic.CreateView):
    """
       Szybka rejestracja użtykownika

    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




#Dodanie komentarza pod opowiednią firmę.
class AddCommentView(LoginRequiredMixin, View):
    """
    Do każdej firmy można przypisać równie
    """
    login_required = 'baza_firm_app.add_comment'
    def get(self, request):
        form = AddCommentForm()
        return render(request, 'add_comment.html', {'form': form})

    def post(self, request):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            author_name = form.cleaned_data['author_name']
            comment = form.cleaned_data['comment']
            compComment = Comments.objects.create(company_name=company_name, author_name=author_name, comment=comment)
            compComment.save()
        return redirect('comments-list')







class CommentsListView(View):
    """
    Widok pozwala na wyświetlenie wszystkich komentarzy dodanych przez użytkowników.
    Widok korzysta z szablony templates/allcomments.html
    """
    def get(self, request):
        all_comment = Comments.objects.all()
        return render(request, 'allcomments.html', context={"all_comment": all_comment})



class AllCategoryServicesView(View):
    def get(self, request):
        all_services = CategoryServices.objects.all()
        return render(request, 'allcategory.html', {'all_services': all_services})


