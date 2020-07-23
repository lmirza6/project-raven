from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('location/', views.location, name = "location"),
    path('specLocation/', views.specLocation, name = "specLocation"),
    path('event/', views.event, name = "event"),
    path('date/', views.date, name = "date"),
]

# urlpatterns = [
#     path('', views.location, name = "location"),
# ]