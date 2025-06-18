from django.forms import ModelForm
from app_sk.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'