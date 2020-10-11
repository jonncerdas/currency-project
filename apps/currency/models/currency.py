from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ['code']
        verbose_name_plural = 'Currencies'
