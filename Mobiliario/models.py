from django.db import models

# Create your models here.
class Mobiliario(models.Model):
    numserie = models.IntegerField(primary_key=True)
    idempleado = models.IntegerField()
    lugar = models.IntegerField()
    descripcion = models.CharField(max_length=400)
