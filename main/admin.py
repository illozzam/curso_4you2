from django.contrib import admin
from main.models import Categoria, Produto


class ProdutoInLine(admin.TabularInline):
    model = Produto
    fields = ['nome', 'quantidade', 'preco']
    extra = 0


# @admin.register(Produto)
# class ProdutoAdmin(admin.ModelAdmin):
#     list_display = ['nome', 'quantidade', 'preco', 'dia_hora']
#     list_editable = ['preco']
#     list_filter = ['nome']
#     search_fields = ['nome']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProdutoInLine]