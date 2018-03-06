from django.db import models


class Batch(models.Model):
    year = models.IntegerField(null=True)

    def __str__(self):
        return str(self.year)
