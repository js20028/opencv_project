from django.contrib import admin
from .models import Allergy
from .models import Result



class SearchAdmin(admin.ModelAdmin):
    search_fields = ['highLevelAllergy']

admin.site.register(Allergy, SearchAdmin)
admin.site.register(Result)

# Register your models here.
