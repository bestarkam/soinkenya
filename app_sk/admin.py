from django.contrib import admin
from app_sk.models import Service, Temoignage, Contact, DetailService, DemanderServicer

# Register your models here.

admin.site.register(Service)
admin.site.register(DetailService)
admin.site.register(DemanderServicer)
admin.site.register(Temoignage)
admin.site.register(Contact)
