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

### 1. Cloner le repository

```bash
git clone https://github.com/mrnlarue-cloud/Projet_9_OC.git
```

### 2. Entrer dans le dossier du projet

```bash
cd Projet_9_OC
```

### 3. Créer un environnement virtuel

Sur Windows :

```powershell
python -m venv venv
```

Sur macOS ou Linux :

```bash
python3 -m venv venv
```

### 4. Activer l'environnement virtuel

Sur Windows PowerShell :

```powershell
.\venv\Scripts\Activate.ps1
```

Sur macOS ou Linux :

```bash
source venv/bin/activate
```

### 5. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 6. Lancer le serveur de développement

```bash
python manage.py runserver
```

Le site est ensuite accessible à l'adresse suivante :

```text
http://127.0.0.1:8000/
```