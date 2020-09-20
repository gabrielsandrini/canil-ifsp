from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from core.forms import FormCachorro
from core.models import Cachorro

url_listagem = '/listagem_cachorro'


@login_required()
@transaction.atomic()
def cadastro_cachorro(request):
    form_cachorro = FormCachorro(request.POST or None)

    context = {'forms': [form_cachorro], 'action': 'Registrar', 'model': 'Cachorro',
               'url_listagem': url_listagem}

    if form_cachorro.is_valid():
        form_cachorro.save()
        return redirect(url_listagem)

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_cachorro(request):
    cachorros = Cachorro.objects.all()
    context = {'dados': cachorros}
    return render(request, 'core/cachorro/listagem_cachorro.html', context)


@login_required()
def atualiza_cachorro(request, cachorro_id):
    cachorro = Cachorro.objects.get(id=cachorro_id)
    form_cachorro = FormCachorro(request.POST or None, instance=cachorro)

    context = {'forms': [form_cachorro], 'action': 'Atualizar', 'model': 'Cachorro',
               'url_listagem': url_listagem}

    if form_cachorro.is_valid():
        form_cachorro.save()
        return redirect(url_listagem)

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def deleta_cachorro(request, cachorro_id):
    cachorro = Cachorro.objects.get(id=cachorro_id)
    cachorro.delete()
    return redirect(url_listagem)
