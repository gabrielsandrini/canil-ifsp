from django.urls import path
from core.views.index import index
from core.views.pessoa import cadastro_pessoa, listagem_pessoa
from core.views.funcionario import cadastro_funcionario, listagem_funcionario
from core.views.veterinario import cadastro_veterinario, listagem_veterinario
from core.views.cachorro import cadastro_cachorro, listagem_cachorro
from core.views.adocao import cadastro_adocao, listagem_adocao

urlpatterns = [
    # Home/Index
    path('', index, name='index'),

    # Pessoa
    path('cadastro_pessoa/', cadastro_pessoa, name='url_cadastro_pessoa'),
    path('listagem_pessoa/', listagem_pessoa, name='url_listagem_pessoa'),

    # Funcionário
    path('cadastro_funcionario/', cadastro_funcionario, name='url_cadastro_funcionario'),
    path('listagem_funcionario/', listagem_funcionario, name='url_listagem_funcionario'),

    # Veterinário
    path('cadastro_veterinario/', cadastro_veterinario, name='url_cadastro_veterinario'),
    path('listagem_veterinario/', listagem_veterinario, name='url_listagem_veterinario'),

    # Cachorro
    path('cadastro_cachorro/', cadastro_cachorro, name='url_cadastro_cachorro'),
    path('listagem_cachorro/', listagem_cachorro, name='url_listagem_cachorro'),

    # Adoção
    path('cadastro_adocao/', cadastro_adocao, name='url_cadastro_adocao'),
    path('listagem_adocao/', listagem_adocao, name='url_listagem_adocao'),
]
