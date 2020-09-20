from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.forms import FormVacina
from core.models import Vacina

url_listagem = '/listagem_vacina'
url_cadastro = '/cadastro_vacina'
model = 'Vacina'


@login_required()
def cadastro_vacina(request):
    form_vacina = FormVacina(request.POST or None)

    context = {'forms': [form_vacina],
               'form_action': 'Registrar',
               'title_page': 'Registro',
               'btn_action': 'Listagem',
               'model': model,
               'url': url_listagem}

    if form_vacina.is_valid():
        form_vacina.save()
        return redirect(url_listagem)

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_vacina(request):
    vacinas = Vacina.objects.all()
    context = {'dados': vacinas,
               'title_page': 'Listagem',
               'btn_action': 'Registrar',
               'model': model,
               'url': url_cadastro
               }
    return render(request, 'core/vacina/listagem_vacina.html', context)

