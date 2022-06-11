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
