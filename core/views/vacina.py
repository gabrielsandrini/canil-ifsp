from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.forms import FormVacina
from core.models import Vacina


@login_required()
def cadastro_vacina(request):
    form_vacina = FormVacina(request.POST or None)
    context = {'forms': [form_vacina], 'action': 'Registrar', 'model': 'Vacina',
               'url_listagem': '/listagem_vacina'}

    if form_vacina.is_valid():
        form_vacina.save()
        return redirect('/listagem_vacina')

    return render(request, 'core/cadastro_e_atualizacao.html', context)


@login_required()
def listagem_vacina(request):
    vacinas = Vacina.objects.all()
    context = {'dados': vacinas}
    return render(request, 'core/vacina/listagem_vacina.html', context)

