#Questão 3, 4, 5

from itertools import product

# Implementação Força Bruta
def mochila_forca_bruta(valores, pesos, capacidade):
    n = len(valores)
    melhor_valor = 0
    iteracoes = 0

    for combinacao in product([0, 1], repeat=n):
        iteracoes += 1
        peso_total = sum(p * c for p, c in zip(pesos, combinacao))
        valor_total = sum(v * c for v, c in zip(valores, combinacao))

        if peso_total <= capacidade and valor_total > melhor_valor:
            melhor_valor = valor_total

    return melhor_valor, iteracoes

# Implementação Programação Dinâmica
def mochila_pd(N, C, itens):
    maxTab = [[0 for _ in range(C + 1)] for _ in range(N + 1)]
    iteracoes = 0

    for i in range(1, N + 1):
        for j in range(1, C + 1):
            iteracoes += 1
            if itens[i][0] <= j:
                maxTab[i][j] = max(maxTab[i - 1][j], itens[i][1] + maxTab[i - 1][j - itens[i][0]])
            else:
                maxTab[i][j] = maxTab[i - 1][j]

    return maxTab[N][C], iteracoes

# Testes com casos do Moodle
if __name__ == "__main__":
    casos = [
        {"capacidade": 165,
         "pesos": [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
         "valores": [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]},

        {"capacidade": 190,
         "pesos": [56, 59, 80, 64, 75, 17],
         "valores": [50, 50, 64, 46, 50, 5]}
    ]

    for idx, caso in enumerate(casos, 1):
        itens = [(0, 0)] + list(zip(caso["pesos"], caso["valores"]))

        melhor_valor_fb, iteracoes_fb = mochila_forca_bruta(caso["valores"], caso["pesos"], caso["capacidade"])
        melhor_valor_pd, iteracoes_pd = mochila_pd(len(caso["pesos"]), caso["capacidade"], itens)

        print(f"\nCaso de teste {idx}:")
        print(f"Força Bruta - Valor: {melhor_valor_fb}, Iterações: {iteracoes_fb}")
        print(f"Prog. Dinâmica - Valor: {melhor_valor_pd}, Iterações: {iteracoes_pd}")