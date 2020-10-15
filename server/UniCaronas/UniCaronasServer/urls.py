from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Rotas para administração
    path('admin/', admin.site.urls),
    # Rotas da aplicação WEB (app)
    path('', include('server.urls')),
]
