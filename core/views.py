from django.shortcuts import render
from .models import especialidades
# Create your views here.

def home(request):
    context = {
        'posts': especialidades.objects.all()
    }
    return render(request, "core/home.html", context)

