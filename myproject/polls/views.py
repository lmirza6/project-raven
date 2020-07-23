from django.shortcuts import render
from django.http import HttpResponse
from .models import Report



def index(request):
    context = {"reports": Report.objects.all()} 
    return render(request, "polls/index.html", context)
