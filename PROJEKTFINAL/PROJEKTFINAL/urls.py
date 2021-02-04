"""PROJEKTFINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from baza_firm.views import Index, AddCompanyView, CompanyListView, CompanySearchView, CompanyView, DeleteCompanyView, AddCommentView, CommentsListView, AllCategoryServicesView, SignUpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', Index, name='home'),
    path('add-company/', AddCompanyView.as_view()),
    path('company-list/', CompanyListView.as_view(), name="company-list"),
    path('category-list/', AllCategoryServicesView.as_view(), name="all-category-list"),
    path('comments-list/', CommentsListView.as_view(), name="comments-list"),
    path('search-company/', CompanySearchView.as_view(), name="company_search"),
    path('company/<int:company_id>', CompanyView.as_view()),
    path('company/delete/<int:new_company_id>', DeleteCompanyView.as_view(), name="delete-company"),
    path('add_comment/', AddCommentView.as_view(), name='comment_add'),

]
