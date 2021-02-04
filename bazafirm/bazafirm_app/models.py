from django.db import models


class CompanyName(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    online_availability = models.BooleanField(default=False)

