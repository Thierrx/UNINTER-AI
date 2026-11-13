from django.urls import path
from . import views

urlpatterns = [
    path("perguntar/", views.perguntar_ia, name="perguntar_ia"),
]