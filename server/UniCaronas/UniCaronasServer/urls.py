from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Rotas para administração
    path('admin/', admin.site.urls),
    # Rotas da aplicação WEB
    path('', include('server.urls')),
    # Rotas para a API
    url('', include('server.paths')),
]
