from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.forms import FormPessoa, FormVeterinario, UserCreateForm
from core.models import Funcionario
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'core/index.html')
    return redirect('login')


@login_required()
def registro_teste(request):
    form = FormPessoa(request.POST or None, request.FILES or None)
    return render(request, 'core/cadastro_e_atualizacao.html', {'action': 'Registrar', 'model': 'Teste', 'form': form})


@login_required()
def atualizacao_teste(request):
    form = FormPessoa(request.POST or None, request.FILES or None)
    return render(request, 'core/cadastro_e_atualizacao.html', {'action': 'Atualizar', 'model': 'Teste', 'form': form})


@login_required()
def listagem_teste(request):
    return render(request, 'core/teste/listagem_teste.html', {'model': 'Teste', 'teste': []})


@login_required()
def deleta_teste(request):
    return render(request)


@login_required()
def cadastro_funcionario(request):
    form_pessoa = FormPessoa(request.POST or None)
    form_credenciais = UserCreateForm(request.POST or None)

    context = {'forms': [form_pessoa, form_credenciais], 'action': 'Registrar', 'model': 'Funcionário' }

    if form_pessoa.is_valid() and form_credenciais.is_valid():
        pessoa = form_pessoa.save()
        credenciais = form_credenciais.save()
        funcionario = Funcionario(pessoa=pessoa, credenciais=credenciais)
        funcionario.save()
        return redirect('index')

    return render(request, 'core/cadastro_e_atualizacao.html', context)
