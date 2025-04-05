from django.db import models

class SiteTemplate(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(verbose_name="Description")
    #image = models.ImageField(upload_to='template_images/', verbose_name="Image de présentation")
    #demo_url = models.URLField(blank=True, null=True, verbose_name="URL de démonstration")

    def __str__(self):
        return self.name

# Create your models here.
