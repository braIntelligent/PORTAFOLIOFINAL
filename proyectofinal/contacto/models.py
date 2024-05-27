from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    mensaje = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} - {self.correo}'

