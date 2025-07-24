"""módulo modelos.restaurante"""

from modelos.avaliacao import Avaliacao


class Restaurante:
    """Classe que representa um restaurante."""

    restaurantes = []

    def __init__(self, nome, categoria, ativo=False):
        """
        Inicializa uma instância de Restaurante.

        :param nome(str): Nome do restaurante.
        :param categoria(str): Categoria do restaurante (ex: Gourmet, Mexicano, etc).
        """
        self._nome = nome
        self._categoria = categoria
        self._ativo = ativo
        self.avaliacao = []
        Restaurante.restaurantes.append(self)

    @property
    def nome(self):
        """Retorna o nome do restaurante."""
        return self._nome

    @property
    def categoria(self):
        """Retorna a categoria do restaurante."""
        return self._categoria

    @property
    def ativo(self):
        """Retorna o estado do restaurante (ativo ou inativo)."""
        return self._ativo

    def __str__(self) -> str:
        return (
            f"{self.nome} ({self.categoria}) - {'Ativo' if self.ativo else 'Inativo'}"
        )

    def alternar_estado(self):
        """Alterna o estado do restaurante entre ativo e inativo."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Recebe uma avaliação de um cliente.

        :param cliente(str): Nome do cliente que fez a avaliação.
        :param nota(int): Nota dada pelo cliente (de 1 a 5).
        
        """
        if not isinstance(nota, (int, float)) or not 1 <= nota <= 5:
            raise ValueError("A nota deve ser um número entre 1 e 5.")
        avaliacao = Avaliacao(cliente, nota)
        self.avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula a média das avaliações recebidas pelo restaurante."""
        if not self.avaliacao:
            return "-"
        soma_das_notas = sum(avaliacao.nota for avaliacao in self.avaliacao)
        quantidade_de_notas = len(self.avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    @classmethod
    def lista_restaurantes(cls) -> None:
        """Lista todos os restaurantes cadastrados."""
        print(
            f'{"Nome do restaurante".ljust(25)} | '
            f'{"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}'
        )
        for restaurante in cls.restaurantes:
            print(
                f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | '
                f'{str(restaurante.media_avaliacoes).ljust(25)} | '
                f'{"Ativo" if restaurante.ativo else "Inativo"}'
            )
