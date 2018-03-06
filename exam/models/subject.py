from django.db import models


class Subject(models.Model):
    subjectName = models.CharField(max_length=100)
    SEMESTER_CHOICES = (
        ('SEMESTER_1', 'SEMESTER 1'),
        ('SEMESTER_2', 'SEMESTER 2'),
        ('SEMESTER_3', 'SEMESTER 3'),
        ('SEMESTER_4', 'SEMESTER 4'),
        ('SEMESTER_5', 'SEMESTER 5'),
        ('SEMESTER_6', 'SEMESTER 6'),
        ('SEMESTER_7', 'SEMESTER 7'),
        ('SEMESTER_8', 'SEMESTER 8'),
    )
    semester = models.CharField(
        max_length=10,
        choices=SEMESTER_CHOICES,
        default='SEMESTER_1',
    )

    def __str__(self):
        return self.subjectName
