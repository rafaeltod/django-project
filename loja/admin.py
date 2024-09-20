from django.contrib import admin
# Register your models here.
from .models import *
class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
    search_fields = ('Fabricante',)
admin.site.register(Fabricante, FabricanteAdmin)
class CategoriaAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
    search_fields = ('Categoria',)
admin.site.register(Categoria, CategoriaAdmin)
class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'
    search_fields = ('Produto',)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario)