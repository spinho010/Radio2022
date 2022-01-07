from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.


class ClientePlano(models.Model):
    plano = models.CharField(verbose_name='Plano: ', max_length=100, blank=True, null=True)
    descri = models.CharField(verbose_name='Descrição: ', max_length=100, blank=True, null=True)

    def __str__(self):
            return "{}".format(self.plano)


class CadastroCliente(models.Model):
    nome_cliente = models.CharField(verbose_name='Nome: ', max_length=60, null=True, blank=True)
    data_assinatura = models.DateTimeField(verbose_name='Data da Assinatura: ', null=False)
    plano_escolhido = models.ForeignKey(ClientePlano, max_length=100, null=True, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
            return "{}".format(self.plano_escolhido)


class CadastroFinal(models.Model):
    nome = models.CharField(verbose_name='Nome: ', max_length=60, null=False)
    data = models.DateTimeField(verbose_name='Data: ', null=False)
    endereco = models.CharField(verbose_name='Endereço: ', max_length=150, null=False)
    contato = models.CharField(verbose_name='Telefone: ', max_length=150, null=False)
    plano_solicitado = models.ForeignKey(ClientePlano, max_length=100, null=True, on_delete=models.PROTECT)

    def __str__(self):
            return "{}".format(self.nome)
