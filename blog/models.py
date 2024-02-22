from django.db import models

class Post(models.Model):
    title = models.CharField(verbose_name='Título del post', max_length=150)
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to="blog/images")
    date = models.DateField(verbose_name='Fecha')

    def __str__(self):
        return self.title