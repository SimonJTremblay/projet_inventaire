from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Produit(models.Model):
    Nom = models.CharField(max_length=100)
    Description = models.TextField()
    Type = models.CharField(max_length=50)
    QuantiteStock = models.IntegerField(validators=[MinValueValidator(0)])
    SeuilMinimum = models.IntegerField(default=0)

    def __str__(self):
        return self.Nom

    def get_absolute_url(self):
        return reverse('produit-detail', kwargs={'pk': self.pk})
