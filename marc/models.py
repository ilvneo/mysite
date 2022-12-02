# -*- coding: utf-8 -*-
import os.path

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    objects = None
    department = models.TextField()
    name = models.TextField()
    relate_Competency = models.TextField()
    education_part = models.TextField()
    education_type = models.TextField()
    education_institute = models.TextField()
    education_start = models.DateTimeField()
    education_end = models.DateTimeField()
    education_time = models.TextField()
    education_cost = models.TextField()
    certificate_item = models.TextField()
    memo = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    docfile1 = models.FileField(upload_to='documents/%Y/%m/%d')
    docfile2 = models.FileField(upload_to='documents/%Y/%m/%d')
    doctype1 = models.TextField()
    doctype2 = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content


# class Document(models.Model):
#     attached = models.FileField('첨부 파일', upload_to='documents/%Y/%m/%d')
#     create_date = models.DateTimeField()
#     modify_date = models.DateTimeField(null=True, blank=True)
#
#     def get_filename(self):
#         return os.path.basename(self.attached.name)
#
#     def __str__(self):
#         return self.attached.name

class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField('첨부파일', upload_to="result/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

    def get_filename(self):
        return os.path.basename(self.uploadedFile.name)


class EduInstitution(models.Model):
    eduInsName = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content


