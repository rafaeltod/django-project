from django.shortcuts import render, get_object_or_404, redirect
from loja.models import Produto, Carrinho, CarrinhoItem
from datetime import datetime
# Função para adicionar um item ao carrinho
def create_carrinhoitem_view(request, produto_id=None):
    print ('create_carrinhoitem_view')
    produto = get_object_or_404(Produto, pk=produto_id)
    if produto:
        print('produto: ' + str(produto.id))
    # Tenta pegar o carrinho da sessão ou cria um novo carrinho
    carrinho_id = request.session.get('carrinho_id')
    print ('carrinho: ' + str(carrinho_id))
    carrinho = None
    if carrinho_id:
        # Se o carrinho já estiver na sessão, tentamos obter o carrinho
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        print (carrinho)
        print ('carrinho1: ' + str(carrinho.id))
        hoje = datetime.today().date()
        # Caso queira define uma expiração do carrinho
        if carrinho.criado_em.date() != hoje:
            # Se o carrinho não for de hoje, cria um novo carrinho
            carrinho = Carrinho.objects.create()
            # Armazena o ID do carrinho na sessão
            request.session['carrinho_id'] = carrinho.id
            print ('novo carrinho: ' + str(carrinho.id))
    else:
        # Se o carrinho não existir na sessão, cria um novo carrinho
        carrinho = Carrinho.objects.create()
        # Armazena o ID do carrinho na sessão
        request.session['carrinho_id'] = carrinho.id
        print ('carrinho2: ' + str(carrinho.id))
    # Verifica se o produto já existe no carrinho do usuário
    carrinho_item = CarrinhoItem.objects.filter(carrinho=carrinho, produto=produto).first()
    if carrinho_item:
        # Se o produto já estiver no carrinho, apenas aumenta a quantidade
        carrinho_item.quantidade += 1
        print ('item de carrinho: Acrescentou 1 item do produto ' + str(carrinho_item.id))
    else:
        # Se o produto não estiver no carrinho, cria um novo item no carrinho
        carrinho_item = CarrinhoItem.objects.create(
            carrinho=carrinho,
            produto=produto,
            quantidade=1,
            preco=produto.preco
        )
        print ('item de carrinho: Acrescentou o produto ' + str(carrinho_item.id))
    carrinho_item.save()
    print ('item de carrinho salvo: ' + str(carrinho_item.id))
    return redirect('/carrinho')