from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    contact = models.EmailField(max_length=500)
    services = models.ForeignKey('CategoryServices', on_delete=models.CASCADE, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    have_stationary = models.ForeignKey('Stationary', on_delete=models.CASCADE, null='Brak danych')
    #atribute_comp = models.ManyToManyField('AttributesCompany')
    def __str__(self):
        return self.name

class CategoryServices(models.Model):
    service = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.service


class Comments(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50, default='Anonim', blank=True, null=True)
    comment = models.CharField(max_length=500, default='Brak komentarza', blank=True, null=True)
    def __str__(self):
        return self.comment

class City(models.Model):
    city_name = models.CharField(max_length=255, default='Brak danych')
    def __str__(self):
        return self.city_name


class AttributesCompany(models.Model):
    atribute_choice = models.CharField(max_length=500, default='')
    def __str__(self):
        return self.atribute_choice

class Stationary(models.Model):
    stationary_point = models.CharField(max_length=500, default='Brak danych')
    def __str__(self):
        return self.stationary_point
