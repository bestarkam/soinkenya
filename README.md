# Soin Kenya — Plateforme de liaison médicale RDC ↔ Kenya

![Django](https://img.shields.io/badge/Django-5.2.2-092E20?style=flat&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Storage-Cloudinary-3448C5?style=flat&logo=cloudinary&logoColor=white)
![License](https://img.shields.io/badge/Licence-MIT-green?style=flat)

---

## À propos du projet

**Soin Kenya** est une plateforme web développée avec Django, destinée à accompagner les patients congolais (RDC) atteints de cancer souhaitant se faire soigner au Kenya. Elle centralise les informations sur les services d'accompagnement médical, facilite les demandes de prise en charge et recueille les témoignages de patients.

---

## Fonctionnalités

| Page | Description |
|---|---|
| **Accueil** (`/`) | Présentation de la mission, aperçu des services, témoignages récents |
| **Services** (`/services`) | Liste dynamique des services disponibles avec description, image et tarif |
| **Demande de service** | Formulaire de demande lié à un service spécifique, notification email à l'admin |
| **Témoignages** | Affichage des témoignages de patients (modérés via l'administration) |
| **Contact** (`/contact`) | Formulaire de contact avec envoi d'email automatique |
| **À propos** | Présentation de l'équipe et de la mission |
| **Admin Django** | Gestion complète du contenu via le panneau d'administration |

---

## Modèles de données

```
Service          → nom, description, phrase phare, image (Cloudinary), prix, disponibilité
DetailService    → détails associés à un service (relation FK)
DemanderService  → demandes de prise en charge des patients
Temoignage       → témoignages patients (contrôle de visibilité)
Contact          → messages reçus via le formulaire de contact
```

---

## Stack technique

- **Backend** : Django 5.2.2
- **Base de données** : PostgreSQL (`psycopg2-binary`) / SQLite (développement)
- **Stockage médias** : Cloudinary + `django-cloudinary-storage`
- **Fichiers statiques** : WhiteNoise
- **Déploiement** : Gunicorn
- **Configuration** : `python-decouple` (variables d'environnement)
- **Images** : Pillow

---

## Installation

### Prérequis

- Python 3.10+
- pip
- Un compte [Cloudinary](https://cloudinary.com/) (gratuit)
- Un serveur SMTP (ex : Gmail)

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-username/soinkenya.git


# 2. Créer et activer l'environnement virtuel
python -m venv sk_env
sk_env\Scripts\activate        # Windows
# source sk_env/bin/activate   # Linux / macOS

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
cp .env.example .env
# Remplissez .env avec vos valeurs (voir ci-dessous)

# 5. Appliquer les migrations
python manage.py migrate

# 6. Charger les données initiales (optionnel)
python manage.py loaddata data.json

# 7. Créer un superutilisateur
python manage.py createsuperuser

# 8. Lancer le serveur
python manage.py runserver
```

Accédez à l'application sur [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Variables d'environnement (`.env`)

```env
SECRET_KEY=votre_cle_secrete_django
DEBUG=True

# Base de données (PostgreSQL en production)
DATABASE_URL=postgres://user:password@host:5432/dbname

# Email (SMTP)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=votre@email.com
EMAIL_HOST_PASSWORD=votre_mot_de_passe_application
CONTACT_EMAIL=contact@soinkenya.com

# Cloudinary
CLOUDINARY_CLOUD_NAME=votre_cloud_name
CLOUDINARY_API_KEY=votre_api_key
CLOUDINARY_API_SECRET=votre_api_secret
```

---

## Structure du projet

```
soinkenya/
├── app_sk/                  # Application principale
│   ├── models.py            # Modèles de données
│   ├── views.py             # Logique métier & vues
│   ├── forms.py             # Formulaires Django
│   ├── urls.py              # Routes de l'application
│   ├── admin.py             # Configuration du panneau admin
│   ├── templates/           # Templates HTML
│   └── static/              # Fichiers CSS, JS, images
├── projet_sk/               # Configuration Django du projet
├── requirements.txt         # Dépendances Python
├── manage.py
└── .env                     # Variables d'environnement (non versionné)
```

---

## Déploiement

Le projet est prêt pour un déploiement sur des plateformes comme **Railway**, **Render** ou **Heroku** grâce à :
- `gunicorn` comme serveur WSGI
- `whitenoise` pour les fichiers statiques
- `python-decouple` pour la gestion sécurisée des secrets

```bash
# Collecter les fichiers statiques avant déploiement
python manage.py collectstatic --noinput
```

---

## Licence

Ce projet est distribué sous licence **MIT**. Voir le fichier `LICENSE` pour plus de détails.

---

> *Simplifier le voyage médical des patients congolais vers le Kenya, étape par étape.*
