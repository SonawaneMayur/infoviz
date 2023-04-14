from django.urls import path

from .views import graph

urlpatterns = [
    path("", graph, name="graph"),
]
