from datetime import date
from .QuartoBase import Quarto

class QuartoDeLuxo(Quarto):
    def __init__(self, numero: int, capacidade: int = 2, preco_base: float = 150.0):
        super().__init__(numero, capacidade, preco_base, tipo="luxo")
        self.id_reserva: int | None = None
        self.data_checkin: date | None = None
        self.data_checkout: date | None = None
        self.valor_total: float = 0.0

    def calcular_preco_diaria(self) -> float:
        return self.preco_base * 1.5