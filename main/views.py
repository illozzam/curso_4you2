from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .models import Categoria, Produto


class InicialView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['valor_total'] = 0
        for produto in Produto.objects.all():
            context['valor_total'] += produto.quantidade * produto.preco
        return context


class CarrinhoView(View):
    def get(self, request, **kwargs):
        contexto = {
            'produto': Produto.objects.get(id=kwargs['produto_id']),
        }
        return render(request, 'carrinho.html', contexto)

    def post(self, request, **kwargs):
        produto = Produto.objects.get(id=kwargs['produto_id'])
        quantidade = request.POST['quantidade']
        preco = request.POST.get('preco')

        produto.quantidade = quantidade
        if preco:
            produto.preco = preco
        produto.save()
        return redirect('inicial')
