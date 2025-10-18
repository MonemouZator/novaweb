from django.db import models

# === PAGE APPLICATIONS ===
class Application(models.Model):
    nom = models.CharField(max_length=150)
    description_courte = models.CharField(max_length=255, blank=True, null=True)
    description_detaillee = models.TextField(blank=True, null=True)
    technologies = models.CharField(max_length=200, help_text="Ex: Django, React, Flutter")
    # On remplace image par video (optionnel: garder image pour fallback)
    video = models.FileField(upload_to="applications/videos/", blank=True, null=True)
    image = models.ImageField(upload_to="applications/", blank=True, null=True)  # optionnel
    lien_demo = models.URLField(blank=True, null=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom



# === PAGE ACCUEIL ===
class Service(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    icone = models.CharField(
        max_length=100,
        blank=True,
        help_text="Classe FontAwesome (ex: fa-solid fa-code)"
    )

    def __str__(self):
        return self.titre

# === PAGE FORMATIONS ===
class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    duree = models.CharField(max_length=100)
    tarif = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="formations/", blank=True, null=True)
    date_debut = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titre


class Temoignage(models.Model):
    nom = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to="temoignages/", blank=True, null=True)
    fonction = models.CharField(max_length=100, blank=True)
    
    # Relations optionnelles
    formation = models.ForeignKey(
        Formation,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Formation suivie"
    )
    application = models.ForeignKey(
        Application,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Application utilisée"
    )

    # Champ pour trier par date
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.message[:20]}..."



# === PAGE À PROPOS ===
class Equipe(models.Model):
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="equipe/", blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

    def get_photo_url(self):
        """Retourne l’URL de la photo ou une image par défaut si vide."""
        if self.photo:
            return self.photo.url
        return '/static/siteapp/img/default-photo.jpg'

class Partenaire(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="partenaires/", blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nom


# === PAGE CONTACT / INSCRIPTION ===
class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=150)
    message = models.TextField()
    date_envoye = models.DateTimeField(auto_now_add=True)

    # Champ pour application
    application_interet = models.ForeignKey(
        'Application',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Application d'intérêt"
    )

    # Champ pour formation
    formation_interet = models.ForeignKey(
        'Formation',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Formation d'intérêt"
    )

    def __str__(self):
        return f"{self.nom} - {self.sujet}"




class CategorieCours(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Cours(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    categorie = models.ForeignKey(CategorieCours, on_delete=models.SET_NULL, null=True, blank=True)
    video = models.FileField(upload_to='cours/videos/', blank=True, null=True)
    pdf = models.FileField(upload_to='cours/pdfs/', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


# siteapp/models.py

# siteapp/models.py

class APropos(models.Model):
    nom = models.CharField(max_length=100, default="Mon Nom")
    photo = models.ImageField(upload_to="apropos/", blank=True, null=True)
    biographie = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to="videos/biographie/", blank=True, null=True)

    def __str__(self):
        return self.nom


class ParcoursAcademique(models.Model):
    annee = models.CharField(max_length=50)
    titre = models.CharField(max_length=200)
    etablissement = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.annee} - {self.titre}"
