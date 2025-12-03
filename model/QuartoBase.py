# quartos/quarto_base.py
from abc import ABC, abstractmethod

class Quarto(ABC):
    """
    Classe base ABSTRATA para um quarto de hotel.
    (Pilar da Abstração)
    """
    def __init__(self, numero: int, capacidade: int, preco_base: float, tipo: str):
        # (Pilar do Encapsulamento)
        self._numero = numero
        self._capacidade = capacidade
        self._preco_base = preco_base
        self._esta_ocupado = False
        self._tipo = tipo 

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def capacidade(self) -> int:
        return self._capacidade

    @property
    def preco_base(self) -> float:
        return self._preco_base

    @property
    def esta_ocupado(self) -> bool:
        return self._esta_ocupado
    
    @property
    def tipo(self) -> str:
        return self._tipo

    @esta_ocupado.setter
    def esta_ocupado(self, status: bool):
        self._esta_ocupado = status

    @abstractmethod
    def calcular_preco_diaria(self) -> float:
        """ (Pilar do Polimorfismo) """
        pass

    def __str__(self):
        return f"Quarto {self.tipo.capitalize()} #{self.numero} (Cap: {self.capacidade}) - Ocupado: {self.esta_ocupado}"