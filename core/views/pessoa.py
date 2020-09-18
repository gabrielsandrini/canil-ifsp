from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from core.forms import FormPessoa


@login_required()
@transaction.atomic()
def cadastro_pessoa(request):
    form_pessoa = FormPessoa(request.POST or None)

    context = {'forms': [form_pessoa], 'action': 'Registrar', 'model': 'Pessoa' }

    if form_pessoa.is_valid():
        pessoa = form_pessoa.save()
        return redirect('index')

    return render(request, 'core/cadastro_e_atualizacao.html', context)
