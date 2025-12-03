from model.Hotel import Hotel
from model.QuartoFactory import ConcreteQuartoFactory 

def main():
    print("--- 1. Inicializando o Hotel (Singleton) ---")
    hotel = Hotel.obter_instancia("Grand Hotel")
    
    print("\n--- 2. Tentando criar outra instância do Hotel ---")
    hotel_clone = Hotel.obter_instancia("Hotel Falso")
    print(f"Hotel 1 é o mesmo objeto que Hotel 2? {hotel is hotel_clone}")
    print(f"Nome do hotel: {hotel.nome}")

    print("\n--- 3. Usando a Factory para criar quartos ---")
    factory = ConcreteQuartoFactory() 
    
    quarto_101 = factory.criar_quarto("simples", 101)
    quarto_201 = factory.criar_quarto("luxo", 201)
    quarto_301 = factory.criar_quarto("suite", 301)

    print("\n--- 4. Adicionando quartos ao Hotel ---")
    hotel.adicionar_quarto(quarto_101)
    hotel.adicionar_quarto(quarto_201)
    hotel.adicionar_quarto(quarto_301)

    print("\n--- 5. Buscando e Ocupando Quartos ---")
    quarto_disponivel = hotel.buscar_quarto_disponivel("simples")
    if quarto_disponivel:
        print(f"Quarto simples encontrado: #{quarto_disponivel.numero}")
        hotel.ocupar_quarto(quarto_disponivel.numero)
    else:
        print("Nenhum quarto simples disponível.")

if __name__ == "__main__":
    main()