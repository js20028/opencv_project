from django.contrib import admin
from .models import Allergy



class SearchAdmin(admin.ModelAdmin):
    search_fields = ['highLevelAllergy']

admin.site.register(Allergy, SearchAdmin)

# Register your models here.
