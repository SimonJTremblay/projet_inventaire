from django.db import models


class Produit(models.Model):
    Nom = models.CharField(max_length=100)
    Description = models.TextField()
    Type = models.CharField(max_length=50)
    QuantiteStock = models.IntegerField()
    SeuilMinimum = models.IntegerField()

    def __str__(self):
        return self.Nom
    