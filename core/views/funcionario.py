from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from core.forms import FormPessoa, UserCreateForm
from core.models import Funcionario

url_listagem = '/listagem_funcionario'
url_cadastro = '/cadastro_funcionario'
model = 'Funcionário'


@login_required()
@transaction.atomic()
def cadastro_funcionario(request):
    form_pessoa = FormPessoa(request.POST or None)
    form_credenciais = UserCreateForm(request.POST or None)

    context = {'forms': [form_pessoa, form_credenciais],
               'form_action': 'Registrar',
               'title_page': 'Registro',
               'btn_action': 'Listagem',
               'model': model,
               'url': url_listagem}

    if form_pessoa.is_valid() and form_credenciais.is_valid():
        pessoa = form_pessoa.save()
        credenciais = form_credenciais.save()
        funcionario = Funcionario(pessoa=pessoa, credenciais=credenciais)
        funcionario.save()
        return redirect(url_listagem)

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_funcionario(request):
    funcionarios = Funcionario.objects.all()

    context = {'dados': funcionarios,
               'title_page': 'Listagem',
               'btn_action': 'Registrar',
               'model': model,
               'url': url_cadastro
               }

    return render(request, 'core/funcionario/listagem_funcionario.html', context)

