from inscricao.models import Edicao, Inscritos, Cospobre, Artistas
from inscricao.forms import InscritosForm, CospobreForm, ArtistaForm
from inscricao.serializers import InscritosSerializers, CospobreSerializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def Inscricao(request):
    context = {}
    if request.method == 'POST':
        form = InscritosForm(request.POST or None)
        serializer = InscritosSerializers(data=request.POST)
        if serializer.is_valid():
            serializer.save(edicao=Edicao.objects.last())
            redirect('inscricao.html')
            context['success'] = True
    form = InscritosForm()
    context['form'] = form
    context['edition'] = Edicao.objects.last().numero
    return render(request, 'inscricao.html', context)

def InscricaoCospobre(request): 
    context = {}
    if request.method == 'POST':
        form = CospobreForm(request.POST or None, request.FILES)
        serializer = CospobreSerializers(data=request.POST)
        if serializer.is_valid():
            if 'som' in request.FILES:
                serializer.save(edicao=Edicao.objects.last(), imagem=request.FILES['imagem'], som=request.FILES['som'])
            else:
                serializer.save(edicao=Edicao.objects.last(), imagem=request.FILES['imagem'])
            redirect('cospobre.html')
            context['success'] = True
    form = CospobreForm()
    context['form'] = form
    context['edition'] = Edicao.objects.last().numero
    return render(request, 'cospobre.html', context)

def InscricaoArtista(request): 
    context = {}
    if request.method == 'POST':
        form = ArtistaForm(request.POST or None, request.FILES)
        if form.is_valid():
            artista = form.save(commit=False)
            artista.edicao = edicao=Edicao.objects.last()
            artista.save()
            redirect('artistas.html')
            context['success'] = True
    form = ArtistaForm()
    context['form'] = form
    context['edition'] = Edicao.objects.last().numero
    return render(request, 'artistas.html', context)

class BuscarParticipante(APIView):
    def get(self, request, edicao, busca):
        inscritos = Inscritos.objects.filter(nome__icontains=busca, edicao__numero=edicao)
        serializer = InscritosSerializers(inscritos, many=True)
        return Response(serializer.data)

class Participantes(APIView):
    def get(self, request, edicao):
        inscritos = Inscritos.objects.filter(edicao__numero=edicao)
        serializer = InscritosSerializers(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request, edicao):
        serializer = InscritosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, edicao):
        inscritos = Inscritos.objects.filter(edicao__numero=edicao)
        inscritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Cospobres(APIView):
    def get(self, request, edicao):
        participantes = Cospobre.objects.filter(edicao__numero=edicao)
        serializer = CospobreSerializers(participantes, many=True)
        return Response(serializer.data)

    def post(self, request, edicao):
        serializer = CospobreSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, edicao):
        participantes = Cospobre.objects.filter(edicao__numero=edicao)
        participantes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ParticipantesDetalhados(APIView):
    def get_object(self, edicao, pk):
        try:
            return Inscritos.objects.get(edicao__numero=edicao, pk=pk)
        except Inscritos.DoesNotExist:
            raise NotFound()

    def get(self, request, edicao, pk):
        inscritos = self.get_object(edicao, pk)
        serializer = InscritosSerializers(inscritos)
        return Response(serializer.data)

    def put(self, request, edicao, pk):
        inscritos = self.get_object(edicao, pk)
        serializer = InscritosSerializers(inscritos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, edicao, pk):
        inscritos = self.get_object(edicao, pk)
        inscritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CospobreDetalhados(APIView):
    def get_object(self, edicao, pk):
        try:
            return Cospobre.objects.get(edicao__numero=edicao, pk=pk)
        except Cospobre.DoesNotExist:
            raise NotFound()

    def get(self, request, edicao, pk):
        participante = self.get_object(edicao, pk)
        serializer = CospobreSerializers(participante)
        return Response(serializer.data)

    def put(self, request, edicao, pk):
        participante = self.get_object(edicao, pk)
        serializer = CospobreSerializers(participante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, edicao, pk):
        participante = self.get_object(edicao, pk)
        participante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@login_required(login_url='/admin/')
def limparPresentes(request, edicao):
    context = {}
    presentes = Inscritos.objects.filter(edicao__numero=edicao, presente=True)
    if request.method == 'POST':
        context['get'] = False
    else:
        context['get'] = True
        if len(presentes) > 0:
            context['sucess'] = True
            presentes.update(presente=False)
    context['sucess'] = False
    return render(request, 'zerar_participantes.html', context)
        

