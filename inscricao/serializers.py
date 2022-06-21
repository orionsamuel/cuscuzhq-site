from inscricao.models import Inscritos, Cospobre

from rest_framework import serializers

class InscritosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = ['id', 'nome', 'telefone', 'email', 'edicao', 'presente', 'sorteado']

class CospobreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cospobre
        fields = ['id', 'nome', 'telefone', 'email', 'edicao', 'imagem', 'som', 
                'nota_1', 'nota_2', 'nota_3']