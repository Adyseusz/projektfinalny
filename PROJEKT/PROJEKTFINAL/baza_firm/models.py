from django.db import models



class Company(models.Model):
    """
    Klasa Company przyjmuje wartości
    name = pole tekstowe do 255 znaków
    description = czyli opisz, pole tekstowe do 500 znaków
    contact = pole mailowe, które musi zawierać znak @ i TEKST.TEKST sprawdzające czy jest to mail
    services = relacja jeden do jednego z modelu CategoryServices
    city = relacja jeden do jednego z modelu CITY
    have_stationary = relacja jeden do jednego z modelu Stationary
    """
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    contact = models.EmailField(max_length=500)
    services = models.ForeignKey('CategoryServices', on_delete=models.CASCADE, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    have_stationary = models.ForeignKey('Stationary', on_delete=models.CASCADE, null=True)
    atribute_comp = models.ManyToManyField('AttributesCompany')
    def __str__(self):
        return self.name

class CategoryServices(models.Model):
    """
    Klasa CategoryServices odpowiada z usługi firm.
    Jest to pole tekstowe przyjmujące wartość 255
    """
    service = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.service


class Comments(models.Model):
    """
    Klasa Comments odpowiada z komentarze firm.

    Przyjmuje takie wartości jak
    company_name = relacja 1do1 z COMPANY
    author_name = pole tekstowe do długości 50 znaków o domyślnym polu ANONIM
    comment = pole tekstowe do długości 500 znaków o domyślnym polu BRAK KOMENTARZA
    """
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50, default='Anonim', blank=True, null=True)
    comment = models.CharField(max_length=500, default='Brak komentarza', blank=True, null=True)
    def __str__(self):
        return self.comment

class City(models.Model):
    """
    Klasa CITY to zbiór miast.
    przyjmuje wartość city_name o polu o długości 255 znaków
    """
    city_name = models.CharField(max_length=255, default='Brak danych')
    def __str__(self):
        return self.city_name


class AttributesCompany(models.Model):
    atribute_choice = models.CharField(max_length=500, default='Brak danych')
    def __str__(self):
        return self.atribute_choice

class Stationary(models.Model):
    """
    Klasa Stationary to przyjmuje wartość stationary_point o max. długości 500 znaków

    Zostały jednak stworzone odpowiedzi TAK / NIE ponieważ to jest tylko ta informacja, którą chcemy uzyskać od wypełniajacego formularz.

    """
    stationary_point = models.CharField(max_length=500, default='Brak danych')
    def __str__(self):
        return self.stationary_point
