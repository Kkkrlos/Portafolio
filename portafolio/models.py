from django.db import models

class Project(models.Model):
    title = models.CharField(verbose_name="Título del proyecto", max_length=100)
    description = models.CharField(verbose_name="Descripción", max_length=250)
    image = models.ImageField(verbose_name="Imagen", upload_to="portafolio/images/")
    url = models.URLField(verbose_name="URL", blank=True)

    def __str__(self):
        return self.title