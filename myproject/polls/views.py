from django.shortcuts import render
from django.http import HttpResponse
from .models import Report
from .models import Location


def index(request):
    date = {"dates": Report.objects.all()}
    context = {"reports": Report.objects.all()} 
    return render(request, "polls/index.html", context)

def location(request):
    context = {"locations": Location.objects.all()} 
    return render(request, "polls/location.html", context)

def specLocation(request):
    context = {"locations": Location.objects.all()}
    return render(request, "polls/specLocation.html", context)

def date(request):
    context = {"dates": Report.objects.all()}
    return render(request, "polls/date.html", context)

def event(request):
    context = {"event": Report.objects.all()}
    return render(request, "polls/event.html", context)