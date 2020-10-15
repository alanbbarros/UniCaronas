from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from server.models import Vehicle
from ..forms import VehicleForm
from ..utilities import message


@login_required(login_url="/login/")
def profile(request):
    return render(request, "profile/profile.html", {
        'user': request.user,
        'vehicles': Vehicle.objects.all().filter(user=request.user)
    })


@login_required(login_url="/login/")
def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            return redirect(reverse('web:profile'))
        else:
            return render(request, "vehicle/create.html", {
                'form': form,
                'message': message("Alguns campos estão preenchidos erroneamente. Corrija-os e tente novamente.", "Warning", False),
            })
    else:
        # Caso for GET, gera o formulário do veículo
        form = VehicleForm()
        # Retorna a rederização da página
        return render(request, "vehicle/create.html", {
            'form': form
        })


@login_required(login_url="/login/")
def vehicle_update(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect(reverse('web:profile'))
        else:
            return render(request, "vehicle/update.html", {
                'vehicle_id': vehicle_id,
                'form': form,
                'message': message("Alguns campos estão preenchidos erroneamente. Corrija-os e tente novamente.", "Warning", False),
            })
    else:
        form = VehicleForm(instance=vehicle)
        return render(request, 'vehicle/update.html', {
            'vehicle_id': vehicle_id,
            'form': form,
        })
