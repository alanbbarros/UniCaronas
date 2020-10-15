from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url
from .api import profile

app_name = "api"
urlpatterns = [
    url('api/get-token/', obtain_auth_token, name='get_token'),
    url('api/profile/$', profile.ApiProfile.as_view(), name='profile'),
    url('api/vehicle/$', profile.ApiVehicle.as_view(), name='profile'),
    url('api/local/$', profile.ApiLocal.as_view(), name='profile'),
    url('api/schedule/$', profile.ApiSchedule.as_view(), name='profile'),
    url('api/ride/$', profile.ApiRide.as_view(), name='profile'),
]
