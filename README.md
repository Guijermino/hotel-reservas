# Sistema de Reservas de Hotel

Este projeto implementa um sistema de gerenciamento de reservas utilizando Programação Orientada a Objetos (POO) e padrões de projeto.  
Ele foi desenvolvido para a disciplina Técnicas de Orientação a Objetos (TOO).

---

## Objetivos do Projeto

- Aplicar os pilares da Programação Orientada a Objetos
- Implementar padrões de projeto (Factory Method e Singleton)
- Simular o fluxo de funcionamento de um hotel
- Organizar o código seguindo boas práticas de modularização

---

## Tecnologias Utilizadas

- Python 3.x
- Programação Orientada a Objetos (POO)
- UML

---

## Arquitetura do Sistema

```text
hotel-reservas/
│
├── model/
│   ├── Quarto.py
│   ├── QuartoBase.py
│   ├── QuartoSimples.py
│   ├── QuartoDeLuxo.py
│   ├── Suite.py
│   ├── Hospede.py
│   └── Hotel.py
│
└── teste.py
Pilares da Programação Orientada a Objetos
Abstração
A classe Quarto representa um modelo genérico para qualquer tipo de quarto.

Encapsulamento
Cada classe concentra seus atributos e métodos internos, organizando melhor a lógica do sistema.

Herança
Os tipos de quartos (QuartoSimples, QuartoDuplo, QuartoDeLuxo, Suite) herdam da classe Quarto.

Polimorfismo
Cada tipo de quarto implementa sua própria versão do método calcular_diaria().

Padrões de Projeto
Singleton – Classe Hotel
Garante que apenas uma instância da classe Hotel seja criada durante a execução do sistema.

python
Copiar código
hotel = Hotel.obter_instancia()
Factory Method – FabricaQuartos
Responsável por criar objetos do tipo Quarto a partir de uma string identificadora.

python
Copiar código
quarto = FabricaQuartos.criar_quarto("luxo", 301)
Como Executar
Pré-requisitos
Python 3 instalado

Execução
No terminal, dentro da pasta do projeto, execute:

bash
Copiar código
python main.py
Exemplo de Saída
nginx
Copiar código
Reserva criada com sucesso.
Reserva #1 - Hóspede: Guilherme - Quarto 301 - Total: R$ 550.00
Autor
Guilherme Guimarães Audibert
Ciência da Computação – 3º Semestre
