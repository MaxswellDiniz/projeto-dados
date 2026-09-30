# =====================================================
# PROJETO: FUNDAMENTOS DE PAYTHON  - AULA 01.5
# ARQUIVO: src\01_calculos_aritmeticos.py
# objetivo: Domínio de operadores aritiméticos e Números
# ======================================================

def main():
    print("=" * 65)
    print("         HAMBURGUERIA SECOPS - SIMULADOR DE CÁLCULO DE CAIA")
    print("=" * 65)

# ENTRADAS DE DADOS E COERÇÃO DE TIPOS:

    nome_cliente = input("Nome do cliente: ")
    idade_cliente = int(input("Idade do cliente: "))
    valor_pedido = float(input("Valor total do pedido (R$): "))
    incluir_bebida_alcoolica = input("Incluir cerveja/Bebida Alcoólica? (s/n): ")

# TAXA FIXA DE ENTREGA PADRÃO:

    taxa_entrega = 10.0
    print("\n--- PROCESSANDO REGRAS DE NEGÓCIOS ---")

# ESTRUTURA CONDICIONAL 1: Validação de bebida Alcoólicas (Segurança/lei)

    if incluir_bebida_alcoolica and idade_cliente < 18:
        print(f"❌ ALERTA DE SEGURANÇA: Venda de bebida alcoólica proíbida para menores de 18 anos!")
        print(f"Bebida será removida do pedido.")
    elif incluir_bebida_alcoolica and idade_cliente >= 18:
        print(f"✅ Bebida liberada com sucesso!")
    else:
        print(f"🔲Pedido sem bebida Alcoólica")
        
# ESTRUTURA CONDICIONAL 2: Regra de free grátis ou desconto
# PEDIDO ACIMA DE 100 REAIS TEM ENTREGA GRÁTIS!

    if valor_pedido >= 100.00:
        taxa_entrega = 0.0
        print(f"🎉 PARABÉNS! Seu pedido atingiu entrega grátis acima de 100 reais!")
    elif valor_pedido >= 60.0 and valor_pedido < 100.00:
        taxa_entrega = 5.0
        print(f"🚚 Você ganhou 50% de DESCONTO NA TAXA DE ENTREGA (R$5.00).")
    else:
        print(f"📦️ Taxa de entrega padrão aplicada: {taxa_entrega}")

# CÁLCULO DO VALOR FINAL COM ENTREGA:    

    valor_total = valor_pedido + taxa_entrega

    print("\n" + "-" * 60)
    print("                  RESUMO DO PEDIDO")
    print("-" * 60)
    print(f"Cliente        :{nome_cliente}")
    print(f"Subtotal Pedido:{valor_pedido:.2f}")
    print(f"Taxa de Entrega:{taxa_entrega:.2f}")
    print(f"VALOR TOTAL    :{valor_total:.2f}")
    print("-" * 60)

if __name__ == "__main__":
    main()
