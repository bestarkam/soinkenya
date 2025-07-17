# Utilise l'image officielle Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8000 pour Django
EXPOSE 8000

# Commande de démarrage par défaut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
