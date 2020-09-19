from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from core.forms import FormPessoa
from core.models import Pessoa

@login_required()
@transaction.atomic()
def cadastro_pessoa(request):
    form_pessoa = FormPessoa(request.POST or None)

    context = {'forms': [form_pessoa], 'action': 'Registrar', 'model': 'Pessoa', 'url_listagem': '/listagem_pessoa' }

    if form_pessoa.is_valid():
        form_pessoa.save()
        return redirect('index')

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_pessoa(request):
    pessoas = Pessoa.objects.all()
    context = {'dados': pessoas}
    return render(request, 'core/pessoa/listagem_pessoa.html', context)
