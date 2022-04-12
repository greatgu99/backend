import imp
from django.contrib import admin
from .models import Symptom
# Register your models here.
@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ['id','symptomName']