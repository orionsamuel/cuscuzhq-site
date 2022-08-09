from inscricao.models import Inscritos, Cospobre, Cosplay

from rest_framework import serializers

class InscritosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = ['id', 'nome', 'telefone', 'email', 'edicao', 'presente', 'sorteado']

class CospobreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cospobre
        fields = ['id', 'nome', 'telefone', 'email', 'personagem', 'edicao', 'imagem', 'som', 
                'direitoImagem', 'nota_1', 'nota_2', 'nota_3']
                
class CosplaySerializers(serializers.ModelSerializer):
    class Meta:
        model = Cosplay
        fields = ['id', 'nome', 'telefone', 'email', 'personagem', 'edicao', 'imagem', 'som', 
                'direitoImagem', 'nota_1', 'nota_2', 'nota_3']
