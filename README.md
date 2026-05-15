LITRevu - Projet 9 OpenClassrooms

Application web développée avec Django dans le cadre du projet 9 du parcours Python OpenClassrooms.

Objectif du projet

LITRevu est une application web permettant à des utilisateurs de demander, publier et consulter des critiques de livres ou d'articles.

Fonctionnalités principales prévues :

inscription et connexion des utilisateurs ;
création de tickets pour demander une critique ;
création de critiques ;
création d'une critique en réponse à un ticket ;
création d'un ticket et d'une critique en une seule étape ;
suivi d'autres utilisateurs ;
affichage d'un flux personnalisé ;
modification et suppression de ses propres contenus.
Installation du projet
1. Récupérer le projet

Cloner le repository GitHub :

git clone <url-du-repository>

Entrer dans le dossier du projet :

cd <nom-du-repository>

2. Créer un environnement virtuel

Sur Windows :

python -m venv venv

Sur macOS ou Linux :

python3 -m venv venv

3. Activer l'environnement virtuel

Sur Windows PowerShell :

.\venv\Scripts\Activate.ps1

Sur macOS ou Linux :

source venv/bin/activate

4. Installer les dépendances

pip install -r requirements.txt

5. Lancer le serveur de développement

python manage.py runserver

Le site sera accessible à l'adresse suivante :

http://127.0.0.1:8000/