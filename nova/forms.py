from django import forms
from .models import MessageContact, Application, Formation

class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ['nom', 'email', 'sujet', 'message', 'application_interet', 'formation_interet']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemple@mail.com'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Objet de votre message'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Votre message...'}),
            'application_interet': forms.HiddenInput(),
            'formation_interet': forms.HiddenInput(),
        }

from django import forms
from .models import Temoignage

class TemoignageForm(forms.ModelForm):
    class Meta:
        model = Temoignage
        fields = ['nom', 'message', 'photo', 'fonction', 'formation', 'application']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Votre témoignage...'}),
            'fonction': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre poste/fonction'}),
            'formation': forms.Select(attrs={'class': 'form-control'}),
            'application': forms.Select(attrs={'class': 'form-control'}),
        }
