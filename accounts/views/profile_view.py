from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')  # Vous pouvez personnaliser la page de profil
