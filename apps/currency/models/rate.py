from django.db import models

class Rate(models.Model):

    currency = models.ForeignKey('currency', on_delete=models.PROTECT)
    rate = models.DecimalField(max_digits=6, decimal_places=3)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.currency, self.rate)

    class Meta:
        ordering = ['-create_time']
