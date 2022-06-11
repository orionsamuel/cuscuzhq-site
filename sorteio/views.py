from inscricao.models import Inscritos, Edicao

from django.shortcuts import render
import random

def sorteio(request, edicao):
    context = {}
    if request.method == 'POST':
        participantes = Inscritos.objects.filter(edicao__numero=edicao, 
                        presente=True, sorteado=False)
        id_participantes = []
        for participante in participantes:
            id_participantes.append(participante.id)
        id_sorteado = random.choice(id_participantes)
        participante_sorteado = Inscritos.objects.get(pk=id_sorteado)
        context['success'] = True
        context['sorteado'] = participante_sorteado.nome
        telefone = '****' + participante_sorteado.telefone[-4:]
        context['telefone'] = telefone
    return render(request, 'sorteio.html', context)
        
