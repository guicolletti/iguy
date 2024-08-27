saldo = 1000

resposta = input("Olá, sou seu Banco Pessoal, o que deseja fazer?\n"
      "1 - Sacar\n"
      "2 - Depositar\n"
      "3 - Consultar Saldo\n"
      "4 - Fechar Banco Pessoal")

if resposta == "1":
    print("---Saque---")
    valor_saque = input("Qual o valor que você deseja sacar? ")
    if valor_saque > saldo:
        print("Saldo insuficiente")

if resposta == "2":
    print("---Despositar---")
    valor_deposito = input("Qual o valor que você deseja depositar? ")
    if valor_deposito > saldo:
        print("Saldo insuficiente")

if resposta == "3":
    print(f"Seu saldo atual é de R${saldo} reais.")

if resposta == "4":