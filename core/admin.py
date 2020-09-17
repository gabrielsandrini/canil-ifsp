from django.contrib import admin
from core.models import Pessoa, Veterinario, Funcionario
# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Veterinario)
admin.site.register(Funcionario)