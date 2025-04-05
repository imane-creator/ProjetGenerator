from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect('/famm1/about')  # Remplacez 'home' par le nom de votre vue d'accueil
        else:
            # Si le formulaire est invalide, affiche les erreurs
            print("Formulaire invalide :", form.errors)
            messages.error(request, f"Erreurs : {form.errors}")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})
