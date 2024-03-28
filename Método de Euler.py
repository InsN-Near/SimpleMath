import numpy as np

def metodo_euler(f, y0, intervalo_t, n):
  """
  Resolve uma equação diferencial dy/dt = f(t, y) usando o Método de Euler.

  Args:
      f: Uma função que recebe o tempo atual (t) e o estado (y) como argumentos
          e retorna a derivada dy/dt.
      y0: O valor inicial do estado (y) no tempo inicial.
      intervalo_t: Uma tupla (t_inicio, t_fim) representando o intervalo de tempo para a solução.
      n: O número de passos a serem usados na aproximação de Euler.

  Returns:
      Uma tupla contendo os pontos de tempo (t) e as soluções aproximadas correspondentes (y).
  """

  t_inicio, t_fim = intervalo_t
  t = np.linspace(t_inicio, t_fim, n + 1)  # Vetor de pontos de tempo
  y = np.zeros(n + 1)  # Vetor para armazenar os valores da solução
  y[0] = y0

  # Iterações do Método de Euler
  for i in range(1, n + 1):
    dt = t[i] - t[i - 1]
    y[i] = y[i - 1] + dt * f(t[i - 1], y[i - 1])

  return t, y

# Exemplo de uso: Resolver dy/dt = t + y, y(0) = 1, t = [0, 2] com 10 passos
def f(t, y):
  return t + y

y0 = 1.0
intervalo_t = (0.0, 2.0)
n = 10

t, y = metodo_euler(f, y0, intervalo_t, n)

# Imprime a solução
print("Tempo:", t)
print("Solução (y):", y)
