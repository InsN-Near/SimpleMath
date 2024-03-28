import numpy as np

def descida_gradiente(f, grad_f, x0, taxa_aprendizado=0.01, tol=1e-5, max_iter=1000):
    """
    Implementa o algoritmo de Descida do Gradiente para encontrar o mínimo de uma função.

    Args:
        f: A função a ser minimizada.
        grad_f: O gradiente da função.
        x0: Palpite inicial para o mínimo.
        taxa_aprendizado: O tamanho do passo realizado em cada iteração.
        tol: Tolerância para convergência.
        max_iter: Número máximo de iterações.

    Retorna:
        O ponto mínimo aproximado da função.
    """

    x = x0
    for i in range(max_iter):
        gradiente = grad_f(x)  
        x = x - taxa_aprendizado * gradiente

        if np.linalg.norm(gradiente) < tol:
            return x

    print("Falha ao convergir dentro de {} iterações.".format(max_iter)) 
    return x

# Exemplo de uso: Minimizar a função f(x) = x^2 + 2x + 1
def f(x):
    return x**2 + 2*x + 1

def grad_f(x):
    return 2*x + 2

palpite_inicial = -5
resultado = descida_gradiente(f, grad_f, palpite_inicial)
print("Mínimo aproximado encontrado em x = ", resultado)
