from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.template.loader import get_template
from .models import CadastroCliente, CadastroFinal

# Create your views here.


#TemplateView

class PauloContruções(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('burlar_login')
    template_name = 'paulo.html'


def login_requirido(request):
    return render(request, 'requerid.html')


class CadastroClienteView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('burlar_login')
    model = CadastroCliente
    fields = ['nome_cliente', 'data_assinatura', 'plano_escolhido']
    template_name = 'create.html'
    success_url = ('/opçoes-pagamento')

    def form_valid(self, form):

        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url



class Contrato(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('burlar_login')
    template_name = 'contrato.html'


class ListCliente(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('burlar_login')
    model = CadastroCliente
    template_name = 'list-cliente.html'

    def get_queryset(self):
        self.object_list = CadastroCliente.objects.filter(usuario=self.request.user)
        return self.object_list


#class OpcoesPag(LoginRequiredMixin, TemplateView):
    #login_url = reverse_lazy('burlar_login')
    #template_name = 'pagamento.html'


#class PagamentoAprovado(LoginRequiredMixin, TemplateView):
    #login_url = reverse_lazy('burlar_login')
    #template_name = 'pagamento-aprovado.html'


#class PagamentoProcessandp(LoginRequiredMixin, TemplateView):
    #login_url = reverse_lazy('burlar_login')
    #template_name = 'pagamento-process.html'