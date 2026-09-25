"""
Resumo: Valida o status de chamados sintéticos de TI.
Objetivo: Demonstrar uso de variáveis, strings, condicionais e funções.
"""

def validar_status(status_informado):
    """Verifica se o status informado é aceito pelo sistema de chamado."""
    # Lista de status válidos (nossa regra de negócio)
    status_permitidos = ["aberto", "em andamento", "fechado"]

    # Convertendo os dados para minúsculo para evitar erros de digitação.
    status_limpo = status_informado.lower()

    if status_limpo in status_permitidos:
        print(f"OK O status {status_informado} é VÁLIDO.")
    else:
        print(f"ERRO o Status {status_informado} é INVÁLIDO.")

def main():
    """Função principal que coordena a execução do Script."""
    print("---- Iniciando traiagem de Chamados ----")

    # Simulando dados sintéticos que vieram de uma planilha ou sistema.
    chamado_1 = "Aberto"
    chamado_2 = "Pendente" #Caso negativo (Não existir em noss regra)
    chamado_3 = ""         #Caso de borda (Vazio)

    # Executando a validação
    validar_status(chamado_1)
    validar_status(chamado_2)
    validar_status(chamado_3)

if __name__== "__main__":
    main()