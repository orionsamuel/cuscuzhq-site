from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscricao/', include('inscricao.urls')),
    path('sorteio/', include('sorteio.urls')),
]
