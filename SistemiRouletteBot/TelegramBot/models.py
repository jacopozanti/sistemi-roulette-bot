from django.db import models
from django.contrib import admin
from datetime import datetime
from django.utils.crypto import get_random_string

class Cliente(models.Model):
    username = models.CharField(max_length=50)
    id_telegram = models.CharField(max_length=12)
    note = models.TextField(blank=True)
    verificato = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.username
admin.site.register(Cliente)

class Subscription(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    inizio = models.DateField()
    scadenza = models.DateField()
    prezzo = models.IntegerField()

    def __str__(self):
        return '{} dal {} al {}'.format(self.cliente, self.inizio.strftime("%d/%m/%Y"), self.scadenza.strftime("%d/%m/%Y")) 
admin.site.register(Subscription)