from django.db import models

class Edicao(models.Model):
    numero = models.IntegerField()
    titulo = models.CharField(max_length=150)

    def __str__(self):
        return self.titulo

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
    som = models.FileField(upload_to="cospobre/sounds", verbose_name='Musica', null=True, blank=True)
    nota_1 = models.IntegerField(null=True, default=0)
    nota_2 = models.IntegerField(null=True, default=0)
    nota_3 = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cospobre"
        verbose_name_plural = 'Cospobres'
        ordering = ['nome', 'personagem', 'edicao']