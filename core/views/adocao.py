from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction


@login_required()
@transaction.atomic()
def cadastro_adocao(request):

    context = {'forms': [], 'action': 'Registrar', 'model': 'Adoção',
               'url_listagem': '/listagem_adocao'}

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_adocao(request):
    return render(request, 'core/adocao/listagem_adocao.html')

