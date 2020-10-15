from django.contrib import admin

from .models import Vehicle, Local, Schedule, Trip, Ride, Passanger

admin.site.register(Vehicle)
admin.site.register(Local)
admin.site.register(Schedule)
admin.site.register(Trip)
admin.site.register(Ride)
admin.site.register(Passanger)
