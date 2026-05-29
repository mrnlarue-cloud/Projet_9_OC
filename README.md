# LITRevu - Projet 9 OpenClassrooms

Application web développée avec Django dans le cadre du projet 9 du parcours Python OpenClassrooms.

LITRevu permet à des utilisateurs de demander, publier et consulter des critiques de livres ou d'articles.  
Chaque utilisateur dispose d'un flux personnalisé basé sur ses propres publications, les utilisateurs qu'il suit, et les critiques reçues sur ses demandes.

---

## Sommaire

1. [Objectif du projet](#objectif-du-projet)
2. [Fonctionnalités](#fonctionnalités)
3. [Technologies utilisées](#technologies-utilisées)
4. [Installation locale](#installation-locale)
5. [Lancement du projet](#lancement-du-projet)
6. [Utilisation de l'application](#utilisation-de-lapplication)
7. [Structure du projet](#structure-du-projet)
8. [Base de données et fichiers médias](#base-de-données-et-fichiers-médias)
9. [Qualité du code](#qualité-du-code)
10. [Commandes utiles](#commandes-utiles)
11. [Auteur](#auteur)

---

## Objectif du projet

Le projet LITRevu a pour objectif de créer une application web permettant à des utilisateurs de :

- demander des critiques de livres ou d'articles ;
- publier des critiques ;
- répondre à des demandes de critique ;
- suivre d'autres utilisateurs ;
- consulter un flux personnalisé ;
- gérer leurs propres publications.

L'application utilise l'architecture Django classique :

- les **modèles** portent les données et la logique métier ;
- les **vues** coordonnent les requêtes et les réponses ;
- les **templates** affichent les pages HTML.

---

## Fonctionnalités

### Authentification

Un visiteur peut :

- créer un compte ;
- se connecter ;
- se déconnecter.

Un utilisateur non connecté ne peut accéder qu'aux pages de connexion et d'inscription.

---

### Publications

Une fois connecté, l'utilisateur accède à une page d'accueil contenant les publications visibles.

La page d'accueil affiche :

- les tickets visibles ;
- les critiques visibles ;
- les tickets et critiques mélangés dans un même flux ;
- les publications triées de la plus récente à la plus ancienne.

---

### Tickets

Un ticket correspond à une demande de critique.

L'utilisateur connecté peut :

- créer un ticket ;
- ajouter un titre ;
- ajouter une description ;
- ajouter une image optionnelle ;
- modifier ses propres tickets ;
- supprimer ses propres tickets après confirmation.

---

### Critiques

Une critique est associée à un ticket.

L'utilisateur connecté peut :

- créer une critique en réponse à un ticket ;
- attribuer une note ;
- ajouter un titre ;
- ajouter un commentaire ;
- modifier ses propres critiques ;
- supprimer ses propres critiques après confirmation.

Un utilisateur ne peut pas créer deux critiques pour le même ticket.

---

### Abonnements

L'utilisateur connecté peut :

- suivre un autre utilisateur en saisissant son nom d'utilisateur ;
- consulter la liste des utilisateurs suivis ;
- se désabonner d'un utilisateur.

Le formulaire d'abonnement gère les cas suivants :

- utilisateur inexistant ;
- tentative de se suivre soi-même ;
- tentative de suivre deux fois le même utilisateur.

---

### Mes posts

La page **Mes posts** permet à l'utilisateur connecté de consulter ses propres contenus :

- ses tickets ;
- ses critiques.

Les contenus sont affichés du plus récent au plus ancien.

Depuis cette page, l'utilisateur peut modifier ou supprimer ses propres publications.

---

### Création d'une critique à partir de zéro

L'application doit permettre de créer une critique sans répondre à un ticket existant.

Cette fonctionnalité consiste à créer en une seule étape :

- un ticket décrivant le livre ou l'article ;
- une critique associée à ce ticket ;
- une note.

---

## Technologies utilisées

- Python
- Django
- SQLite
- HTML
- Bootstrap
- Crispy Forms
- Git

---

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

---

## Lancement du projet

Lancer le serveur de développement :

```bash
python manage.py runserver
```

Le site est ensuite accessible à l'adresse suivante :

```text
http://127.0.0.1:8000/
```

La racine du site redirige vers la page d'accueil.

---

## Utilisation de l'application

### Créer un compte

Depuis la page d'inscription, saisir un nom d'utilisateur et un mot de passe.

### Se connecter

Depuis la page de connexion, saisir ses identifiants.

### Créer une demande de critique

Depuis l'accueil, cliquer sur le bouton de création de ticket, puis remplir le formulaire.

### Créer une critique

Depuis une publication de type ticket, cliquer sur le bouton permettant de créer une critique.

### Gérer ses publications

Depuis la page **Mes posts**, l'utilisateur peut consulter, modifier ou supprimer ses propres tickets et critiques.

### Gérer ses abonnements

Depuis la page **Abonnements**, l'utilisateur peut suivre un autre utilisateur ou se désabonner.

---

## Structure du projet

```text
Projet_9/
│
├── configuration/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── litreview/
│   ├── migrations/
│   ├── templates/
│   │   └── pages/
│   │       ├── temp_partiels/
│   │       ├── accueil.html
│   │       ├── abonnements.html
│   │       ├── base.html
│   │       ├── connexion.html
│   │       ├── inscription.html
│   │       ├── creer_ticket.html
│   │       ├── creer_critique.html
│   │       ├── modifier_ticket.html
│   │       ├── modifier_critique.html
│   │       ├── mes_posts.html
│   │       ├── confirmer_suppression_ticket.html
│   │       └── confirmer_suppression_critique.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## Base de données et fichiers médias

Le projet utilise SQLite comme base de données locale.

Le fichier suivant doit être inclus dans le repository :

```text
db.sqlite3
```

Les images envoyées par les utilisateurs sont stockées dans :

```text
media/
```

Le dossier `media/` ne doit pas être suivi par Git, car il contient des fichiers envoyés localement pendant l'utilisation du site.

---

## Qualité du code

Avant chaque commit important, les commandes suivantes ont été utilisées :

```bash
black .
flake8
python manage.py check
```

Le projet suit les principes suivants :

- code lisible ;
- noms explicites ;
- logique métier placée dans les modèles ;
- vues simples ;
- templates organisés ;
- commits précis et séparés.

---

## Commandes utiles

### Lancer le serveur

```bash
python manage.py runserver
```

### Vérifier le projet Django

```bash
python manage.py check
```

### Formater le code

```bash
black .
```

### Vérifier la qualité du code

```bash
flake8
```

### Vérifier l'état Git

```bash
git status
```

---

## Notes de développement

Le projet utilise un modèle utilisateur personnalisé :

```python
AUTH_USER_MODEL = "litreview.User"
```

La logique métier principale est portée par les modèles Django, notamment pour :

- le flux de publications ;
- les abonnements ;
- la création de tickets ;
- la création de critiques ;
- la modification des contenus ;
- la suppression des contenus.

Les vues restent volontairement simples : elles reçoivent la requête, appellent les méthodes des modèles, puis renvoient une réponse ou une redirection.

---

## Auteur

Projet réalisé par Marion LARUE dans le cadre du parcours Python OpenClassrooms.