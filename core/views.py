from django.shortcuts import render
from core.forms import FormTeste

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def registro_teste(request):
    form = FormTeste(request.POST or None, request.FILES or None)
    return render(request, 'core/cadastro.html', {'action': 'Registrar', 'model': 'Teste', 'form': form})