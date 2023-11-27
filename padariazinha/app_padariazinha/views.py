from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request, 'usuarios/home.html')

def produto(request):
    #Salvar os dados da tela para o banco de dados
    novo_produto = Produto()
    novo_produto.produto = request.POST.get('produto')
    novo_produto.preco = request.POST.get('preco')
    novo_produto.save()
    #Exibir todos os usuários já cadastrados em uma nova página
    produtos = {
        'produtos': Produto.objects.all()
    }
    #retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/produtos.html', produtos)