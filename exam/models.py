from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Batch(models.Model):
    year = models.IntegerField(null=True)

    def __str__(self):
        return str(self.year)


class BatchSection(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    section = models.CharField(max_length=10)

    def __str__(self):
        return self.batch.__str__() + '-' + self.section


class BatchSectionSemester(models.Model):
    batchSection = models.ForeignKey(BatchSection, on_delete=models.CASCADE)
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
        return self.batchSection.__str__() + '-' + self.semester


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


class Faculty(models.Model):
    facultyFullName = models.CharField(max_length=100)
    facultyEmail = models.CharField(max_length=200)
    facultyContactNumber = models.CharField(max_length=200)

    def __str__(self):
        return self.facultyFullName + '-' + self.facultyEmail


class FacultySubject(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.faculty.__str__() + '-' + self.subject.__str__()


class ExamInfo(models.Model):
    examCategory = models.ForeignKey(ExamCategory, on_delete=models.CASCADE)
    facultySubject = models.ForeignKey(FacultySubject, on_delete=models.CASCADE)
    examDate = models.DateField(null=False)

    def __str__(self):
        return self.examCategory.__str__() + '-' + self.facultySubject.__str__()


class SampleQuestion(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = RichTextUploadingField(max_length=1000000)

    def __str__(self):
        return 'Sample Question - ' + self.subject.__str__()
