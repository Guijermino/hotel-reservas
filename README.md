Sistema de Reservas de Hotel
Descrição do Projeto

Este projeto foi desenvolvido para a disciplina de Técnicas de Orientação a Objetos (TOO).
Ele representa um sistema simples de gerenciamento de reservas em um hotel, permitindo cadastrar hóspedes, quartos e gerar reservas com cálculo automático do valor total.

A proposta do trabalho é demonstrar, na prática, os pilares da Programação Orientada a Objetos e a aplicação de dois padrões de projeto: Factory Method e Singleton.

Funcionalidades do Sistema

Cadastro de quartos

Cadastro de hóspedes

Criação de reservas

Cálculo automático do valor total da estadia

Tipos diferentes de quartos, cada um com seu próprio cálculo de diária

Utilização dos padrões de projeto Singleton e Factory

Estrutura do Projeto
hotel-reservas/
│
├── main.py
├── README.md
│
├── core/
│   └── Hotel.py
│
├── model/
│   ├── Quarto.py
│   ├── QuartoSimples.py
│   ├── QuartoDuplo.py
│   ├── QuartoLuxo.py
│   ├── Suite.py
│   ├── Hospede.py
│   └── Reserva.py
│
└── FabricaQuartos.py

Pilares da Programação Orientada a Objetos
1. Abstração

A classe Quarto representa um modelo genérico de quarto, definindo atributos essenciais e o método abstrato calcular_diaria().

2. Encapsulamento

Os atributos e métodos relacionados a cada entidade (quarto, hóspede, reserva, etc.) estão encapsulados em suas respectivas classes.

3. Herança

Os tipos de quarto (QuartoSimples, QuartoDuplo, QuartoLuxo e Suite) herdam da classe Quarto, reutilizando código e características comuns.

4. Polimorfismo

Cada tipo de quarto implementa sua própria versão do método calcular_diaria(), alterando o comportamento conforme necessário.

Padrões de Projeto Utilizados
Factory Method

A classe FabricaQuartos é responsável por criar instâncias de quartos com base no tipo informado.
Isso organiza a criação de objetos e facilita a expansão do sistema.

Singleton

A classe Hotel utiliza o padrão Singleton para garantir que apenas uma instância do hotel exista durante toda a execução do sistema.
Tudo é centralizado em um único objeto gerenciador.

Como Executar o Projeto

Certifique-se de ter o Python instalado.

Abra o terminal na pasta raiz do projeto.

Execute o comando:

python main.py


O sistema irá gerar automaticamente uma reserva de teste e exibir o valor total calculado.

Autor

Guilherme Guimarães Audibert
Ciência da Computação – 3º Semestre