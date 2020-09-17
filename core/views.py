from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.forms import FormTeste
from core.models import Teste

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def registro_teste(request):
    form = FormTeste(request.POST or None, request.FILES or None)
    return render(request, 'core/cadastro_e_atualizacao.html', {'action': 'Registrar', 'model': 'Teste', 'form': form})


def atualizacao_teste(request):
    form = FormTeste(request.POST or None, request.FILES or None)
    return render(request, 'core/cadastro_e_atualizacao.html', {'action': 'Atualizar', 'model': 'Teste', 'form': form})


def listagem_teste(request):
    testes = Teste.objects.all()
    return render(request, 'core/teste/listagem_teste.html', {'model': 'Teste', 'teste': testes})

def deleta_teste(request):
    return render(request)