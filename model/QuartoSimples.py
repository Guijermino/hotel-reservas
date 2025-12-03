from .QuartoBase import Quarto  

class QuartoSimples(Quarto):
    """
    (Pilar da Herança: herda de Quarto)
    """
    def __init__(self, numero: int, capacidade: int = 2, preco_base: float = 100.0):
        super().__init__(numero, capacidade, preco_base, tipo="simples")

    def calcular_preco_diaria(self) -> float:
        """ (Implementação do Polimorfismo) """
        return self.preco_base