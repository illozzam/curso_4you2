from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .models import Categoria, Produto

from .forms import CarrinhoForm


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
        produto = Produto.objects.get(id=kwargs['produto_id'])
        contexto = {
            'produto': produto,
            'formulario': CarrinhoForm(instance=produto),
        }
        return render(request, 'carrinho.html', contexto)

    def post(self, request, **kwargs):
        produto = Produto.objects.get(id=kwargs['produto_id'])
        formulario = CarrinhoForm(request.POST, instance=produto)
        if formulario.is_valid():
            formulario.save()
        return redirect('inicial')
