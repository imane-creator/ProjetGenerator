
from django.urls import path, include
from .views import  templates_list
from django.views.generic import RedirectView
from accounts.views.profile_view import profile
from django.contrib.auth.views import LogoutView
 

app_name ='templates_manager'
urlpatterns = [
  path("template/", templates_list, name="login"),
  path('famm1/about', RedirectView.as_view(url='/static/famm1/about.html')),
  path('profile/', profile, name='profile'),
  path('logout/', LogoutView.as_view(), name='logout'),   # URL pour afficher le profil

  # path('about/', about_view, name='about'),


]
# app_name = 'static'

# urlpatterns = [
#       path('about/', about_view, name='about'),

# ]