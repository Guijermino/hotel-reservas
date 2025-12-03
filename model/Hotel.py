from typing import Optional
from .QuartoBase import Quarto 

class Hotel:
    
    _instancia: Optional['Hotel'] = None

    @staticmethod
    def obter_instancia(nome: str = "Hotel Padrão") -> 'Hotel':
        
        if Hotel._instancia is None:
            Hotel._instancia = Hotel(nome)
        
        return Hotel._instancia

    def __init__(self, nome: str):
        
        if hasattr(self, '_inicializado'):
            return
            
        self.nome: str = nome
        self.quartos: list[Quarto] = []
        self.reservas: list = []
        self._inicializado: bool = True
        print(f"Singleton Hotel '{self.nome}' foi inicializado (só deve ver esta msg 1 vez).")

    def adicionar_quarto(self, quarto: Quarto):
        self.quartos.append(quarto)
        print(f"Quarto #{quarto.numero} ({quarto.tipo}) adicionado ao {self.nome}.")

    def buscar_quarto_disponivel(self, tipo: str) -> Quarto | None:
        for quarto in self.quartos:
            if quarto.tipo == tipo.lower() and not quarto.esta_ocupado:
                return quarto
        return None

    def ocupar_quarto(self, numero_quarto: int) -> bool:
        for quarto in self.quartos:
            if quarto.numero == numero_quarto:
                if not quarto.esta_ocupado:
                    quarto.esta_ocupado = True
                    print(f"Quarto #{numero_quarto} foi ocupado.")
                    return True
                else:
                    print(f"Quarto #{numero_quarto} já está ocupado.")
                    return False
        
        print(f"Quarto #{numero_quarto} não encontrado.")
        return False