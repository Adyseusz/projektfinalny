from django.shortcuts import render, redirect
from django.views import View
from .forms import AddCompanyForm, CompanySearchForm, AddCommentForm
from .models import Company, CategoryServices, Comments, City, Stationary
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm




# Funkcja wyświetlająca stronę główną
def Index(request):
    return render(request, "index.html")

# Klasa, która odpowiada za wyświetlanie się wszystkich firm
class CompanyListView(View):
    def get(self, request):
        company = Company.objects.all()
        return render(request, "allcompany.html", context={"company": company})



# Klasa umożliwiająca dodanie firm
class AddCompanyView(View):
    def get(self, request):
        form = AddCompanyForm()
        return render(request, 'addcompany.html', {'form': form})

    def post(self, request):
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            new_company = Company.objects.create(name=form.cleaned_data['name'], description=form.cleaned_data['description'], contact=form.cleaned_data['contact'], services=form.cleaned_data['services'], city=form.cleaned_data['city'], have_stationary=form.cleaned_data['have_stationary'])
            #new_company.atribute_comp.set(form.cleaned_data['atribute_company'])

            return redirect(f'/company/{new_company.id}')
        else:
            return render(request, 'addcompany.html', {'form': form})

# Wyszukiwanie firm przez formularz
class CompanySearchView(View):
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

#Widok wyświetlania firm na stronie company/
class CompanyView(View):
    def get(self, request, company_id):
        company = Company.objects.get(id=company_id)
        contact = Company.objects.all()
        comments = Comments.objects.filter(company_name=company)
        city = City.objects.all()
        stationary = Stationary.objects.all()
        return render(request, 'company.html', {'company': company,
                                                'contact': contact, 'company_id': company_id, 'city': city, 'comments': comments, 'stationary': stationary})

# Usunięcie firmy
class DeleteCompanyView(View):
    def get(self, request, new_company_id):
        company = Company.objects.get(id=new_company_id)
        company.delete()
        return redirect('company-list')

    def post(self, request):
        company = Company.objects.get(id=new_company_id)
        company.delete()
        return redirect('company-list')


#szybka rejestracja użytkownika
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




#Dodanie komentarza pod opowiednią firmę.
class AddCommentView(View):
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






#Wyświetlanie wszystkich komentarzy
class CommentsListView(View):
    def get(self, request):
        all_comment = Comments.objects.all()
        return render(request, 'allcomments.html', context={"all_comment": all_comment})


#Wyświetlanie wszystkich możliwych usług
class AllCategoryServicesView(View):
    def get(self, request):
        all_services = CategoryServices.objects.all()
        return render(request, 'allcategory.html', {'all_services': all_services})


