from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from app_sk.forms import ContactForm, ServiceForm, DetailServiceFormSet
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

 

def ajouter_service(request):
    if request.method == 'POST':
        service_form = ServiceForm(request.POST)
        formset = DetailServiceFormSet(request.POST)

        if service_form.is_valid() and formset.is_valid():
            service = service_form.save()
            formset.instance = service
            formset.save()
            return redirect('app_sk:index')
    else:
        service_form = ServiceForm()
        formset = DetailServiceFormSet()

    return render(request, 'app_sk/service/ajouter_service.html', {
        'service_form': service_form,
        'formset': formset,
    })


def liste_services(request):
    services = Service.objects.prefetch_related('services')
    context = {
        'services': services,
        'current_page' : 'service'
    }
    return render(request, 'app_sk/service/liste_services.html', context)


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