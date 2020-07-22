from django.shortcuts import render
from django.http import HttpResponse
from .models import Question 


def index(request):
    context = {"questions": Question.objects.all()} 
    return render(request, "polls/index.html", context)
