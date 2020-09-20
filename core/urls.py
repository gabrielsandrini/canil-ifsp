from django.urls import path
from core.views.index import index
from core.views.pessoa import cadastro_pessoa, listagem_pessoa, atualiza_pessoa, deleta_pessoa
from core.views.funcionario import cadastro_funcionario, listagem_funcionario
from core.views.veterinario import cadastro_veterinario, listagem_veterinario
from core.views.cachorro import (cadastro_cachorro, listagem_cachorro, atualiza_cachorro, deleta_cachorro,
                                 rastrear_cachorro)
from core.views.adocao import cadastro_adocao, listagem_adocao, atualiza_adocao, deleta_adocao
from core.views.consulta_veterinario import cadastro_consulta_veterinario, listagem_consulta_veterinario
from core.views.vacina import cadastro_vacina, listagem_vacina
from core.views.vacinacao import cadastro_vacinacao, listagem_vacinacao

urlpatterns = [
    # Home/Index
    path('', index, name='index'),

    # Pessoa
    path('cadastro_pessoa/', cadastro_pessoa, name='url_cadastro_pessoa'),
    path('listagem_pessoa/', listagem_pessoa, name='url_listagem_pessoa'),
    path('atualiza_pessoa/<int:pessoa_id>', atualiza_pessoa, name='url_atualiza_pessoa'),
    path('deleta_pessoa/<int:pessoa_id>', deleta_pessoa, name='url_deleta_pessoa'),

    # Funcionário
    path('cadastro_funcionario/', cadastro_funcionario, name='url_cadastro_funcionario'),
    path('listagem_funcionario/', listagem_funcionario, name='url_listagem_funcionario'),

    # Veterinário
    path('cadastro_veterinario/', cadastro_veterinario, name='url_cadastro_veterinario'),
    path('listagem_veterinario/', listagem_veterinario, name='url_listagem_veterinario'),

    # Cachorro
    path('cadastro_cachorro/', cadastro_cachorro, name='url_cadastro_cachorro'),
    path('listagem_cachorro/', listagem_cachorro, name='url_listagem_cachorro'),
    path('atualiza_cachorro/<int:cachorro_id>', atualiza_cachorro, name='url_atualiza_cachorro'),
    path('deleta_cachorro/<int:cachorro_id>', deleta_cachorro, name='url_deleta_cachorro'),
    path('rastreamento/', rastrear_cachorro, name='url_rastrear_cachorro'),

    # Adoção
    path('cadastro_adocao/', cadastro_adocao, name='url_cadastro_adocao'),
    path('listagem_adocao/', listagem_adocao, name='url_listagem_adocao'),
    path('atualiza_adocao/<int:adocao_id>', atualiza_adocao, name='url_atualiza_adocao'),
    path('deleta_adocao/<int:adocao_id>', deleta_adocao, name='url_deleta_adocao'),

    # Consulta
    path('cadastro_consulta/', cadastro_consulta_veterinario, name='url_cadastro_consulta'),
    path('listagem_consulta/', listagem_consulta_veterinario, name='url_listagem_consulta'),

    # Vacina
    path('cadastro_vacina/', cadastro_vacina, name='url_cadastro_vacina'),
    path('listagem_vacina/', listagem_vacina, name='url_listagem_vacina'),

    # Vacinacao
    path('cadastro_vacinacao/', cadastro_vacinacao, name='url_cadastro_vacinacao'),
    path('listagem_vacinacao/', listagem_vacinacao, name='url_listagem_vacinacao'),
]
