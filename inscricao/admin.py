from django.contrib import admin
from inscricao.models import Inscritos, Edicao

class InscritosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'edicao', 'presente']
    search_fields = ['nome', 'edicao']

class EdicaoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'titulo']
    search_fields = ['numero']

admin.site.register(Inscritos, InscritosAdmin)
admin.site.register(Edicao, EdicaoAdmin)
