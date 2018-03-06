from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from .subject import Subject


class SampleQuestion(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = RichTextUploadingField(max_length=1000000)

    def __str__(self):
        return 'Sample Question - ' + self.subject.__str__()
