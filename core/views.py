from django.shortcuts import render, HttpResponse

html_base = """
<h1>Control de Citas</h1>
<ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/about/">Acerca de</a></li>

"""
# Create your views here.

def home(request):
    return render(request, "core/home.html")

