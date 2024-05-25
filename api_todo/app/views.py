from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from app.models import Produto, Relacao, Nivel, Usuario
from rest_framework.exceptions import NotFound
from app.serializers import ProdutoSerializers, RelacaoSerializers
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def relacao (request):
    if request.method == "POST":
        serializer = RelacaoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
    elif request.method == "GET":
        relacao = Relacao.objects.all()
        serializer = RelacaoSerializers(relacao,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def relacao_id (request,id):
    try:
        relacao = Relacao.objects.get(id=id)  # Corrigindo o nome da variável
    except Relacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = RelacaoSerializers(relacao)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = RelacaoSerializers(instance=relacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        relacao.delete()  # Corrigindo o nome da variável
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
