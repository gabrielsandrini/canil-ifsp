from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from core.forms import FormPessoa, UserCreateForm
from core.models import Funcionario


@login_required()
@transaction.atomic()
def cadastro_funcionario(request):
    form_pessoa = FormPessoa(request.POST or None)
    form_credenciais = UserCreateForm(request.POST or None)

    context = {'forms': [form_pessoa, form_credenciais], 'action': 'Registrar', 'model': 'Funcionário' }

    if form_pessoa.is_valid() and form_credenciais.is_valid():
        pessoa = form_pessoa.save()
        credenciais = form_credenciais.save()
        funcionario = Funcionario(pessoa=pessoa, credenciais=credenciais)
        funcionario.save()
        return redirect('index')

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_funcionario(request):
    funcionarios = Funcionario.objects.all()
    context = {'dados': funcionarios}
    return render(request, 'core/teste/listagem_teste.html', context)
