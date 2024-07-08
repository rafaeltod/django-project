from django.contrib import admin
# Register your models here.
from .models import *
class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Categoria)
class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'
admin.site.register(Produto, ProdutoAdmin)