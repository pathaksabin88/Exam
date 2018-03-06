from django.contrib import admin
from .models import Batch, BatchSection, BatchSectionSemester, ExamCategory, ExamInfo, FacultySubject, Faculty, Subject, SampleQuestion

# Register your models here.

admin.site.register(Batch)
admin.site.register(BatchSection)
admin.site.register(BatchSectionSemester)
admin.site.register(ExamCategory)
admin.site.register(Subject)
admin.site.register(Faculty)
admin.site.register(ExamInfo)
admin.site.register(FacultySubject)
admin.site.register(SampleQuestion)