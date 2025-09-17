from django.contrib import admin
from inscricao.models import Inscritos, Edicao, Cospobre, Cosplay, Artistas, NotasCospobre, NotasCosplay

class InscritosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'edicao', 'presente1', 'presente2']
    search_fields = ['nome', 'edicao']

class CospobreAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'personagem', 'edicao', 'imagem', 'som', 
                    'direitoImagem']
    search_fields = ['nome', 'edicao']

class NotasCospobreAdmin(admin.ModelAdmin):
    list_display = ['nome', 'personagem', 'edicao', 'cospobreId', 'nota_1', 'nota_2', 'nota_3', 'total_nota']
    search_fields = ['nome', 'personagem', 'edicao']
    
class CosplayAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'personagem', 'edicao', 'imagem', 'som', 
                    'direitoImagem']
    search_fields = ['nome', 'edicao']

class NotasCosplayAdmin(admin.ModelAdmin):
    list_display = ['nome', 'personagem', 'edicao', 'cosplayId', 'nota_1', 'nota_2', 'nota_3', 'total_nota']
    search_fields = ['nome', 'personagem', 'edicao']

class ArtistasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'experiencia', 'obrasPublicadas', 'obrasFuturas',
                'instagram', 'facebook', 'devianart', 'blog', 'outraRedeSocial', 'arquivos', 'total', 'fliq']
    search_fields = ['nome', 'edicao']

class EdicaoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'titulo']
    search_fields = ['numero']

admin.site.register(Inscritos, InscritosAdmin)
admin.site.register(Cospobre, CospobreAdmin)
admin.site.register(NotasCospobre, NotasCospobreAdmin)
admin.site.register(Cosplay, CosplayAdmin)
admin.site.register(NotasCosplay, NotasCosplayAdmin)
admin.site.register(Artistas, ArtistasAdmin)
admin.site.register(Edicao, EdicaoAdmin)
