from django.db import models

# Create your models here.
class PatientInformation(models.Model):
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    balance = models.DecimalField(max_digits=None, decimal_places=None, **options)
