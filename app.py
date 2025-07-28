"""app.py"""
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante("Restaurante Praça", "Gourmet")
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
prato_pasta = Prato('Pasta à Carbonara', 30.00, 'Deliciosa pasta com molho cremoso e bacon.')
restaurante_praca.adicionar_bebida_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_cardapio(prato_pasta)

def main():
    """Main function to run the application."""
    print(bebida_suco)
    print(prato_pasta)
    restaurante_praca.lista_restaurantes()



if __name__ == "__main__":
    main()
