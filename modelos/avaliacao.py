"""módulo modelos.avaliacao"""

class Avaliacao:
    """Classe que representa uma avaliação de restaurante."""
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota

    @property
    def cliente(self):
        """Retorna o cliente que fez a avaliação."""
        return self._cliente

    @property
    def nota(self):
        """Retorna a nota da avaliação."""
        return self._nota

    def __str__(self):
        return f"Avaliação de {self._cliente}: {self._nota}"
