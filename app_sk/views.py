from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from app_sk.forms import ContactForm
from app_sk.models import Service, Temoignage, Contact
from django.conf import settings

# Create your views here.
def index(request):
    temoignages = Temoignage.objects.all()
    context={
        'temoignages' : temoignages,
        'current_page' : 'index'
    }
    return render(request, 'app_sk/index.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #enregistrer dans la base de donnees
            form.save()
            
            #envoyer une notification par mail
            cd = form.cleaned_data
            subject = f"Contact depuis le site - Objet dans le corps du message"
            message = f"Nom : {cd['nom_complet']}\nmail : {cd['mail']}\nTéléphone : {cd['telephone']}\n\nMessage:\n{cd['message']}"
            send_mail(subject, message, cd['mail'], [settings.CONTACT_EMAIL])
            return redirect('app_sk:message_success')
    else:
        form = ContactForm()

    context={
        'form': form,
        'current_page':'contact'
    }

    return render(request, 'app_sk/principal/contact.html', context)

def message_success(request):
    return render(request, 'app_sk/principal/contact_success.html')