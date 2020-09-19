from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from core.models import Adocao
from core.forms import FormAdocao

url_listagem = '/listagem_adocao'


@login_required()
@transaction.atomic()
def cadastro_adocao(request):
    form_adocao = FormAdocao(request.POST or None)

    context = {'forms': [form_adocao], 'action': 'Registrar', 'model': 'Adoção',
               'url_listagem': url_listagem}

    if form_adocao.is_valid():
        form_adocao.save()
        return redirect(url_listagem)

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_adocao(request):
    adocoes = Adocao.objects.all()
    context = {'dados': adocoes}
    return render(request, 'core/adocao/listagem_adocao.html', context)

