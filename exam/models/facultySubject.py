from django.db import models
from .faculty import Faculty
from .subject import Subject


class FacultySubject(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.faculty.__str__() + '-' + self.subject.__str__()