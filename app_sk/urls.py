from django.urls import path
from . import views


urlpatterns=[
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name="contact"),
    path('confirmation/', views.message_success, name="message_success"),
]