from django.shortcuts import render
from core.models import Cachorro


def index(request):
    if request.user.is_authenticated:
        return render(request, 'core/index_autenticado.html')
    cachorros = Cachorro.objects.all()
    return render(request, 'core/index.html', {'cachorros': cachorros})
