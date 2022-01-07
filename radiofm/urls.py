"""radiofm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import PauloContruções, login_requirido, CadastroClienteView, Contrato, ListCliente, OpcoesPag, PagamentoAprovado, CreateAssinatura, Finalizacao, ListFinal
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),
    path("", include("pages.urls", namespace="pages")),
    path("divulgacao1/", PauloContruções.as_view(), name="divulgação"),
    path('requerid/', views.login_requirido, name="burlar_login"),
    path('add-cliente/', CadastroClienteView.as_view(), name='add-cliente'),
    path('contrato/', Contrato.as_view(), name='contrato'),
    path('list-cliente/', ListCliente.as_view(), name='listar-cliente'),
    path('opçoes-pagamento/', OpcoesPag.as_view(), name='opc-pagamento'),
    path('pagamento-aprovado/', PagamentoAprovado.as_view(), name='pag-aproved'),
    path('create-assinatura/', CreateAssinatura.as_view(), name='create-final'),
    path('finalizacao/', Finalizacao.as_view(), name='final'),
    path('list-final/', ListFinal.as_view(), name='list-final'),
]
