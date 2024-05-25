from app.models import Produto, Relacao, Nivel, Usuario
from rest_framework import serializers

class ProdutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'valor', 'limite_cri', 'limite_adu ', 'limite_beb']


class RelacaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Relacao
        fields = ['id','inicio','fim', 'produto', 'quant_cri', 'usuario', 'nivel' ]

