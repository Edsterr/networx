from django.db import models

class User(models.Model):
    sid = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    floor = models.IntegerField()
    skills = models.ManyToManyField('Skills')

    def __str__(self):
        return self.name

class Skills(models.Model):
    skillName = models.CharField(max_length=100)
    skillLevel = models.IntegerField()