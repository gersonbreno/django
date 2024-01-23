from django.urls import path
from . views import *
urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('cria-lista/', CriaListaView.as_view(), name='crialista'),
    path('Excluir-lista/<int:pk>/', DelatarListaView.as_view(), name='excluir'),
    path('concluir-lista/<int:pk>/',  ConcluirView.as_view(), name='concluir'),
    path('atualizar-lista/<int:pk>/',  AtualizaListaView.as_view(), name='atualizar'),
]
