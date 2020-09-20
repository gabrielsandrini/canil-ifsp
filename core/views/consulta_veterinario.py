from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from core.forms import FormConsultaVeterinario
from core.models import Consulta

url_listagem = '/listagem_consulta'
url_cadastro = '/cadastro_consulta'
model = 'Consulta'


@login_required()
@transaction.atomic()
def cadastro_consulta_veterinario(request):
    form_consulta_veterinario = FormConsultaVeterinario(request.POST or None)

    context = {'forms': [form_consulta_veterinario],
               'form_action': 'Registrar',
               'title_page': 'Registro',
               'btn_action': 'Listagem',
               'model': model,
               'url': url_listagem}

    if form_consulta_veterinario.is_valid():
        form_consulta_veterinario.save()
        return redirect(url_listagem)

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_consulta_veterinario(request):
    consultas = Consulta.objects.all()

    context = {'dados': consultas,
               'title_page': 'Listagem',
               'btn_action': 'Registrar',
               'model': model,
               'url': url_cadastro
               }

    return render(request, 'core/consulta/listagem_consulta.html', context)

