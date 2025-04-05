from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('templates/', include('templates_manager.urls')),
    path('famm1/about', RedirectView.as_view(url='/static/famm1/about.html'), name='famm1_index'),
 

]
