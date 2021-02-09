from django.contrib import admin
from .models import Company, CategoryServices, Comments, City, AttributesCompany, Stationary
# Register your models here.


admin.site.register(Company)
admin.site.register(CategoryServices)
admin.site.register(Comments)
admin.site.register(City)
admin.site.register(AttributesCompany)
admin.site.register(Stationary)