from django.contrib import admin
from django.urls import path
from .views import auth, views, profile

app_name = "web"
urlpatterns = [
    # Rotas para administração
    path('admin/', admin.site.urls),
    # Página de apresentação do sistema
    path('', views.welcome, name="welcome"),
    # Rotas para autenticação
    path('login/', auth.login, name="login"),
    path('logout/', auth.logout, name="logout"),
    # Rotas em que apenas os usuários autenticados possuem acesso
    path('home/', views.home, name="home"),
    path('profile/', profile.profile, name="profile"),
    path('vehicle/create/', profile.vehicle_create, name="vehicle-create"),
    path('vehicle/<vehicle_id>/update/', profile.vehicle_update, name="vehicle-update"),
]
