from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from core.forms import FormCachorro
from core.models import Cachorro


@login_required()
@transaction.atomic()
def cadastro_cachorro(request):
    form_cachorro = FormCachorro(request.POST or None)

    context = {'forms': [form_cachorro], 'action': 'Registrar', 'model': 'Cachorro'}

    if form_cachorro.is_valid():
        form_cachorro.save()
        return redirect('index')

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_cachorro(request):
    cachorros = Cachorro.objects.all()
    context = {'dados': cachorros}
    return render(request, 'core/teste/listagem_teste.html', context)
