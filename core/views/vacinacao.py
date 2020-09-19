from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.forms import FormVacinacao
from core.models import Vacinacao


@login_required()
def cadastro_vacinacao(request):
    form_vacinacao = FormVacinacao(request.POST or None)
    context = {'forms': [form_vacinacao], 'action': 'Registrar', 'model': 'Vacinações',
               'url_listagem': '/listagem_vacinacao'}

    if form_vacinacao.is_valid():
        form_vacinacao.save()
        return redirect('/listagem_vacinacao')

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_vacinacao(request):
    vacinacoes = Vacinacao.objects.all()
    context = {'dados': vacinacoes}
    return render(request, 'core/vacinacao/listagem_vacinacao.html', context)

