from django.db import models
from django.contrib.auth.models import User


class ResumeJob(models.Model):
    title = models.CharField(max_length=250)
    period = models.CharField(max_length=150)
    content = models.TextField()
    website = models.CharField(max_length=150, default='')
    company = models.CharField(max_length=150, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ResumeEducation(models.Model):
    name = models.CharField(max_length=350)
    period = models.CharField(max_length=150)
    website = models.CharField(max_length=150, default='')
    specialization = models.CharField(max_length=150, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OtherExperience(models.Model):
    name = models.CharField(max_length=150)
    period = models.CharField(max_length=150)
    website = models.CharField(max_length=150, default='')
    content = models.TextField(default='')
    company = models.CharField(max_length=150, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
