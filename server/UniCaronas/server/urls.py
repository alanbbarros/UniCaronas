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
    path('login/', auth.page_login, name="login"),
    path('logout/', auth.page_logout, name="logout"),
    # Rotas em que apenas os usuários autenticados possuem acesso
    path('home/', views.home, name="home"),
    path('profile/', profile.page_profile, name="profile"),
    path('vehicle/create/', profile.page_vehicle_create, name="vehicle-create"),
    path('vehicle/<vehicle_id>/update/', profile.page_vehicle_update, name="vehicle-update"),
]
