from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def welcome(request):
    """
    Apenas retorna a tela de introdução, uma rápida descrição do sistema
    :param request: Request da página
    :return: HttpResponse
    """

    return render(request, 'welcome.html')


@login_required(login_url="/login/")
def home(request):
    """
    Apenas retorna a tela inicial do sistema, com resumos e informações relacionadas às caronas
    :param request: Request da página
    :return: HttpResponse
    """

    return render(request, 'home.html')
