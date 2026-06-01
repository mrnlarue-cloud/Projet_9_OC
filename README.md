# LITRevu - Projet 9 OpenClassrooms

Application web développée avec Django dans le cadre du projet 9 du parcours Python OpenClassrooms.

LITRevu permet à des utilisateurs de demander, publier et consulter des critiques de livres ou d'articles.  
Chaque utilisateur dispose d'un flux personnalisé basé sur ses propres publications, les utilisateurs qu'il suit, et les critiques reçues à sa demande.

---

## Sommaire

1. [Objectif du projet](#objectif-du-projet)
2. [Fonctionnalités](#fonctionnalités)
3. [Comptes de test](#comptes-de-test)
4. [Technologies utilisées](#technologies-utilisées)
5. [Installation locale](#installation-locale)
6. [Lancement du projet](#lancement-du-projet)
7. [Utilisation de l'application](#utilisation-de-lapplication)
8. [Structure du projet](#structure-du-projet)
9. [Base de données et fichiers médias](#base-de-données-et-fichiers-médias)
10. [Qualité du code](#qualité-du-code)
11. [Commandes utiles](#commandes-utiles)
12. [Notes de développement](#notes-de-développement)
13. [Auteur](#auteur)

---

## Objectif du projet

Le projet LITRevu a pour objectif de créer une application web permettant à ses utilisateurs de :

- Demander des critiques de livres ou d'articles ;
- Publier des critiques ;
- Répondre à des demandes de critique ;
- Suivre d'autres utilisateurs ;
- Consulter un flux personnalisé ;
- Gérer leurs propres publications.

L'application suit l'architecture Django classique :

- Les **Modèles** portent les données et la logique métier ;
- les **Vues** coordonnent les requêtes et les réponses ;
- les **Templates** affichent les pages HTML.

J'ai choisi de garder une architecture assez simple, avec une seule application principale `litreview`, afin que le projet reste lisible et facile à expliquer.

---

## Fonctionnalités

### Authentification

Un visiteur peut :

- Créer un compte ;
- Se connecter.

Un utilisateur connecté peut :

- Accéder aux pages protégées ;
- Se déconnecter.

Un utilisateur non connecté ne peut accéder qu'aux pages de connexion et d'inscription.

---

### Flux de publications

Une fois connecté, l'utilisateur arrive sur sa page d'accueil.

Le flux affiche :

- Les tickets visibles ;
- Les critiques visibles ;
- Les tickets et critiques mélangés dans une seule liste ;
- Les publications triées de la plus récente à la plus ancienne.

Le flux prend en compte :

- Les publications de l'utilisateur connecté ;
- Les publications des utilisateurs suivis ;
- Les critiques publiées en réponse aux tickets de l'utilisateur connecté.

---

### Tickets

Un ticket correspond à une demande de critique.

L'utilisateur connecté peut :

- Créer un ticket ;
- Ajouter un titre ;
- Ajouter une description ;
- Ajouter une image optionnelle ;
- Modifier ses propres tickets ;
- Remplacer l'image d'un ticket ;
- Supprimer ses propres tickets après confirmation.

---

### Critiques

Une critique est associée à un ticket.

L'utilisateur connecté peut :

- Créer une critique en réponse à un ticket ;
- Attribuer une note de 0 à 5 ;
- Ajouter un titre ;
- Ajouter un commentaire ;
- Modifier ses propres critiques ;
- Supprimer ses propres critiques après confirmation.

Un utilisateur ne peut pas créer deux critiques pour le même ticket.

---

### Créer un ticket avec sa critique

L'application permet aussi de créer un ticket et une critique en une seule étape.

Cette fonctionnalité sert à publier une critique à partir de zéro :

- Création du ticket décrivant le livre ou l'article ;
- Création de la critique associée ;
- Attribution d'une note ;
- Association automatique des deux contenus à l'utilisateur connecté.

---

### Abonnements

L'utilisateur connecté peut :

- Suivre un autre utilisateur en saisissant son nom d'utilisateur ;
- Consulter la liste des utilisateurs suivis ;
- Se désabonner après une page de confirmation.

Le formulaire d'abonnement gère les cas suivants :

- Utilisateur inexistant ;
- Tentative de se suivre soi-même ;
- Tentative de suivre deux fois le même utilisateur.

---

### Mes posts

La page **Mes posts** permet à l'utilisateur connecté de consulter ses propres contenus :

- Ses propres tickets ;
- Ses propres critiques.

Les contenus sont affichés du plus récent au plus ancien.

Depuis cette page, l'utilisateur peut modifier ou supprimer ses propres publications.

---

### Interface

L'interface utilise Bootstrap et Crispy Forms.

J'ai ajouté un style personnalisé directement dans le template de base, avec un thème sombre et des touches dorées.  
L'objectif était de garder une interface simple, mais plus cohérente avec l'univers d'un site de critiques littéraires.

---

## Comptes de test

La base de données fournie contient des données de démonstration.

Compte administrateur :

```text
Nom d'utilisateur : Lecteur0
Mot de passe : abcd0123!
Rôle : administrateur
```

Ce compte permet d'accéder à l'administration Django :

```text
http://127.0.0.1:8000/admin/
```

Les autres comptes lecteurs présents dans la base peuvent être utilisés pour tester :

- Le flux ;
- Les abonnements ;
- Les demandes de critique ;
- Les critiques entre utilisateurs.

---

## Technologies utilisées

- Python 3.11
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

La racine du site redirige automatiquemnt vers la page d'accueil.

---

## Utilisation de l'application

### Créer un compte

Depuis la page d'inscription, saisir un nom d'utilisateur et un mot de passe.

### Se connecter

Depuis la page de connexion, saisir ses identifiants.

### Créer une demande de critique

Depuis l'accueil, cliquer sur **Demander une critique**, puis remplir le formulaire du ticket.

### Créer une critique en réponse à un ticket

Depuis un ticket visible dans le flux, cliquer sur **Créer une critique**, puis remplir le formulaire.

### Créer un ticket avec sa critique

Depuis l'accueil, cliquer sur **Créer un ticket avec sa critique**.

Cette page contient deux parties :

- Le ticket, pour présenter le livre ou l'article ;
- La critique, pour donner son avis et sa note.

### Gérer ses publications

Depuis la page **Mes posts**, l'utilisateur peut consulter, modifier ou supprimer ses propres tickets et critiques.

Les suppressions passent par une page de confirmation.

### Gérer ses abonnements

Depuis la page **Abonnements**, l'utilisateur peut suivre un autre utilisateur en saisissant son nom d'utilisateur.

Il peut aussi se désabonner d'un utilisateur suivi.  
Le désabonnement passe également par une page de confirmation.

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
│   │       │   ├── review.html
│   │       │   ├── ticket.html
│   │       │   └── ticket_reponse.html
│   │       ├── accueil.html
│   │       ├── abonnements.html
│   │       ├── base.html
│   │       ├── connexion.html
│   │       ├── inscription.html
│   │       ├── creer_ticket.html
│   │       ├── creer_critique.html
│   │       ├── creer_critique_avec_ticket.html
│   │       ├── modifier_ticket.html
│   │       ├── modifier_critique.html
│   │       ├── mes_posts.html
│   │       ├── confirmer_desabonnement.html
│   │       ├── confirmer_suppression_ticket.html
│   │       └── confirmer_suppression_critique.html
│   │
│   ├── admin.py
│   ├── apps.py
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

Le fichier suivant est inclus dans le repository :

```text
db.sqlite3
```

Il contient des données de démonstration pour tester l'application.

Les images de démonstration sont stockées dans :

```text
media/
```

Le dossier `media/` est inclus dans le repository afin que les couvertures de livres affichées dans les tickets soient visibles lors d'une installation locale.

---

## Qualité du code

Les commandes suivantes ont été utilisées :

```bash
black .
flake8
python manage.py check
```

Le projet suit les principes suivants :

- Code lisible ;
- Noms explicites ;
- Logique métier placée principalement dans les modèles ;
- Vues simplifiées le plus possible ;
- Templates organisés avec des partiels réutilisables ;
- Commits précis et séparés.

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

### Vérifier qu'aucune migration n'est oubliée

```bash
python manage.py makemigrations --check --dry-run
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

Les modèles principaux sont :

- `User` ;
- `Ticket` ;
- `Review` ;
- `UserFollows`.

La logique métier principale est portée par les modèles Django, notamment pour :

- Le flux de publications ;
- Les abonnements ;
- La création de tickets ;
- La création de critiques ;
- La création d'un ticket avec sa critique ;
- La modification des contenus ;
- La suppression des contenus ;
- Les protections liées à l'utilisateur connecté.

Les vues restent volontairement simples : elles reçoivent la requête, instancient les formulaires, appellent les méthodes des modèles, puis renvoient une réponse ou une redirection.

Les templates sont découpés avec des partiels pour éviter de répéter le code d'affichage des tickets et des critiques.

---

## Auteur

Projet réalisé par Marion LARUE dans le cadre du parcours Python OpenClassrooms.