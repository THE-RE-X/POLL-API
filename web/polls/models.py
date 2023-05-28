from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=250)
    option1 = models.IntegerField(default=0)
    option2 = models.IntegerField(default=0)
    option3 = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=255)
