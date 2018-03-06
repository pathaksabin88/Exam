from django.db import models
from .examCategory import ExamCategory
from .facultySubject import FacultySubject


class ExamInfo(models.Model):
    examCategory = models.ForeignKey(ExamCategory, on_delete=models.CASCADE)
    facultySubject = models.ForeignKey(FacultySubject, on_delete=models.CASCADE)
    examDate = models.DateField(null=False)

    def __str__(self):
        return self.examCategory.__str__() + '-' + self.facultySubject.__str__()