from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_pessoa/', views.cadastro_pessoa, name='url_cadastro_pessoa'),
    path('cadastro_funcionario/', views.cadastro_funcionario, name='url_cadastro_funcionario'),
    path('cadastro_veterinario/', views.cadastro_veterinario, name='url_cadastro_veterinario'),
    path('registro-teste/', views.registro_teste, name='registro_teste'),
    path('atualizacao-teste/<int:id>', views.atualizacao_teste, name='atualizacao_teste'),
    path('listagem-teste/', views.listagem_teste, name='listagem_teste'),
    path('deleta-teste/', views.deleta_teste, name='deleta_teste'),
]