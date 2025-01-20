from django.shortcuts import render, redirect
from loja.models import Produto, Fabricante, Categoria
from loja.models import Produto
from datetime import timedelta, datetime
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

def delete_produto_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        produto = request.POST.get("Produto")
        print("postback-delete")
        print(id)
        try:
            Produto.objects.filter(id=id).delete()
            print("Produto %s excluido com sucesso" % produto)
        except Exception as e:
            print("Erro excluindo produto: %s" % e)
    return redirect("/produto")

def delete_produto_view(request, id=None):
    produtos = Produto.objects.all()
    Categorias = Categoria.objects.all()
    Fabricantes = Fabricante.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = {'produto': produto, 'fabricantes' : Fabricantes, 'categorias' : Categorias}
    return render(request, template_name='produto/produto-delete.html', context=context, status=200)

def details_produto_view(request, id=None):
    produtos = Produto.objects.all()
    Categorias = Categoria.objects.all()
    Fabricantes = Fabricante.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = {'produto': produto, 'fabricantes' : Fabricantes, 'categorias' : Categorias}
    return render(request, template_name='produto/produto-details.html', context=context, status=200)

@login_required
def edit_produto_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        produto = request.POST.get("Produto")
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        categoria = request.POST.get("CategoriaFk")
        fabricante = request.POST.get("FabricanteFk")
        print("postback")
        print(id)
        print(produto)
        print(destaque)
        print(promocao)
        print(msgPromocao)
        try:
            obj_produto = Produto.objects.filter(id=id).first()
            obj_produto.Produto = produto
            obj_produto.destaque = (destaque is not None)
            obj_produto.promocao = (promocao is not None)
            obj_produto.fabricante = Fabricante.objects.filter(id=fabricante).first()
            obj_produto.categoria = Categoria.objects.filter(id=categoria).first()
            if msgPromocao is not None:
                obj_produto.msgPromocao = msgPromocao
                obj_produto.save()
                print("Produto %s salvo com sucesso" % produto)
        except Exception as e:
                print("Erro salvando edição de produto: %s" % e)
    return redirect("/produto")


def edit_produto_view(request, id=None):
    produtos = Produto.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    Fabricantes = Fabricante.objects.all()
    Categorias = Categoria.objects.all()
    context = {'produto': produto, 'fabricantes' : Fabricantes, 'categorias' : Categorias}
    return render(request, template_name='produto/produto-edit.html', context=context, status=200)


def list_produto_view(request, id=None):
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    dias = request.GET.get("dias")
    produtos = Produto.objects.all()
    if id is not None:
        produtos = produtos.filter(Produto__contains=produto)
    if produto is not None:
        produtos = produtos.filter(Produto=produto)
    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)
    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)
    if categoria is not None:
        produtos = produtos.filter(categoria__Categoria=categoria)
    if fabricante is not None:
        produtos = produtos.filter(fabricante__Fabricante=fabricante)
    if dias is not None:
        now = timezone.now()
        now = now - timedelta(days=int(dias))
        produtos = produtos.filter(criado_em__gte=now)
    if id is not None:
        produtos = produtos.filter(id=id)
    print(produtos)
    context = {'produtos': produtos}
    return render(request, template_name='produto/produto.html', context=context, status=200)

def create_produto_view(request, id=None):
    if request.method == 'POST':
        produto = request.POST.get("Produto")
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        categoria_id = request.POST.get("CategoriaFk")
        fabricante_id = request.POST.get("FabricanteFk")
        preco = request.POST.get("preco")
        image = request.POST.get("image")
        print("postback-create")
        print(produto)
        print(destaque)
        print(promocao)
        print(msgPromocao)
        print(Categoria)
        print(Fabricante)
        print(preco)
        print(image)
        try:
            obj_produto = Produto()
            obj_produto = Categoria()
            obj_produto = Fabricante()
            obj_produto.Produto = produto
            obj_produto.Categoria = produto
            obj_produto.Fabricante = produto
            obj_produto.destaque = (destaque is not None)
            obj_produto.promocao = (promocao is not None)
            if msgPromocao is not None:
                obj_produto.msgPromocao = msgPromocao
            if categoria_id:
                obj_produto.categoria = Categoria.objects.filter(id=categoria_id).first()
            if fabricante_id:
                obj_produto.fabricante = Fabricante.objects.filter(id=fabricante_id).first()
            obj_produto.preco = 0
            if (preco is not None) and ( preco != ""):
                obj_produto.preco = preco
            obj_produto.criado_em = timezone.now()
            obj_produto.alterado_em = obj_produto.criado_em
            if request.FILES is not None:
                num_files = len(request.FILES.getlist('image'))
                if num_files > 0:
                    imagefile = request.FILES['image']
                    print(imagefile)
                    fs = FileSystemStorage()
                    filename = fs.save(imagefile.name, imagefile)
                    if (filename is not None) and (filename != ""):
                        obj_produto.image = filename
            obj_produto.save()
            print("Produto %s salvo com sucesso" % produto)
        except Exception as e:
            print("Erro inserindo produto: %s" % e)
        return redirect("/produto")
    categorias = Categoria.objects.all()
    fabricantes = Fabricante.objects.all()
    context = {'categorias': categorias, 'fabricantes': fabricantes}
    return render(request, template_name='produto/produto-create.html', context=context, status=200)