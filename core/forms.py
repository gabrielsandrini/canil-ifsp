from django.forms import ModelForm
from core.models import Teste

class FormTeste(ModelForm):
    class Meta:
        model = Teste
        fields = '__all__'