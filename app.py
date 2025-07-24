"""app.py"""
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Restaurante Praça", "Gourmet")
restaurante_mexicano = Restaurante("Restaurante Mexicano", "Mexicano")
restaurante_japones = Restaurante("Restaurante Japonês", "Japonesa")
restaurante_praca.receber_avaliacao("Cliente 1", 5)

restaurante_mexicano.alternar_estado()

def main():
    """Main function to run the application."""
    Restaurante.lista_restaurantes()


if __name__ == "__main__":
    main()
