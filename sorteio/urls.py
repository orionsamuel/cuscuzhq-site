from sorteio.views import sorteio
from django.urls import path

urlpatterns = [
    path('<int:edicao>/', sorteio),
]