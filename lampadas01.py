# Interação com o usuário para obter os dados de entrada

print("--- Entrada de Dados do Cômodo ---")
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))
potencia_da_lampada = float(input("Digite a potência da lâmpada utilizada (em watts): "))   


if largura <= 0 or comprimento <= 0 or potencia_da_lampada <= 0:
        print("\n[Erro]: Por favor, insira apenas valores maiores que zero.")
else:
 # 1. Calcular a área do cômodo
    area = largura * comprimento

    # 2. Calcular a potência total necessária (3 watts por metro quadrado)
    potencia_total_necessaria = area * 3

    # 3. Calcular o número de lâmpadas necessárias (arredondando para cima)
    numero_lampadas = (potencia_total_necessaria // potencia_da_lampada)

    # 4. Calcular a quantidade de bocais disponíveis baseados na área (1 bocal a cada 3m²)
    numero_bocais = (area / 3)

    print(f"\n=== Relatório de Iluminação ===")
    print(f"Dimensões do cômodo: {largura:.2f}m x {comprimento:.2f}m")
    print(f"Área total: {area:.2f} m²")
    print(f"Potência total necessária: {potencia_total_necessaria:.2f} W")
    print(f"Potência da lâmpada adotada: {potencia_da_lampada:.2f} W")
    print(f"Número de lâmpadas recomendadas: {numero_lampadas}")
    print(f"Limite físico de bocais instaláveis (1 a cada 3m²): {numero_bocais}")

    if numero_lampadas > numero_bocais:
        print("\n[Atenção]: O número de lâmpadas necessárias excede o limite físico recomendado de bocais para este tamanho de cômodo!")
        
    