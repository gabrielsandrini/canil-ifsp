from django.urls import path
from core.views.index import index
from core.views.pessoa import cadastro_pessoa
from core.views.funcionario import cadastro_funcionario
from core.views.veterinario import cadastro_veterinario


urlpatterns = [
    path('', index, name='index'),
    path('cadastro_pessoa/', cadastro_pessoa, name='url_cadastro_pessoa'),
    path('cadastro_funcionario/', cadastro_funcionario, name='url_cadastro_funcionario'),
    path('cadastro_veterinario/', cadastro_veterinario, name='url_cadastro_veterinario'),
]

"""
    path('registro-teste/', views.registro_teste, name='registro_teste'),
    path('atualizacao-teste/<int:id>', views.atualizacao_teste, name='atualizacao_teste'),
    path('listagem-teste/', views.listagem_teste, name='listagem_teste'),
    path('deleta-teste/', views.deleta_teste, name='deleta_teste'),
"""