from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('contact/', views.contact, name="contact"),
    path('confirmation/', views.message_success, name="message_success"),
    path('ajoutservice/', views.ajouter_service, name="ajouter_service"),
    path('service/', views.liste_services, name="service"),
    path('service/<uuid:service_id>/demander-service/', views.demander_service, name="demander_service"),
]