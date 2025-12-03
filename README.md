Sistema de Reservas de Hotel

Este projeto implementa um sistema de gerenciamento de reservas utilizando Programação Orientada a Objetos (POO) e padrões de projeto. Ele foi desenvolvido para a disciplina Técnicas de Orientação a Objetos (TOO).

1. Objetivos do Projeto

Aplicar os pilares da Programação Orientada a Objetos

Implementar padrões de projeto (Factory Method e Singleton)

Simular o fluxo de funcionamento de um hotel

Organizar o código seguindo boas práticas de modularização

2. Tecnologias Utilizadas

Python 3.x

POO (Programação Orientada a Objetos)

UML

3. Arquitetura do Sistema
hotel-reservas/
├── model/
│   ├── Quarto.py
│   ├── QuartoSimples.py
│   ├── QuartoBase.py
│   ├── QuartoDeLuxo.py
│   ├── Suite.py
│   ├── Hospede.py
│   └── Hotel.py
│
└── teste.py

4. Pilares da POO
4.1 Abstração

A classe Quarto representa um modelo genérico para qualquer tipo de quarto.

4.2 Encapsulamento

Cada classe concentra seus atributos e métodos internos, organizando melhor a lógica do sistema.

4.3 Herança

Os tipos de quartos (QuartoSimples, QuartoDuplo, QuartoDeLuxo, Suite) herdam de Quarto.

4.4 Polimorfismo

Cada tipo de quarto implementa sua própria versão de calcular_diaria().

5. Padrões de Projeto
5.1 Singleton – Classe Hotel

Garante que apenas uma instância da classe Hotel seja criada.

hotel = Hotel.obter_instancia()

5.2 Factory Method – FabricaQuartos

Responsável por criar objetos do tipo Quarto a partir de uma string:

quarto = FabricaQuartos.criar_quarto("luxo", 301)

6. Diagrama UML

![Diagrama UML](uml.png)

7. Como Executar
7.1 Pré-requisitos

Python 3 instalado

7.2 Execução

No terminal, dentro da pasta do projeto:

python main.py

8. Exemplo de Saída
Reserva criada com sucesso.
Reserva #1 - Hóspede: Guilherme - Quarto 301 - Total: R$ 550.00

9. Autor

Guilherme Guimarães Audibert
Ciência da Computação – 3º Semestre
