def encryptar(mensagem, chave):
  """Criptografa uma mensagem usando a criptografia baseada em N com uma chave.

  Args:
      mensagem: A mensagem para criptografar (string).
      chave: A chave de criptografia como uma sequência de 6 números (lista de inteiros).

  Returns:
      A mensagem criptografada (string).
  """
  alfabeto = 'abcdefghijklmnopqrstuvwxyz'
  nova_mensagem = ''
  for caracter in mensagem:
    if caracter.isalpha():
      nova_posição = (alfabeto.index(caracter.lower()) + sum(chave)) % 26
      nova_letra = alfabeto[nova_posição]
      nova_mensagem += nova_letra.upper() if caracter.isupper() else nova_letra
    else:
      nova_mensagem += caracter
  return nova_mensagem

def descriptografar(mensagem_criptografada, chave):
  """Descriptografa uma mensagem criptografada com a criptografia baseada em uma chave.

  Args:
      mensagem_criptografada: A mensagem criptografada para descriptografar (string).
      chave: A chave de criptografia usada para criptografar a mensagem (lista de inteiros).

  Returns:
      A mensagem descriptografada (string).
  """
  return encryptar(mensagem_criptografada, [-i for i in chave])  # Descriptografia usa chave negativa

def principal():
  """Fornece o menu interativo para criptografia e descriptografia."""
  while True:
    print("Escolha uma opção:")
    print("1. Criptografar")
    print("2. Descriptografar (Traduzir)")
    print("3. Sair")
    escolha = input("Digite sua escolha: ")

    if escolha == '1':
      mensagem = input("Digite a mensagem para criptografar: ")
      chave = [int(x) for x in input("Digite a chave de criptografia (6 números): ").split()]
      if len(chave) != 6:
        print("Comprimento de chave inválido. A chave deve ter 6 números.")
        continue
      mensagem_criptografada = encryptar(mensagem, chave)
      print("Mensagem criptografada:", mensagem_criptografada)

    elif escolha == '2':
      mensagem_criptografada = input("Digite a mensagem criptografada: ")
      chave = [int(x) for x in input("Digite a chave de descriptografia (6 números): ").split()]
      if len(chave) != 6:
        print("Comprimento de chave inválido. A chave deve ter 6 números.")
        continue
      mensagem_descriptografada = descriptografar(mensagem_criptografada, chave)
      print("Mensagem descriptografada:", mensagem_descriptografada)

    elif escolha == '3':
      print("Saindo...")
      break

    else:
      print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
  principal()
