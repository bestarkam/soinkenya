from django.db import models
import uuid
from django.utils import timezone


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nom = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=200, blank=False, null=False)
    disponible = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class DetailService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services", null=True)
    detail = models.CharField(max_length=100, blank=False, null=False)
    

    def __str__(self):
        return f"{self.service.nom}/{self.detail}"


class Temoignage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nom = models.CharField(max_length=30, blank=False, null=False)
    post_nom = models.CharField(max_length=30, blank=False, null=False)
    temoignage = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.temoignage


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nom_complet = models.CharField(max_length=100, blank=False, null=False)
    mail = models.EmailField(blank=False, null=False)
    telephone = models.CharField(max_length=20, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.nom_complet}"
