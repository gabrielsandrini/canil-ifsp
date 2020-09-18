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
    pessoa = models.OneToOneField(Pessoa, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.pessoa.nome + ' - ' + self.pessoa.cpf

    class Meta:
        verbose_name_plural = 'Funcionarios'


class Veterinario(models.Model):
    funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)
    crmv = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.funcionario.pessoa.nome + ' - ' + self.funcionario.pessoa.cpf

    class Meta:
        verbose_name_plural = 'Veterinarios'


class Cachorro(models.Model):
    nome = models.CharField(max_length=45)
    raca = models.CharField(max_length=45, blank=True, null=True)
    cor = models.CharField(max_length=80)
    porte = models.CharField(max_length=45)
    data_nascimento = models.DateField(blank=True, null=True)
    pedigree = models.CharField(max_length=45, unique=True)
    caracteristicas_extras = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome + self.raca + ' - ' + self.pedigree

    class Meta:
        verbose_name_plural = 'Cachorros'


class Adocao(models.Model):
    guardiao = models.ForeignKey(Cachorro, on_delete=models.SET_NULL, null=True)
    cachorro = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    data = models.DateField()

    def __str__(self):
        return self.guardiao + ' - ' + self.cachorro

    class Meta:
        verbose_name_plural = 'Adocoes'


class Vacina(models.Model):
    descricao = models.CharField(max_length=60)

    def __str__(self):
        return self.descricao + ' - ' + self.id

    class Meta:
        verbose_name_plural = 'Vacinas'


class Vacinacao(models.Model):
    vacina = models.ForeignKey(Vacina, on_delete=models.SET_NULL, null=True)
    cachorro = models.ForeignKey(Cachorro, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return self.cachorro + ' - ' + self.vacina

    class Meta:
        verbose_name_plural = 'Vacinacoes'


class Medicacao(models.Model):
    nome_medicamento = models.CharField(max_length=100)
    posologia = models.CharField(max_length=100)

    def __str__(self):
        return self.cachorro + ' - ' + self.medicamento

    class Meta:
        verbose_name_plural = 'Medicacoes'


class Consulta(models.Model):
    veterinario = models.ForeignKey(Veterinario, on_delete=models.DO_NOTHING)
    cachorro = models.ForeignKey(Cachorro, on_delete=models.CASCADE)
    data = models.DateField()
    medicacao = models.ManyToManyField(Medicacao, blank=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.data + ' - ' + self.cachorro

    class Meta:
        verbose_name_plural = 'Consultas'

