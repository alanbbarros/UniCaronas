from idna import unicode
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from server.models import Vehicle, Local, Schedule, Ride
from server.serializers import VehicleSerializer


@permission_classes([IsAuthenticated])
class ApiProfile(APIView):
    @staticmethod
    def get(request):
        vehicles = []
        for vehicle in Vehicle.objects.filter(user=request.user):
            vehicles.append(VehicleSerializer(vehicle).data)

        content = {
            'user': unicode(request.user),
            'vehicles': unicode(vehicles)
        }
        return Response(content)


@permission_classes([IsAuthenticated])
class ApiVehicle(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


@permission_classes([IsAuthenticated])
class ApiLocal(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = VehicleSerializer


@permission_classes([IsAuthenticated])
class ApiSchedule(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = VehicleSerializer


@permission_classes([IsAuthenticated])
class ApiRide(generics.ListCreateAPIView):
    queryset = Ride.objects.all()
    serializer_class = VehicleSerializer
