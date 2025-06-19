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


def demander_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == "POST" :
        form = DemandeServiceForm(request.POST)
        if form.is_valid():
            #enregistrer dans la base de donnees
            demande = form.save(commit=False)
            demande.service = service
            demande.save()
            #notifier l'utilisateur
            messages.success(request, f"Votre demande a été envoyé avec succès; nous vous repondrons dans moins de 24h.")

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

            return redirect('app_sk:service')
    else :
        form = DemandeServiceForm()

    context = {
        'service': service,
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