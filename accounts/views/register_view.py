
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été créé avec succès !")
            return redirect('accounts:login')  # Rediriger vers la page de connexion
        else:
            print("Formulaire invalide :", form.errors)
            messages.error(request, f"Erreurs : {form.errors}")
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
