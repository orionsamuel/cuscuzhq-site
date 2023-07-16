from inscricao.models import Edicao, Inscritos, Cospobre, NotasCospobre
from inscricao.models import Cosplay, NotasCosplay, Artistas
from inscricao.forms import InscritosForm, CospobreForm, CosplayForm, ArtistaForm
from inscricao.serializers import InscritosSerializers, CospobreSerializers, NotasCospobreSerializers
from inscricao.serializers import CosplaySerializers, NotasCosplaySerializers, EdicaoSerializers

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
        serializerNotas = NotasCospobreSerializers(data=request.POST)
        if serializer.is_valid():
            if 'som' in request.FILES:
                serializer.save(edicao=Edicao.objects.last(), imagem=request.FILES['imagem'], som=request.FILES['som'])
            else:
                serializer.save(edicao=Edicao.objects.last(), imagem=request.FILES['imagem'])
        if serializerNotas.is_valid():
            serializerNotas.save(edicao=Edicao.objects.last(), nome=request.POST['nome'], 
                                personagem=request.POST['personagem'])
            redirect('cospobre.html')
            context['success'] = True
    form = CospobreForm()
    context['form'] = form
    context['edition'] = Edicao.objects.last().numero
    return render(request, 'cospobre.html', context)
    
def InscricaoCosplay(request): 
    context = {}
    if request.method == 'POST':
        form = CosplayForm(request.POST or None, request.FILES)
        serializer = CosplaySerializers(data=request.POST)
        serializerNotas = NotasCosplaySerializers(data=request.POST)
        if serializer.is_valid():
            if 'som' in request.FILES:
                serializer.save(edicao=Edicao.objects.last(), imagem=request.FILES['imagem'], som=request.FILES['som'])
            else:
                serializer.save(edicao=Edicao.objects.last(), imagem=request.FILES['imagem'])
        if serializerNotas.is_valid():
            serializerNotas.save(edicao=Edicao.objects.last(), nome=request.POST['nome'], 
                                personagem=request.POST['personagem'])
            redirect('cosplay.html')
            context['success'] = True
    form = CosplayForm()
    context['form'] = form
    context['edition'] = Edicao.objects.last().numero
    return render(request, 'cosplay.html', context)


def InscricaoArtista(request): 
    context = {}
    if request.method == 'POST':
        print(request.POST)
        form = ArtistaForm(request.POST or None, request.FILES)
        total = int(request.POST['experiencia']) * 1 + int(request.POST['obrasPublicadas']) * 50
        if form.is_valid():
            artista = form.save(commit=False)
            artista.edicao = edicao=Edicao.objects.last()
            artista.total = total
            artista.fliq = True
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
        
class Cosplays(APIView):
    def get(self, request, edicao):
        participantes = Cosplay.objects.filter(edicao__numero=edicao)
        serializer = CosplaySerializers(participantes, many=True)
        return Response(serializer.data)

    def post(self, request, edicao):
        serializer = CosplaySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, edicao):
        participantes = Cosplay.objects.filter(edicao__numero=edicao)
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
        
# class NotasCospobre(APIView):
#     def get(self, request, edicao):
#         notas = NotasCospobre.objects.filter(edicao__numero=edicao)
#         serializer = NotasCospobreSerializers(notas, many=True)
#         return Response(serializer.data)

#     def post(self, request, edicao):
#         serializer = NotasCospobreSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, edicao):
#         notas = NotasCospobre.objects.filter(edicao__numero=edicao)
#         notas.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class AlterarNotasCospobre(APIView):
    def get_object(self, edicao, pk):
        try:
            return NotasCospobre.objects.get(edicao__numero=edicao, pk=pk)
        except NotasCospobre.DoesNotExist:
            raise NotFound()

    def get(self, request, edicao, pk):
        notas = self.get_object(edicao, pk)
        serializer = NotasCospobreSerializers(notas)
        return Response(serializer.data)

    def post(self, request, edicao):
        serializer = NotasCospobreSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, edicao, pk):
        notas = self.get_object(edicao, pk)
        serializer = NotasCospobreSerializers(notas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CospobreVencedores(APIView):
    def get_object(self, edicao):
        try:
            return NotasCospobre.objects.get(edicao__numero=edicao)
        except NotasCospobre.DoesNotExist:
            raise NotFound()

    def get(self, request, edicao):
        participantes = NotasCospobre.objects.filter(edicao__numero=edicao).order_by('-total_nota')
        serializer = NotasCospobreSerializers(participantes, many=True)
        return Response(serializer.data)
        
class CosplayDetalhados(APIView):
    def get_object(self, edicao, pk):
        try:
            return Cosplay.objects.get(edicao__numero=edicao, pk=pk)
        except Cosplay.DoesNotExist:
            raise NotFound()

    def get(self, request, edicao, pk):
        participante = self.get_object(edicao, pk)
        serializer = CosplaySerializers(participante)
        return Response(serializer.data)

    def put(self, request, edicao, pk):
        participante = self.get_object(edicao, pk)
        serializer = CosplaySerializers(participante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, edicao, pk):
        participante = self.get_object(edicao, pk)
        participante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AlterarNotasCosplay(APIView):
    def get_object(self, edicao, pk):
        try:
            return NotasCosplay.objects.get(edicao__numero=edicao, pk=pk)
        except NotasCosplay.DoesNotExist:
            raise NotFound()

    def get(self, request, edicao, pk):
        notas = self.get_object(edicao, pk)
        serializer = NotasCosplaySerializers(notas)
        return Response(serializer.data)

    def put(self, request, edicao, pk):
        notas = self.get_object(edicao, pk)
        serializer = NotasCosplaySerializers(notas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotasCosplay(APIView):
    def get(self, request, edicao):
        notas = NotasCosplay.objects.filter(edicao__numero=edicao)
        serializer = NotasCosplaySerializers(notas, many=True)
        return Response(serializer.data)

    def post(self, request, edicao):
        serializer = NotasCosplaySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, edicao):
        notas = NotasCosplay.objects.filter(edicao__numero=edicao)
        notas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CosplayVencedores(APIView):
    def get_object(self, edicao):
        try:
            return NotasCosplay.objects.get(edicao__numero=edicao)
        except Cosplay.DoesNotExist:
            raise NotFound()

    def get(self, request, edicao):
        participantes = NotasCosplay.objects.filter(edicao__numero=edicao).order_by('-total_nota')
        serializer = NotasCosplaySerializers(participantes, many=True)
        return Response(serializer.data)

class GetEdicao(APIView):
    def get_object(self):
        try:
            return Edicao.objects.get()
        except Edicao.DoesNotExist:
            raise NotFound()

    def get(self, request):
        edicao = Edicao.objects.last()
        serializer = EdicaoSerializers(edicao)
        return Response(serializer.data)

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
        

