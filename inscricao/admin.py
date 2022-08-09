from django.contrib import admin
from inscricao.models import Inscritos, Edicao, Cospobre, Cosplay, Artistas

class InscritosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'edicao', 'presente']
    search_fields = ['nome', 'edicao']

class CospobreAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'personagem', 'edicao', 'imagem', 'som', 
                    'direitoImagem', 'nota_1', 'nota_2', 'nota_3']
    search_fields = ['nome', 'edicao']
    
class CosplayAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'personagem', 'edicao', 'imagem', 'som', 
                    'direitoImagem', 'nota_1', 'nota_2', 'nota_3']
    search_fields = ['nome', 'edicao']

class ArtistasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'experiencia', 'obrasPublicadas', 'obrasFuturas',
                'instagram', 'facebook', 'devianart', 'blog', 'outraRedeSocial', 'arquivos']
    search_fields = ['nome', 'edicao']

class EdicaoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'titulo']
    search_fields = ['numero']

admin.site.register(Inscritos, InscritosAdmin)
admin.site.register(Cospobre, CospobreAdmin)
admin.site.register(Cosplay, CosplayAdmin)
admin.site.register(Artistas, ArtistasAdmin)
admin.site.register(Edicao, EdicaoAdmin)
