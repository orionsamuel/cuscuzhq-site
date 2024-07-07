from inscricao.models import Inscritos, Cospobre, Cosplay, Edicao, NotasCospobre, NotasCosplay

from rest_framework import serializers

class InscritosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = ['id', 'nome', 'telefone', 'email', 'edicao', 'presente1', 'presente2' 'sorteado']

class CospobreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cospobre
        fields = ['id', 'nome', 'telefone', 'email', 'personagem', 'edicao', 'imagem', 'som', 
                'direitoImagem']
                
class CosplaySerializers(serializers.ModelSerializer):
    class Meta:
        model = Cosplay
        fields = ['id', 'nome', 'telefone', 'email', 'personagem', 'edicao', 'imagem', 'som', 
                'direitoImagem']

class EdicaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Edicao
        fields = ['id', 'numero', 'titulo']

class NotasCospobreSerializers(serializers.ModelSerializer):
    class Meta:
        model = NotasCospobre
        fields = ['id', 'nome', 'personagem', 'edicao', 'nota_1', 'nota_2', 'nota_3', 'total_nota']

class NotasCosplaySerializers(serializers.ModelSerializer):
    class Meta:
        model = NotasCosplay
        fields = ['id', 'nome', 'personagem', 'edicao', 'nota_1', 'nota_2', 'nota_3', 'total_nota']
