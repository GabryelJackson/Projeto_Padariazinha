from django.urls import path
from app_padariazinha import views
urlpatterns = [
    #rota, view responsável, nome de referência
    path('', views.home, name='home'),
    path('usuarios/', views.produto, name='listagem_produtos')
]