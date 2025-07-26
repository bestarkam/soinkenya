from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from app_sk.forms import ContactForm, ServiceForm, DetailServiceFormSet, DemandeServiceForm
from app_sk.models import Service, Temoignage, Contact
from django.conf import settings
from django.contrib import messages

# Create your views here.
def index(request):
    temoignages = Temoignage.objects.all()
    leServices = Service.objects.all().order_by('disponible')
    
    
    context={
        'leServices' : leServices,
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


def afficherApropos(request):
    context = {
        'propos' : 'propos'
    }
    
    return render(request, 'app_sk/principal/propos.html', context)


def demander_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    details = service.services.all()

    if request.method == "POST" :
        form = DemandeServiceForm(request.POST)
        if form.is_valid():
            #enregistrer dans la base de donnees
            demande = form.save(commit=False)
            demande.service = service
            demande.save()

            #envoyer une notification par mail pour admin
            cd = form.cleaned_data
            subject = f"Nouvelle demande de service : {service.nom}"
            message = (
                f"Nom : {cd.get('nom')}\n"
                f"Post-nom : {cd.get('post_nom')}\n"
                f"Email : {cd.get('email')}\n"
                f"Téléphone : {cd.get('phone_number')}\n"
                f"Service demandé : {service.nom}"
            )
            send_mail(subject, message, cd.get('email'), [settings.CONTACT_EMAIL])

            return redirect('app_sk:message_success')
    else :
        form = DemandeServiceForm()

    context = {
        'service': service,
        'details' : details,
        'form' : form
    }

    return render(request, 'app_sk/service/demanderservice.html', context)


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