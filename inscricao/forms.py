from inscricao.models import Inscritos, Cospobre

from django.forms import ModelForm

class InscritosForm(ModelForm):
    class Meta:
        model = Inscritos
        fields = ['nome', 'telefone', 'email']

class CospobreForm(ModelForm):
    class Meta:
        model = Cospobre
        fields = ['nome', 'telefone', 'email', 'personagem', 'imagem', 'som']
