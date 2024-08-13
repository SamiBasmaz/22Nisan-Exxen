from django.contrib import admin
from .models import Film
# Register your models here.



# admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title','description','created_at')