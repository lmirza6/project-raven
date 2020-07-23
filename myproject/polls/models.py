import datetime
from django.db import models
from django.utils import timezone
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text

class Report(models.Model):
    date = models.DateTimeField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return f"{self.description[:25]}..."

class Location(models.Model):
    name = models.CharField(max_length=100)
    report = models.ForeignKey(Report, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

