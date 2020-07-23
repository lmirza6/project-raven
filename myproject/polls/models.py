import datetime 

from django.db import models

from django.utils import timezone 

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text

    @property
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 
    def __str__(self):
        return self.choice_text 

class User(models.Model):
    date = models.DateTimeField(max_length=64)
    location = models.CharField(max_length=128)
    description = models.TextField()
    def __str__(self):
        return self.user_text 


