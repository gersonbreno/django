from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, FormView, DeleteView, View, UpdateView
from .models import Tarefa
from django.urls import reverse_lazy
from . forms import CadastrarTarefaForms, AtulizarTarefaForms
from datetime import date
# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista'] = Tarefa.objects.all().order_by("-data_entrega")
        return context
        

class CriaListaView(FormView):
    template_name = 'cadastrar.html'
    form_class = CadastrarTarefaForms
    success_url = reverse_lazy("home")
    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)
    
class  DelatarListaView(DeleteView):
    model = Tarefa
    template_name = "exluir.html"
    success_url = reverse_lazy('home')


class  ConcluirView(View):
    def get(self, request, pk):
        lista = Tarefa.objects.get(pk = pk)
        lista.data_fim = date.today()
        lista.save()
        return redirect("home")
class AtualizaListaView(UpdateView):
    model = Tarefa
    template_name = 'atualizar.html'
    form_class = AtulizarTarefaForms
    success_url = reverse_lazy("home")
    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    
    def get_form(self, form_class=None):
        form = super().get_form(AtulizarTarefaForms)
        # Esconda o campo que você não quer editar
        del form.fields['data_fim']
        return form
