# Generated by Django 3.1.2 on 2020-10-15 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locais',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cronograma',
                'verbose_name_plural': 'Cronogramas',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Modelo')),
                ('maker', models.CharField(max_length=50, verbose_name='Fabricante')),
                ('color', models.CharField(max_length=25, verbose_name='Cor')),
                ('board', models.CharField(max_length=10, unique=True, verbose_name='Placa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Veículo',
                'verbose_name_plural': 'Veículos',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_price', models.FloatField(default=4, verbose_name='Preço padrão')),
                ('day', models.IntegerField(choices=[(1, 'Domingo'), (2, 'Segunda'), (3, 'Terça'), (4, 'Quarta'), (5, 'Quinta'), (6, 'Sexta'), (7, 'Sábado')])),
                ('destiny', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trip_locals_destiny', to='server.local', verbose_name='Local de destino')),
                ('origin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trip_locals_origin', to='server.local', verbose_name='Local de origem')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.schedule')),
            ],
            options={
                'verbose_name': 'Planejamento diário',
                'verbose_name_plural': 'Planejamentos diários',
            },
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=4, verbose_name='Valor')),
                ('destiny', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ride_locals_destiny', to='server.local', verbose_name='Local de destino')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Motorista')),
                ('origin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ride_locals_origin', to='server.local', verbose_name='Local de origem')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.vehicle', verbose_name='Veículo')),
            ],
            options={
                'verbose_name': 'Carona',
                'verbose_name_plural': 'Caronas',
            },
        ),
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Não confirmada'), (2, 'Confirmada'), (3, 'Em andamento'), (4, 'Finalizada')])),
                ('passenger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Passageiro')),
                ('ride', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.ride', verbose_name='Carona')),
            ],
            options={
                'verbose_name': 'Passageiro',
                'verbose_name_plural': 'Passageiros',
            },
        ),
    ]
