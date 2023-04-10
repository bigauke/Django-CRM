from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record



def home(request):
    records = Record.objects.all()

    # checar se está logado
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
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "Você foi desconectado!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Você se registrou com sucesso, Seja bem vindo!")
            return redirect('home')
    else:
        form = SignUpForm(request.POST)
        return render(request, 'register.html' , {'form': form})
    return render(request, 'register.html' , {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Procurar por Records  
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html' , {'customer_record': customer_record})
    else:
        messages.success(request, "Você deve estar logado para visuzalizar esta página!")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Cadastro deletado com sucesso!")
        return redirect('home')
    else:
         messages.success(request, "Você deve estar logado para deletar isso!")
         return redirect('home')
    
def add_record(request):
    
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Dados adicionado com sucesso!")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "Você deve estar logado...")
        return  redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "O dados foram atualizados!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "Você deve estar logado")
        return redirect('home')





    
