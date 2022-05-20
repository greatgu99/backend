from django.contrib import admin
from .models import History
# Register your models here.
@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id','disease_tag','date']