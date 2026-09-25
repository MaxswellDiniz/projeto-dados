# Validador de Chamados

Este projeto tem como objetivo principal **validar chamados fictícios** de um sistema de suporte, garantindo que os dados inseridos sigam as regras de negócio esperadas antes de serem processados.

## Pré-requisitos

O projeto foi desenvolvido e validado utilizando a seguinte versão do ambiente:
* **Python 3.12.3**

## Como Executar

Para executar o script de validação, abra o seu terminal na raiz do projeto e utilize o comando abaixo:

```bash
python3 src/validador_chamados.py
```

## Testes Realizados

A suíte de testes do script cobre os seguintes cenários fundamentais:

* **Caso Válido:** Verifica se o sistema processa corretamente um chamado que possui todos os campos preenchidos e válidos.
* **Caso Pendente:** Valida o comportamento do script ao lidar com chamados que estão aguardando alguma ação ou aprovação.
* **Caso Vazio:** Garante que o sistema trate erros adequadamente e exiba alertas quando um chamado for enviado sem nenhuma informação.
