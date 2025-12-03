from .QuartoBase import Quarto

class Suite(Quarto):
    """
    (Pilar da Herança: herda de Quarto)
    """
    def __init__(self, numero: int, area_m2: float = 50.0, capacidade: int = 4, preco_base: float = 250.0):
        super().__init__(numero, capacidade, preco_base, tipo="suite")
        self._area_m2 = area_m2

    @property
    def area_m2(self) -> float:
        return self._area_m2

    def calcular_preco_diaria(self) -> float:
        """ (Implementação do Polimorfismo) """
        return self.preco_base * 2.0