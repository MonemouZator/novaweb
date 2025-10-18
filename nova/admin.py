from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Application, Service, Temoignage, Formation, Equipe, Partenaire, MessageContact,APropos,ParcoursAcademique

admin.site.register(Application)
admin.site.register(Service)
admin.site.register(Temoignage)
admin.site.register(Formation)
admin.site.register(Equipe)
admin.site.register(Partenaire)
admin.site.register(MessageContact)
admin.site.register(APropos)
admin.site.register(ParcoursAcademique)

from django.contrib import admin
from .models import CategorieCours, Cours

@admin.register(CategorieCours)
class CategorieCoursAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_creation')
    list_filter = ('categorie',)
    search_fields = ('titre', 'description')
