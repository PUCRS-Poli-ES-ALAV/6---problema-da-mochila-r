# Questões 1,2

import sys
sys.setrecursionlimit(20000)

# Fibonacci Recursivo
def fibo_rec(n, contagem):
    contagem['chamadas'] += 1
    if n <= 1:
        return n
    return fibo_rec(n - 1, contagem) + fibo_rec(n - 2, contagem)


# Fibonacci Iterativo usando Programação Dinâmica
def fibo_iter(n, contagem):
    f = [0] * (n + 1)
    f[0], f[1] = 0, 1
    for i in range(2, n + 1):
        contagem['iteracoes'] += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


# Fibonacci com Memoização
def memoized_fibo(n, contagem, f=None):
    if f is None:
        f = [-1] * (n + 1)

    contagem['chamadas'] += 1

    if f[n] >= 0:
        return f[n]

    if n <= 1:
        f[n] = n
    else:
        f[n] = memoized_fibo(n - 1, contagem, f) + memoized_fibo(n - 2, contagem, f)

    return f[n]


# Exemplo de uso com contagem de operações
if __name__ == "__main__":
    import pandas as pd

    valores_teste = [4, 8, 16, 32, 128, 1000]
    resultados = []

    for valor in valores_teste:
        linha = {'n': valor}

        if valor <= 32:
            contagem_rec = {'chamadas': 0}
            resultado_rec = fibo_rec(valor, contagem_rec)
            linha['FIBO-REC (resultado)'] = resultado_rec
            linha['FIBO-REC (chamadas)'] = contagem_rec['chamadas']

        contagem_iter = {'iteracoes': 0}
        resultado_iter = fibo_iter(valor, contagem_iter)
        linha['FIBO (resultado)'] = resultado_iter
        linha['FIBO (iterações)'] = contagem_iter['iteracoes']

        contagem_memo = {'chamadas': 0}
        resultado_memo = memoized_fibo(valor, contagem_memo)
        linha['MEMOIZED-FIBO (resultado)'] = resultado_memo
        linha['MEMOIZED-FIBO (chamadas)'] = contagem_memo['chamadas']

        resultados.append(linha)

    df_resultados = pd.DataFrame(resultados)
    print(df_resultados)
