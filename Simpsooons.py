import numpy as np

def simpson(f, a, b, n):
    """
    Aproxima a integral definida de uma função f ao longo do intervalo [a, b]
    usando a Regra de Simpson.

    Argumentos:
        f: A função a ser integrada (deve aceitar variáveis simbólicas).
        a: Limite inferior da integração.
        b: Limite superior da integração.
        n: O número de subintervalos (deve ser par).

    Retorna:
        Uma tupla contendo:
            - O valor aproximado da integral.
            - Uma estimativa do limite do erro, potencialmente definindo a estimativa como zero se zeros simbólicos forem encontrados.
    """

    if n % 2 != 0:
        raise ValueError("n deve ser um número par.")

    h = (b - a) / n  # Largura do subintervalo
    x = np.linspace(a, b, n + 1)  # Vetor de pontos
    y = f(x)

    integral = h/3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

    # Estimativa de erro com tratamento para zeros
    import sympy as sp
    x_sim = sp.Symbol('x')
    estimativa_erro = (b - a) * h**4 / 180  * abs(sp.diff(f(x_sim), x_sim, 4)) 
    for expressao in estimativa_erro.args:  # Loop para lidar com zeros simbólicos
        if isinstance(expressao, sp.Zero): 
            estimativa_erro = 0  # Define a estimativa de erro como zero se a derivada contiver zero
            break

    return integral, estimativa_erro

# Exemplo de uso: Aproximar a integral de x^2 de 0 a 2 usando 6 intervalos
def f(x):
    return x**2

a = 0.0
b = 2.0
n = 6

integral_aproximada, estimativa_erro = simpson(f, a, b, n)
print("Integral aproximada:", integral_aproximada)
print("Estimativa de erro:", estimativa_erro)
