from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request): 
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada por {username}!')
            return redirect('core-home')
    else:
        form = UserCreationForm()
    return render(request,'pacientes/register.html', {'form': form})


