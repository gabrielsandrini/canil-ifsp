from django.urls import path
from core.views.index import index
from core.views.pessoa import cadastro_pessoa, listagem_pessoa
from core.views.funcionario import cadastro_funcionario
from core.views.veterinario import cadastro_veterinario


urlpatterns = [
    path('', index, name='index'),
    path('cadastro_pessoa/', cadastro_pessoa, name='url_cadastro_pessoa'),
    path('listagem_pessoa/', listagem_pessoa, name='url_listagem_pessoa'),

    path('cadastro_funcionario/', cadastro_funcionario, name='url_cadastro_funcionario'),

    path('cadastro_veterinario/', cadastro_veterinario, name='url_cadastro_veterinario'),
]
