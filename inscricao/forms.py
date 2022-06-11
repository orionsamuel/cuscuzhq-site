from inscricao.models import Inscritos

from django.forms import ModelForm

class InscritosForm(ModelForm):
    class Meta:
        model = Inscritos
        fields = ['nome', 'telefone', 'email']
