# Plateforme de liaison médicale RDC - Kenya

## Objectif du projet

Ce projet Django a pour objectif de créer un site web dynamique destiné à faciliter le processus de prise en charge des patients congolais atteints de cancer souhaitant se faire soigner au Kenya.

La plateforme permet de :
- Présenter les services offerts pour accompagner les malades dans toutes les étapes du voyage médical.
- Fournir un formulaire de contact sécurisé pour entrer en relation avec l’équipe.
- Partager les témoignages de patients ayant déjà bénéficié du service.

---

## Fonctionnalités principales

### Page d’accueil (`/`)
- Présentation de la mission
- Brève description des services
- Témoignages récents
- Lien vers contact

### Page Services (`/services`)
- Liste dynamique des services disponibles (modèle `Service`)
- Description détaillée de chaque service
- Possibilité de mise à jour via l’admin

### Page Contact (`/contact`)
- Formulaire de contact dynamique (modèle `Contact`)
  - Nom
  - Email
  - Téléphone
  - Message
- Notifications par e-mail à l’admin (via SMTP)

### Témoignages (`/temoignages`)
- Affichage des témoignages enregistrés (modèle `Temoignage`)
- Nom du patient (anonymisé si besoin), date, contenu du témoignage
- Ajout/modération via le panneau d’administration Django

---

## Modèles Django

# models.py (extrait simplifié)
class Service(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    message = models.TextField()
    date_envoye = models.DateTimeField(auto_now_add=True)

class Temoignage(models.Model):
    nom = models.CharField(max_length=100)
    contenu = models.TextField()
    date = models.DateField(auto_now_add=True)
