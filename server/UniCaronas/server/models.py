from django.db import models
from django.contrib.auth.models import User


class Vehicle(models.Model):
    model = models.CharField(max_length=50, verbose_name="Modelo")
    maker = models.CharField(max_length=50, verbose_name="Fabricante")
    color = models.CharField(max_length=25, verbose_name="Cor")
    board = models.CharField(max_length=10, verbose_name="Placa", unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"

    @property
    def get_board(self):
        return self.board.__str__().upper()

    def __str__(self):
        return f"{self.maker} {self.model} - [{self.board.upper()}]"


class Local(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"

    def __str__(self):
        return self.name


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cronograma"
        verbose_name_plural = "Cronogramas"

    def __str__(self):
        return f"Cronograma de {self.user.get_username()}"


class Trip(models.Model):
    default_price = models.FloatField(verbose_name="Preço padrão", default=4)
    week_days = (
        (1, "Domingo"),
        (2, "Segunda"),
        (3, "Terça"),
        (4, "Quarta"),
        (5, "Quinta"),
        (6, "Sexta"),
        (7, "Sábado"),
    )
    origin = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, related_name='%(class)s_locals_origin', verbose_name="Local de origem")
    destiny = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, related_name='%(class)s_locals_destiny', verbose_name="Local de destino")
    day = models.IntegerField(choices=week_days)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Planejamento diário"
        verbose_name_plural = "Planejamentos diários"

    def __str__(self):
        return self.schedule.__str__() + " - " + self.get_day_display()


class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Motorista")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, verbose_name="Veículo")
    origin = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, verbose_name="Local de origem", related_name='%(class)s_locals_origin')
    destiny = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, verbose_name="Local de destino", related_name='%(class)s_locals_destiny')
    price = models.FloatField(verbose_name="Valor", default=4)

    class Meta:
        verbose_name = "Carona"
        verbose_name_plural = "Caronas"

    def __str__(self):
        return f"Carona de {self.driver.get_username()} [{self.vehicle.__str__()}]"


class Passanger(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Passageiro")
    ride = models.ForeignKey(Ride, on_delete=models.SET_NULL, null=True, verbose_name="Carona")
    type_status = (
        (1, "Não confirmada"),
        (2, "Confirmada"),
        (3, "Em andamento"),
        (4, "Finalizada"),
    )
    status = models.IntegerField(choices=type_status)

    class Meta:
        verbose_name = "Passageiro"
        verbose_name_plural = "Passageiros"

    def __str__(self):
        return f"Carona {self.get_status_display()} - {self.passenger.get_username()}"
