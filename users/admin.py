from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from users.models import CadastroCliente, CadastroFinal, ClientePlano

# Register your models here.

class Cadastro1Admin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'data_assinatura', 'plano_escolhido', 'usuario')

admin.site.register(CadastroCliente, Cadastro1Admin)


class Cadastro2Admin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'endereco', 'contato', 'plano_solicitado')

admin.site.register(CadastroFinal, Cadastro2Admin)


class PlanosAdmin(admin.ModelAdmin):
    list_display = ('plano', 'descri')

admin.site.register(ClientePlano, PlanosAdmin)