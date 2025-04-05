
import os
from django.shortcuts import render, get_object_or_404
from .models import SiteTemplate
from django.http import FileResponse, JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader

# Liste des templates
def templates_list(request):
    templates = SiteTemplate.objects.all()
    return render(request, 'templates_manager/list_template.html', {'templates': templates})

def famm1_index(request):
    return render(request, 'famm1/index.html')


def famm1_index_static(request):
    file_path = os.path.join('static', 'famm1', 'index.html')
    return FileResponse(open(file_path, 'rb'))

# views.py
# def about_view(request):
#     context = {
#         "title": "About us"
#     }
#     return render(request, "about.html", context)

# def about_view(request):
#     # Charger le modèle
#     template = loader.get_template('about.html')
    
#     # Créer un dictionnaire de contexte
#     context = {
#         "title": "About us"
#     }
    
#     # Rendre le template avec le contexte et retourner la réponse HTTP
#     return HttpResponse(template.render(context, request))
# # views.py
# def about_view(request):
#     context = {
#         "title": "About us",
#         "heading": "Why Shop With Us",
#         "cards": [
#             {
#                 "icon": "a-solid fa-keyboard",  # Fast Delivery icon
#                 "title": "Fast Delivery",
#                 "description": "Variations of passages of Lorem Ipsum available"
#             },
#             {
#                 "icon": "fa-solid fa-box-open",  # Free Shipping icon
#                 "title": "Free Shipping",
#                 "description": "Variations of passages of Lorem Ipsum available"
#             },
#             {
#                 "icon": "fa-solid fa-star",  # Best Quality icon
#                 "title": "Best Quality",
#                 "description": "Variations of passages of Lorem Ipsum available"
#             },
#         ]
#     }
#     return render(request, "about.html", context)
def about_view(request):
    # Charger le modèle
    template = loader.get_template('about.html')
    
    # Créer un dictionnaire de contexte avec le titre spécifique
    context = {
        'title': 'About Us'  # Valeur pour le titre
    }
    
    # Rendre le template avec le contexte et retourner la réponse HTTP
    return HttpResponse(template.render(context, request))

# Détail d'un template
def template_detail(request, pk):
   template = get_object_or_404(SiteTemplate, pk=pk)
   return render(request, 'templates_manager/template_detail.html', {'template': template})




