from django.db import models

# Create your models here.
class Symptom(models.Model):
    symptomName=models.CharField(max_length=40)
    symptomDescription = models.CharField(max_length=300,blank=True)
    def __str__(self):
        return self.symptomName
    class Meta:
        ordering = ['symptomName']