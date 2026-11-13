from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def materiais(request):
    return render(request, "academics/materiais.html")