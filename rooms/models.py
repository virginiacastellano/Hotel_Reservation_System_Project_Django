from django.db import models

# Create your models here.
class Chambre(models.Model):
    nom           = models.CharField(max_length=20)
    prix          = models.IntegerField()
    description   = models.TextField()
    image         = models.ImageField(upload_to='media/pics')
