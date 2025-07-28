"""Arquivo: modelos/cardapio/bebida.py"""
from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    """Classe que representa uma bebida no cardápio.

    Args:
        nome (str): Nome da bebida. 
        preco (float): Preço da bebida.
        tamanho (str): Tamanho da bebida (ex: pequeno, médio, grande).
    """
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
