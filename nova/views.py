from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Application, MessageContact
from django.core.mail import send_mail
from django.conf import settings

from .models import Service, Temoignage, Formation, Application,Equipe
from .models import Formation

from django.contrib import messages




def accueil(request):
    services = Service.objects.all()
    equipes=Equipe.objects.all()
    temoignages = Temoignage.objects.all()
    formations = Formation.objects.all()[:3]     # Affiche 3 formations sur la page d'accueil
    applications = Application.objects.all()[:3]  # Affiche 3 applications sur la page d'accueil

    return render(request, 'siteapp/accueil.html', {
        'services': services,
        'equipes': equipes,
        'temoignages': temoignages,
        'formations': formations,
        'applications': applications
    })



def formations(request):
    formations = Formation.objects.all()
    return render(request, 'siteapp/formations.html', {'formations': formations})



from .models import Application

def applications(request):
    apps = Application.objects.all()  # récupère toutes les applications
    return render(request, 'siteapp/applications.html', {'apps': apps})
from .models import Application

def applications(request):
    apps = Application.objects.all()  # récupère toutes les applications
    return render(request, 'siteapp/applications.html', {'apps': apps})

def apropos(request):
    return render(request, 'siteapp/apropos.html')

def contact(request):
    return render(request, 'siteapp/contact.html')


def tt(request):
    apps = Application.objects.all()
    fomas = Formation.objects.all()
    
    # On passe les variables au template
    return render(request, 'siteapp/ajout.html', {
        'apps': apps,
        'fomas': fomas
    })


from .models import Temoignage


from .forms import TemoignageForm


def temoignages(request):
    # On récupère tous les témoignages triés par date décroissante
    temoignages = Temoignage.objects.order_by('-date_publication')
    return render(request, 'siteapp/temoignages.html', {'temoignages': temoignages})


def ajouter_temoignage(request):
    # Récupérer les options pour les selects
    apps = Application.objects.all()
    fomas = Formation.objects.all()

    if request.method == "POST":
        nom = request.POST.get("nom", "").strip()
        fonction = request.POST.get("fonction", "").strip()
        message_text = request.POST.get("message", "").strip()
        photo = request.FILES.get("photo")
        formation_id = request.POST.get("formation")
        application_id = request.POST.get("application")

        formation = Formation.objects.filter(id=formation_id).first() if formation_id else None
        application = Application.objects.filter(id=application_id).first() if application_id else None

        if not nom or not message_text:
            messages.error(request, "Les champs Nom et Témoignage sont obligatoires.")
        else:
            Temoignage.objects.create(
                nom=nom,
                fonction=fonction,
                message=message_text,
                photo=photo,
                formation=formation,
                application=application
            )
            messages.success(request, "Merci pour votre témoignage !")
            return redirect('temoignages')

    return render(request, 'siteapp/ajout.html', {'apps': apps, 'fomas': fomas})


def contact(request):
    app_id = request.GET.get('app_id')
    formation_id = request.GET.get('formation_id')
    initial_data = {}

    # Pré-remplir le champ selon ce qui est cliqué
    if app_id:
        try:
            application = Application.objects.get(id=app_id)
            initial_data['application_interet'] = application
        except Application.DoesNotExist:
            pass

    if formation_id:
        try:
            formation = Formation.objects.get(id=formation_id)
            initial_data['formation_interet'] = formation
        except Formation.DoesNotExist:
            pass

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()
            
            # Préparer le texte de l'email
            texte_email = f"""
Nom : {message.nom}
Email : {message.email}
Sujet : {message.sujet}
Application d'intérêt : {message.application_interet}
Formation d'intérêt : {message.formation_interet}
Message : {message.message}
            """
            send_mail(
                subject=f"Nouveau message de {message.nom}",
                message=texte_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('contact')
    else:
        form = ContactForm(initial=initial_data)

    return render(request, 'siteapp/contact.html', {'form': form})


from django.shortcuts import render
from .models import Cours, CategorieCours

def liste_cours(request):
    categorie_id = request.GET.get('categorie')
    if categorie_id:
        cours = Cours.objects.filter(categorie_id=categorie_id).order_by('-date_creation')
    else:
        cours = Cours.objects.all().order_by('-date_creation')
    categories = CategorieCours.objects.all()
    return render(request, 'siteapp/liste_cours.html', {'cours': cours, 'categories': categories})


# siteapp/views.py
from django.shortcuts import render
from .models import APropos, ParcoursAcademique

def apropos(request):
    # On récupère la première page "À propos" (ou créer un filtre si plusieurs)
    page = APropos.objects.first()
    parcours = ParcoursAcademique.objects.all().order_by('annee')  # tri par année croissante

    return render(request, 'siteapp/apropos.html', {
        'page': page,
        'parcours': parcours
    })
