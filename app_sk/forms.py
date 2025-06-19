from django.forms import ModelForm, inlineformset_factory
from app_sk.models import Contact, Service, DetailService, DemanderServicer
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom du service'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description du service',
                'rows': 3
            })
        }

class DetailServiceForm(ModelForm):
    class Meta:
        model = DetailService
        fields = ['service', 'detail']
        widgets = {
            'service': forms.Select(attrs={
                'class': 'form-select'
            }),
            'detail': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Détail du service'
            })
        }

DetailServiceFormSet = inlineformset_factory(
    Service,
    DetailService,
    form=DetailServiceForm,
    extra=1,  
    can_delete=True  
)

class DemandeServiceForm(ModelForm):
    class Meta:
        model = DemanderServicer
        fields = ['nom', 'post_nom', 'phone_number', 'email']

        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre nom'
            }),
            'post_nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre post_nom'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre numéro de téléphone'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre adresse mail'
            })
        }

