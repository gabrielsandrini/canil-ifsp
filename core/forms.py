from django.forms import ModelForm
from core.models import Pessoa, Veterinario, Cachorro, Consulta
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class FormPessoa(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class FormVeterinario(ModelForm):
    class Meta:
        model = Veterinario
        fields = ('crmv', )


class FormCachorro(ModelForm):
    class Meta:
        model = Cachorro
        fields = '__all__'


class FormConsultaVeterinario(ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'