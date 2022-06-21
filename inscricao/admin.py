from django.contrib import admin
from inscricao.models import Inscritos, Edicao, Cospobre

class InscritosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'edicao', 'presente']
    search_fields = ['nome', 'edicao']

class CospobreAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'personagem', 'edicao', 'imagem', 'som', 
                    'nota_1', 'nota_2', 'nota_3']
    search_fields = ['nome', 'edicao']

class EdicaoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'titulo']
    search_fields = ['numero']

admin.site.register(Inscritos, InscritosAdmin)
admin.site.register(Cospobre, CospobreAdmin)
admin.site.register(Edicao, EdicaoAdmin)
