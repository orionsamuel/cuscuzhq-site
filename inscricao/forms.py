from inscricao.models import Inscritos, Cospobre, Cosplay, Artistas

from django.forms import ModelForm

class InscritosForm(ModelForm):
    class Meta:
        model = Inscritos
        fields = ['nome', 'telefone', 'email']

class CospobreForm(ModelForm):
    class Meta:
        model = Cospobre
        fields = ['nome', 'telefone', 'email', 'personagem', 'imagem', 'som', 'direitoImagem']
        
class CosplayForm(ModelForm):
    class Meta:
        model = Cosplay
        fields = ['nome', 'telefone', 'email', 'personagem', 'imagem', 'som', 'direitoImagem']

class ArtistaForm(ModelForm):
    class Meta:
        model = Artistas
        fields = ['nome', 'telefone', 'email', 'experiencia', 'obrasPublicadas', 'obrasFuturas',
                'instagram', 'facebook', 'devianart', 'blog', 'outraRedeSocial', 'arquivos']
