def executar_instrucoes(tamanho_Memoria, instrucoes):
    # Inicializa a memória com zeros
    memoria = [0] * (tamanho_Memoria + 1)  # índice de 1 a N

    for instrucao in instrucoes:
        tipo = instrucao[0]

        if tipo == 1:  # FRENTE posicao valor
            posicao, valor = instrucao[1], instrucao[2]
            incremento = valor
            i = posicao
            while i <= tamanho_Memoria and incremento > 0:
                memoria[i] += incremento
                incremento -= 1
                i += 1

        elif tipo == 2:  # TRÁS posicao valor
            posicao, valor = instrucao[1], instrucao[2]
            incremento = valor
            i = posicao
            while i >= 1 and incremento > 0:
                memoria[i] += incremento
                incremento -= 1
                i -= 1

        elif tipo == 3:  # IMPRIME posicao
            posicao = instrucao[1]
            print(memoria[posicao])


# -------------------------------
# Exemplo de uso:
tamanho_Memoria = 16
instrucoes = [
    (1, 4, 8),   # FRENTE 4 8
    (2, 16, 3),  # TRÁS 16 3
    (2, 2, 12),  # TRÁS 2 12
    (1, 8, 7),   # FRENTE 8 7
    (3, 4),      # IMPRIME 4
    (3, 14),     # IMPRIME 14
    (3, 1)       # IMPRIME 1
]

executar_instrucoes(tamanho_Memoria, instrucoes)
