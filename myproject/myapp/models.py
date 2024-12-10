from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
