from django.shortcuts import render, redirect
from django.views import View
from .models import CompanyName

def Base(request):
    return render(request, "base.html")


class AddCompanyView(View):
    def get(self, request):
        return render(request, "add_company.html")

    def post(self, request):
        name = request.POST.get("name")
        description = request.POST.get("description")
        city = request.POST.get("city")
        online_availability = request.POST.get("online") == "on"

        if not name:
            return render(request, "add_company.html", context={"error": "Nie podano nawy firmy"})
        if not description:
            return render(request, "add_company.html", context={"error": "Nie dodałeś opisu"})
        if not city:
            return render(request, "add_company.html", context={"error": "Nie podano miasta"})
        if CompanyName.objects.filter(name=name).first():
            return render(request, "add_company.html", context={"error": "Firma o podanej nazwie istnieje"})

        CompanyName.objects.create(name=name, description=description, city=city, online_availability=online_availability)
        return redirect("company-list")



class CompanyListView(View):
    def get(self, request):
        companies = CompanyName.objects.all()
        return render(request, "companies.html", context={"companies": companies})
