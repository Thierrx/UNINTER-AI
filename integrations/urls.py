from django.urls import path
from . import views

urlpatterns = [
    path(
        "abrir/",
        views.abrir_navegador,
        name="abrir_navegador"
    ),
]