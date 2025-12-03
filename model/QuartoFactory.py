from abc import ABC, abstractmethod
from .QuartoBase import Quarto
from .QuartoSimples import QuartoSimples
from .QuartoDeLuxo import QuartoDeLuxo
from .Suite import Suite

class QuartoFactory(ABC):
    """ Interface da Fábrica (Padrão Factory) """
    @abstractmethod
    def criar_quarto(self, tipo: str, numero: int) -> Quarto:
        pass

class ConcreteQuartoFactory(QuartoFactory):
    """ Implementação concreta da Fábrica """
    
    def criar_quarto(self, tipo: str, numero: int) -> Quarto:
        tipo_lower = tipo.lower()
        
        if tipo_lower == "simples":
            return QuartoSimples(numero=numero)
        
        elif tipo_lower == "luxo":
            return QuartoDeLuxo(numero=numero)
        
        elif tipo_lower == "suite":
            return Suite(numero=numero) 
        
        else:
            raise ValueError(f"Tipo de quarto desconhecido: {tipo}")