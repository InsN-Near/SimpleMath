import sympy as sp

def metodo_newton_raphson(funcao_str, chute_inicial, tol=1e-5, iter_max=5):
    """
    Implementa o Método de Newton-Raphson para encontrar raízes de uma função.

    Argumentos:
        funcao_str: Representação da função como texto (ex.: "x**3 - 2*x - 5")
        chute_inicial: Adivinha inicial para a raiz
        tol: Tolerância para convergência (padrão: 1e-5)
        iter_max: Número máximo de iterações (padrão: 5)

    Retorna:
        A raiz aproximada da função, ou None se não convergir.
    """

    x = sp.Symbol('x')  # Cria uma variável simbólica para cálculos
    f = sp.sympify(funcao_str)  # Converte a string em uma expressão SymPy
    df = sp.diff(f, x)     # Calcula a derivada

    for n in range(iter_max):
        fx = f.subs(x, chute_inicial)
        dfx = df.subs(x, chute_inicial)

        if abs(fx) < tol:
            return chute_inicial
        if dfx == 0:
            raise ValueError("Derivada é zero em x={}".format(chute_inicial))

        chute_inicial = chute_inicial - fx / dfx

        print("Iteração {}: x = {:.6f}".format(n + 1, chute_inicial))

    print("Falhou em convergir em {} iterações".format(iter_max))
    return None

# Exemplo de uso
funcao_texto = "x**3 - 2*x - 5"
chute_inicial = 2.0

raiz = metodo_newton_raphson(funcao_texto, chute_inicial)

if raiz is not None:
    print("Raiz aproximada encontrada:", raiz)
