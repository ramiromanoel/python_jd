"""
import json
lista = ["sapato", 39, 10.38, True]

produto1 = {
    "nome": "sapato",
    "quantidade": 39,
    "preco": 10.38,
    "disponibilidade": True
}

produto2 = {
    "nome": "televisao",
    "quantidade": 10,
    "preco": 70.38,
    "disponibilidade": False
}

carrinho: list = []

carrinho.append(produto1)
carrinho.append(produto2)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)
"""

from typing import Dict, Any

livro1: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "Estagiário",
    "Ano": 2005
}

livro2: Dict[str, Any] = {
    "Titulo": "Game of Thrones 2",
    "Autor": "Estagiário",
    "Ano": 2007
}

lista_de_livros = []

lista_de_livros.append(livro1)
lista_de_livros.append(livro2)

print(lista_de_livros)

lista_de_livros_usando_dict: dict = {
    "livro1": {
    "Titulo": "Game of Thrones 2",
    "Autor": "Estagiário",
    "Ano": 2007
    },

    "livro2": {
    "Titulo": "Game of Thrones 2",
    "Autor": "Estagiário",
    "Ano": 2007
    }
}

print(lista_de_livros_usando_dict["livro1"]["Titulo"])