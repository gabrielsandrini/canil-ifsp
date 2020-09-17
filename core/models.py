from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=10, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome + ' - ' + self.cpf

    class Meta:
        verbose_name_plural = 'Pessoas'


class Funcionario(models.Model):
    credenciais = models.OneToOneField(User, on_delete=models.CASCADE)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome + ' - ' + self.pessoa.cpf

    class Meta:
        verbose_name_plural = 'Funcionarios'


class Veterinario(models.Model):
    funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)
    crmv = models.CharField(max_length=45)

    def __str__(self):
        return self.funcionario.pessoa.nome + ' - ' + self.crmv

    class Meta:
        verbose_name_plural = 'Veterinarios'

"""
class Cachorro(models.Model):


class Adocao(models.Model):


class Vacina(models.Model):


class Vacinacao(models.Model):


class Consulta(models.Model):


class Medicamento(models.Model):
"""