from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from core.forms import FormConsultaVeterinario
from core.models import Consulta


@login_required()
@transaction.atomic()
def cadastro_consulta_veterinario(request):
    form_consulta_veterinario = FormConsultaVeterinario(request.POST or None)
    context = {'forms': [form_consulta_veterinario], 'action': 'Registrar', 'model': 'Consulta',
               'url_listagem': '/listagem_consulta'}
    if form_consulta_veterinario.is_valid():
        form_consulta_veterinario.save()
        return redirect('index')

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_consulta_veterinario(request):
    consultas = Consulta.objects.all()
    context = {'dados': consultas}
    return render(request, 'core/consulta/listagem_consulta.html', context)

