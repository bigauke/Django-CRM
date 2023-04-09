from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
    # chegar se está logado
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # autenticado
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Você está logado")
            return redirect('home')
        else:
            messages.success(request, "Houve um erro ao logar, por favor tente novamente.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Você foi desconectado!")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html' , {})