from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from core.forms import FormPessoa, FormVeterinario, UserCreateForm
from core.models import Funcionario, Veterinario

url_listagem = '/listagem_veterinario'


@login_required()
@transaction.atomic()
def cadastro_veterinario(request):
    form_pessoa = FormPessoa(request.POST or None)
    form_credenciais = UserCreateForm(request.POST or None)
    form_veterinario = FormVeterinario(request.POST or None)

    context = {'forms': [form_pessoa, form_credenciais, form_veterinario], 'action': 'Registrar',
               'model': 'Veterinário', 'url_listagem': url_listagem}

    if form_pessoa.is_valid() and form_credenciais.is_valid() and form_veterinario.is_valid():

        pessoa = form_pessoa.save()

        credenciais = form_credenciais.save()

        funcionario = Funcionario(pessoa=pessoa, credenciais=credenciais)
        funcionario.save()

        veterinario = form_veterinario.save(False)
        veterinario.funcionario = funcionario
        veterinario.save()

        return redirect(url_listagem)

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_veterinario(request):
    veterinarios = Veterinario.objects.all()
    context = {'dados': veterinarios}
    return render(request, 'core/veterinario/listagem_veterinario.html', context)
