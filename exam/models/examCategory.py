from django.db import models
from .batchSectionSemester import BatchSectionSemester


class ExamCategory(models.Model):
    batchSectionSemester = models.ForeignKey(BatchSectionSemester, on_delete=models.CASCADE)
    TERM_CHOICES = (
        ('MID_TERM', 'MID TERM'),
        ('FINAL_TERM', 'FINAL TERM'),
        ('PRACTICAL', 'PRACTICAL'),
    )
    term = models.CharField(
        max_length=100,
        choices=TERM_CHOICES,
        default='MID_TERM',
    )

    def __str__(self):
        return self.batchSectionSemester.__str__() + '-' + self.term