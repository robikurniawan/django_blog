from django.contrib import admin

# Register your models here.
from .models import Artikel  
class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'published',
        'updated'
    ]


admin.site.register(Artikel,ArtikelAdmin)