from django.db import models


class CurrencyRate(models.Model):
    currency = models.CharField(max_length=8)
    rate = models.FloatField()

    def __str__(self):
        return self.currency
