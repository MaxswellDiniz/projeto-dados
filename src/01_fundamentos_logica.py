# ============================================================
# PROJETO: FUNDAMENTOS DE PYTHON - AULA 01
# ARQUIVO: src/01_fundamentos_logica.py
# OBJETIVO: Variáveis, Tipos, Type Casting e Operadores
# ============================================================

# 1. Entrada de dados Brutos (Dados simulados em formato de texto/String)

id_servidor = "SRV-01"
capacidade_disco_gb_texto = "500.00"
espaco_ocupado_disco_texto = "420.00"
limite_alerta_porcentagem_fload = 80.0

# 2. conversão de tipo (type)
capacidade_disco = float(capacidade_disco_gb_texto)
espaco_ocupado = float(espaco_ocupado_disco_texto)

# 3. Operadores matemáticos de memória 

espaco_livre = capacidade_disco - espaco_ocupado
porcentagem_usado = (espaco_ocupado / capacidade_disco) * 100.0

# 4. Operadores de comparação 

espaco_critico = porcentagem_usado >= limite_alerta_porcentagem_fload

# 5. EXIBIÇÃO DOS RESULTADOS FORMATADOS

print("--- Diagnóstico do Servidor ---")

print(f"identificação do Id da Máquina: {id_servidor}")
print(f"A capacidade atual do disco é de: {capacidade_disco}")
print(f"Espaço ocupado no disco: {espaco_ocupado}")
print(f"Ainda resta de espaço disponível: {espaco_livre}")
print(f"--- Alerta de Status: {espaco_critico}")