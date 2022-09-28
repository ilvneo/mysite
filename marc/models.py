# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    objects = None
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    docfile1 = models.FileField(upload_to='documents/%Y/%m/%d')
    docfile2 = models.FileField(upload_to='documents/%Y/%m/%d')
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


class Document(models.Model):
    attached = models.FileField('첨부 파일', upload_to='ducments/%Y/%m/%d')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def get_filename(self):
        return os.path.basename(self.attached.name)

    def __str__(self):
        return self.attached.name


class EduInstitution(models.Model):
    eduInsName = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content


https://jonghoit.tistory.com/27