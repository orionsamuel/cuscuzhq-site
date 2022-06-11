from inscricao.models import Inscritos

from rest_framework import serializers

class InscritosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = ['id', 'nome', 'telefone', 'email', 'edicao', 'presente', 'sorteado']