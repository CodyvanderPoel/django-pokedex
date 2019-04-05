from django.db import models

# Create your models here.

class Pokemon(models.Model):
    nationalId = models.IntegerField()
    name = models.CharField(max_length=100)
    pokemonType = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    image = models.URLField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Pokemon"
