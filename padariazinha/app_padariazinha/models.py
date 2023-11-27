from django.db import models

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    produto = models.TextField(max_length=255)
    preco = models.IntegerField()