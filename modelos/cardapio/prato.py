"""Arquivo: modelos/cardapio/prato.py"""
from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    """Classe que representa um prato no cardápio.
    
    Args:
        nome (str): Nome do prato.
        preco (float): Preço do prato.
        descricao (str): Descrição do prato.
    """
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao