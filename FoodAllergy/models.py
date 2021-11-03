from django.db import models

# Create your models here.


class Allergy(models.Model):
    # allergyNum = models.AutoField()
    allergyName = models.CharField(max_length=30)
    highLevelAllergy = models.CharField(max_length=30, blank=True, null=True)
    level = models.IntegerField()
    myAllergy = models.CharField(max_length=10)