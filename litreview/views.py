from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def accueil(request):
    """Vue django"""
    return render(request, "pages/accueil.html")