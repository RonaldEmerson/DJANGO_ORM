#from django.utils.html import format_html

#from .choices import sexos
# Create your models here.


from django.db import models

class Docente(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombres')

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.ForeignKey(Docente, null=True, blank=True, on_delete=models.CASCADE)

