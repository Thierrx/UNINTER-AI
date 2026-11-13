from django.urls import path
from . import views

urlpatterns = [
    path("", views.materiais, name="materiais"),
]