from django.db import models

# Categoria -> id, nome
# Produto -> id, nome, quantidade, preco, categoria

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    dia_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome