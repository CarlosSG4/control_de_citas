from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada por {username}!')
            return redirect('core-home')
    else:
        form = UserRegisterForm()
    return render (request, 'pacientes/register.html', {'form': form})



