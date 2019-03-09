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

def about(request):
    return HttpResponse(html_base + """
    <h2>Acerca de</h2>
    <p> Somos una empresa dedicada a el facil manejo de citas</p>
    """)