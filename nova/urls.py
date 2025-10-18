from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('formations/', views.formations, name='formations'),
    path('applications/', views.applications, name='applications'),
    path('apropos/', views.apropos, name='apropos'),
    path('contact/', views.contact, name='contact'),
    path('temoignages/', views.temoignages, name='temoignages'),
    path('temoignages/ajouter/', views.ajouter_temoignage, name='ajouter_temoignage'),
    path('ajout/', views.tt, name='ajou'),
     path('cours/', views.liste_cours, name='liste_cours'),
]
