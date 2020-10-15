from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from server.models import Vehicle
from ..forms import VehicleForm
from ..utilities import message


@login_required(login_url="/login/")
def page_profile(request):
    """
    Retorna a renderização da página do perfil do usuário
    :param request: Request da página
    :return: Renderização de uma página
    """

    # Retorna a renderização da página
    return render(request, "profile/profile.html", {
        'user': request.user,
        'profile': get_profile_data(request)
    })


@login_required(login_url="/login/")
def get_profile_data(request, json_response: bool = False) -> dict or JsonResponse:
    """
    Retorna as informações para visualização do perfil do usuário
    :param request: Request da página
    :param json_response: Se o retorno da função será em formato JsonResponse
    :return: um dicionário ou um JsonResponse contendo: os veículos
    """

    # Consultando os dados necessários para construção da página
    profile_data = {
        'vehicles': Vehicle.objects.all().filter(user=request.user)
    }
    # Retornando as inforamções de acordo com o parâmetro informado
    return profile_data if not json_response else JsonResponse(profile_data, safe=False)


@login_required(login_url="/login/")
def page_vehicle_create(request):
    """
    Retorna a página de criação de dados caso da requisição ser GET
    Em caso da requisição ser do tipo POST, chama a função para validar e registrar o veículo
    :param request: Request da página
    :return: Renderização de uma página ou redirecionamento
    """

    # Verificando o tipo da requisição
    if request.method == 'POST':
        # Se for do tipo POST, chama a função para validar e registrar os dados
        form = creat_vehicle(request)
        if form is True:
            # Se o retorno da função for True, do tipo booleano, o veículo foi regitrado com sucesso
            return redirect(reverse('web:profile'))
        else:
            # Se não for, ocorreu falha em algum campo então retornado a renderização da página com esse(s) erro(s)
            return render(request, "profile/vehicle/create.html", {
                'form': form,
                'message': message("Alguns campos estão preenchidos erroneamente. Corrija-os e tente novamente.", "Warning", False),
            })
    else:
        # Caso for GET, gera o formulário do veículo
        form = VehicleForm()
        # Retorna a rederização da página
        return render(request, "profile/vehicle/create.html", {
            'form': form
        })


@login_required(login_url="/login/")
def creat_vehicle(request, json_response: bool = False) -> bool or VehicleForm or JsonResponse:
    """
    Valida os dados do formulário de criação de um novo veículo e retorna True caso esteja correto
    e consiga registrar as informações no banco de dados
    Caso alguma informação esteja errada, é retornado a classe do form do veículo com os erros do formulário
    :param request: Request da página
    :param json_response: Se o retorno da função será no formato JsonResponde
    :return: Um booleano em caso de sucesso e um form validado em caso de falha
    """

    # Criando o form para validar os dados
    form = VehicleForm(request.POST)
    # Verifica a validação dos dados
    if form.is_valid():
        # Registra o usuário no banco de dados
        vehicle = form.save(commit=False)
        vehicle.user = request.user
        vehicle.save()
        # Retorna True como resposta
        return True if not json_response else JsonResponse(True)
    else:
        # Retorna os dados validados contendo os erros do formulário
        return form if not json_response else JsonResponse(form)


@login_required(login_url="/login/")
def page_vehicle_update(request, vehicle_id):
    """
    Retorna a página de edição de um determinado veículo caso o método do request seja GET
    Em caso do método do request ser POST, atualiza os dados do veículo e redireciona para a página do usuário
    :param request: Request da página
    :param vehicle_id: ID do veículo a ser modificado
    :return: Renderização de uma página ou redirecionamento
    """

    # Consultando o veículo
    vehicle = Vehicle.objects.get(id=vehicle_id)

    # Verificando o tipo da requisição
    if request.method == 'POST':
        # Caso for do tipo POST, chama a função para atualizar os dados
        form = update_vehicle(request, vehicle)
        # Verificando o retorno da função
        if form is True:
            # Se o retorno da função for True, do tipo booleano, o veículo foi regitrado com sucesso
            return redirect(reverse('web:profile'))
        else:
            # Se não for, ocorreu falha em algum campo então retornado a renderização da página com esse(s) erro(s)
            return render(request, "profile/vehicle/update.html", {
                'vehicle_id': vehicle_id,
                'form': form,
                'message': message("Alguns campos estão preenchidos erroneamente. Corrija-os e tente novamente.", "Warning", False),
            })
    else:
        # Em caso de requisição tipo GET, apenas renderiza a página de de edição
        form = VehicleForm(instance=vehicle)
        return render(request, 'profile/vehicle/update.html', {
            'vehicle_id': vehicle_id,
            'form': form,
        })


@login_required(login_url="/login/")
def update_vehicle(request, vehicle, json_response: bool = False) -> bool or VehicleForm or JsonResponse:
    """
    Atualiza os dados de um veículo
    :param request: Request da página
    :param vehicle: Instância do veículo
    :param json_response: Se o retorno da função será no formato json
    :return: Um booleano em caso de sucesso e um form validado em caso de falha
    """

    # Criando o formulário do objeto
    form = VehicleForm(request.POST, instance=vehicle)
    # Verificando se o formulário está correto
    if form.is_valid():
        # Caso esteja correto, salva as alterações
        form.save()
        # Retorna True como resposta
        return True if not json_response else JsonResponse(True)
    else:
        # Retorna a instância do formulátio com os erros
        return form if not json_response else JsonResponse(form)
