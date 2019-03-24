from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
#funcion de registro manda en automatico el formulario
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta ha sido creada satisfactoriamente porfavor inicia sesion!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render (request, 'pacientes/register.html', {'form': form})
#esto sirve para poder visualizar los archivos html con django
@login_required
def profile(request):
    return render(request, 'pacientes/profile.html')


def consultorios(request):
    return render(request, 'pacientes/consultorios.html')

def especialidades(request):
    return render(request, 'pacientes/espec.html')



