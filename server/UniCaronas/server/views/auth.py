from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as djanngo_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from ..utilities import message


def page_login(request):
    """
    Realiza a renderização da página de login caso a requisição for do tipo GET
    E tenta realizar a autenticação caso a requisição seja POST
    :param request: Request da página
    :return: render or redirect
    """

    # Verificando o tipo da requisição
    if request.method == 'POST':
        # Caso for POST, realiza a tentativa de login
        if login(request):
            # Caso o login seja efetuado com sucesso, redireciona para a Home do sistema
            return redirect(reverse('web:home'))
        else:
            # Caso o login não seja efetuado com sucesso, renderiza a página de login para uma nova tentativa
            return render(request, 'auth/login.html', {
                'message': message("Usuário ou senha incorretos.", 'warning'),
            })
    else:
        # Caso seja GET, retorna a página de login para o usuário
        return render(request, 'auth/login.html')


def login(request, json_response: bool = False) -> bool or JsonResponse:
    """
    Tenta realizar a autenticação do usuário e retorna True ou False caso consiga ou não
    Informado o parâmetro json_response como True, é retornado em formato JsonResponse
    :param request: Request da página
    :param json_response: Se o retorno é tipo JsonResponse
    :return: bool ou JsonResponse
    """

    # Primeiro consulta os dados do usuário
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Testa as credênciais
    user = authenticate(username=username, password=password)

    if user:
        # Caso as credênciais estjam corretas, realiza o login do usuário
        django_login(request, user)
        return True if not json_response else JsonResponse(True, safe=False)
    else:
        return False if not json_response else JsonResponse(False, safe=False)


@login_required(login_url="/login/")
def page_logout(request):
    """
    Realiza o encerramento da sessão do usuário
    :param request: Request da página
    :return: Redirect
    """

    # Verificando o tipo da requisição
    if request.method == 'POST':
        # Se o tipo da requisição for POST, o logout é aceito
        logout(request)
        return redirect(reverse('web:login'))
    else:
        # Se não, foi inserido manualmente a rota. Logo a ação é interrompida
        return redirect(reverse('web:home'))


@login_required(login_url="/login/")
def logout(request, json_response: bool = False):
    """
    Realiza o encerramento da sessão
    :param request: Request da página
    :param json_response: Se o retorno é tipo JsonResponse
    :return: bool ou JsonResponse
    """

    djanngo_logout(request)
    return True if not json_response else JsonResponse(True, safe=False)
