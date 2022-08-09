from django.db import models

class Edicao(models.Model):
    numero = models.IntegerField()
    titulo = models.CharField(max_length=150)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Edição"
        verbose_name_plural = 'Edições'
        ordering = ['numero']

class Inscritos(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, default="")
    presente = models.BooleanField(default=False)
    sorteado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = 'Participantes'
        ordering = ['nome', 'edicao']

class Cospobre(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    personagem = models.CharField(max_length=150, null=True)
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, default="")
    imagem = models.ImageField(upload_to='cospobre/images', verbose_name='Imagem', null=True, blank=False)
    som = models.FileField(upload_to="cospobre/sounds", verbose_name='Musica', null=True, blank=False)
    direitoImagem = models.BooleanField(default=False, null=True, blank=False)
    nota_1 = models.IntegerField(null=True, default=0)
    nota_2 = models.IntegerField(null=True, default=0)
    nota_3 = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cospobre"
        verbose_name_plural = 'Cospobres'
        ordering = ['nome', 'personagem', 'edicao']
        
class Cosplay(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    personagem = models.CharField(max_length=150, null=True)
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, default="")
    imagem = models.ImageField(upload_to='cosplay/images', verbose_name='Imagem', null=True, blank=False)
    som = models.FileField(upload_to="cosplay/sounds", verbose_name='Musica', null=True, blank=False)
    direitoImagem = models.BooleanField(default=False, null=True, blank=False)
    nota_1 = models.IntegerField(null=True, default=0)
    nota_2 = models.IntegerField(null=True, default=0)
    nota_3 = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cosplay"
        verbose_name_plural = 'Cosplays'
        ordering = ['nome', 'personagem', 'edicao']

class Artistas(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, default="")
    experiencia = models.IntegerField()
    obrasPublicadas = models.IntegerField()
    obrasFuturas = models.TextField(max_length=400)
    instagram = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    devianart = models.CharField(max_length=200, blank=True)
    blog = models.CharField(max_length=200, blank=True)
    outraRedeSocial = models.CharField(max_length=200, blank=True)
    arquivos = models.FileField(upload_to="artistas/files", verbose_name='Arquivos', null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = 'Artistas'
        ordering = ['nome', 'edicao']

