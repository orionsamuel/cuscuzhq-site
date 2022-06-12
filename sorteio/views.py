from inscricao.models import Inscritos, Edicao

from django.shortcuts import render
import random

def sorteio(request, edicao):
    context = {}
    if request.method == 'POST':
        context['get'] = False
        participantes = Inscritos.objects.filter(edicao__numero=edicao, 
                        presente=True, sorteado=False)
        id_participantes = []
        for participante in participantes:
            id_participantes.append(participante.id)
        if len(id_participantes) > 0:
            id_sorteado = random.choice(id_participantes)
            participante_sorteado = Inscritos.objects.get(pk=id_sorteado)
            participante_sorteado.sorteado = True
            participante_sorteado.save()
            context['success'] = True
            context['sorteado'] = participante_sorteado.nome
            telefone = '****' + participante_sorteado.telefone[-4:]
            context['telefone'] = telefone
        else:
            context['sucess'] = False
    else:
        participantes = Inscritos.objects.filter(edicao__numero=edicao, 
                        presente=True, sorteado=False)
        id_participantes = []
        for participante in participantes:
            id_participantes.append(participante.id)
        if len(id_participantes) == 0:
            context['get'] = True
    return render(request, 'sorteio.html', context)
        
