# LITRevu - Projet 9 OpenClassrooms

Application web développée avec Django dans le cadre du projet 9 du parcours Python OpenClassrooms.

## Objectif du projet

LITRevu est une application web permettant à des utilisateurs de demander, publier et consulter des critiques de livres ou d'articles.

Le projet devra permettre à un utilisateur de :

- s'inscrire et se connecter ;
- créer un ticket pour demander une critique ;
- créer une critique ;
- créer une critique en réponse à un ticket ;
- créer un ticket et une critique en une seule étape ;
- suivre d'autres utilisateurs ;
- consulter un flux personnalisé ;
- modifier et supprimer ses propres contenus.

## Technologies utilisées

- Python
- Django
- SQLite
- Git

## Installation locale

Cloner le repository :

git clone https://github.com/mrnlarue-cloud/Projet_9_OC.git

Entrer dans le dossier du projet :

cd Projet_9_OC

Créer un environnement virtuel :

Sur Windows :

python -m venv venv

Sur macOS ou Linux :

python3 -m venv venv

Activer l'environnement virtuel :

Sur Windows PowerShell :

.\venv\Scripts\Activate.ps1

Sur macOS ou Linux :

source venv/bin/activate

Installer les dépendances :

pip install -r requirements.txt

Lancer le serveur de développement :

python manage.py runserver

Le site est ensuite accessible à l'adresse suivante :

http://127.0.0.1:8000/

## État actuel du projet

Le projet est en cours d'initialisation.

Éléments déjà mis en place :

- environnement virtuel local ;
- fichier .gitignore ;
- fichier README ;
- installation de Django ;
- fichier requirements.txt ;
- création du projet Django ;
- vérification du lancement du serveur local.

Le projet Django utilise pour le moment un dossier de configuration nommé :

configuration/

Aucune application Django métier n'a encore été créée.

Aucune migration n'a encore été effectuée.

## Notes de développement

Les migrations seront faites plus tard, après décision sur le modèle utilisateur personnalisé.

Le fichier db.sqlite3 n'est donc pas encore versionné à ce stade du projet.