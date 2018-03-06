from django.db import models


class Faculty(models.Model):
    facultyFullName = models.CharField(max_length=100)
    facultyEmail = models.CharField(max_length=200)
    facultyContactNumber = models.CharField(max_length=200)

    def __str__(self):
        return self.facultyFullName + '-' + self.facultyEmail