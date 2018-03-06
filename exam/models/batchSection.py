from django.db import models
from .batch import Batch


class BatchSection(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    section = models.CharField(max_length=10)

    def __str__(self):
        return self.batch.__str__() + '-' + self.section
