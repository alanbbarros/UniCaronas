from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as djanngo_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from ..utilities import message


def login(request):
    if request.method == 'POST':
        # Primeiro consulta os dados do usuário
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Testa as credênciais
        user = authenticate(username=username, password=password)

        if user:
            django_login(request, user)
            return redirect(reverse('web:home'))
        else:
            return render(request, 'auth/login.html', {
                'message': message("Usuário ou senha incorretos.", 'warning'),
            })
    else:
        # Caso seja GET, retorna a página de login para o usuário
        return render(request, 'auth/login.html')


@login_required(login_url="/login/")
def logout(request):
    if request.method == 'POST':
        djanngo_logout(request)
        return redirect(reverse('web:login'))
    else:
        return redirect(reverse('web:home'))
