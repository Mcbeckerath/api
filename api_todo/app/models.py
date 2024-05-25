from django.db import models

class Produto(models.Model):
    nome = models.TextField()
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    limite_cri = models.IntegerField()
    limite_adu = models.IntegerField()
    limite_beb = models.IntegerField()

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=255, default='Default Nome')

    def __str__(self):
        return self.nome

class Nivel(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class Relacao(models.Model):
    inicio = models.DateField()
    fim = models.DateField()
    quant_cri = models.IntegerField()
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE, null=True)
    nivel = models.ForeignKey("Nivel", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Relação {self.id} - {self.usuario.nome} - {self.produto.nome}"
