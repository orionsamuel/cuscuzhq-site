from inscricao.views import Inscricao, Participantes, ParticipantesDetalhados, BuscarParticipante
from inscricao.views import limparPresentes, InscricaoCospobre, InscricaoCosplay, InscricaoArtista
from inscricao.views import Cospobres, CospobreDetalhados
from inscricao.views import Cosplays, CosplayDetalhados
from django.urls import path

urlpatterns = [
    path('', Inscricao),
    path('cospobre', InscricaoCospobre),
    path('cosplay', InscricaoCosplay),
    path('artistas', InscricaoArtista),
    path('v1/participantes/<int:edicao>/', Participantes.as_view()),
    path('v1/participantes/<int:edicao>/buscar/<str:busca>/', BuscarParticipante.as_view()),
    path('v1/participantes/<int:edicao>/<int:pk>/', ParticipantesDetalhados.as_view()),
    path('v1/cospobre/<int:edicao>/', Cospobres.as_view()),
    path('v1/cospobre/<int:edicao>/<int:pk>/', CospobreDetalhados.as_view()),
    path('v1/cosplay/<int:edicao>/', Cosplays.as_view()),
    path('v1/cosplay/<int:edicao>/<int:pk>/', CosplayDetalhados.as_view()),
    path('presentes/<int:edicao>/', limparPresentes),
]
