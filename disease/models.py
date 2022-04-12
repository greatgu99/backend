from django.db import models

# Create your models here.
class Disease(models.Model):
    diseaseName = models.CharField(max_length=40)
    diseaseDescription = models.CharField(max_length=300,blank=True)
    def __str__(self):
        return self.diseaseName
    class Meta:
        ordering = ['diseaseName']