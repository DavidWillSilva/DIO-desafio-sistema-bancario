menu = ''' 
MENU

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0.00
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("\nDeposito\n")
        valor_deposito = float(input("Informe o valor do deposito: "))
        if valor_deposito < 0:
            print("Depositar apenas valor positivo.")
        else:
            saldo += valor_deposito
            extrato += "Deposito de +R$ {:.2f}\n".format(valor_deposito)
            print("DEPOSITO REALIZADO COM SUCESSO!")

    elif opcao == "s":
        print("\nSaque\n")
        valor_saque = float(input("Informe o valor que deseja Sacar: "))
        if numero_saques < LIMITE_SAQUES:          
            if valor_saque > limite:
                print("Valor limite excedido!")

            elif valor_saque > saldo:
                print("Saldo Insuficiente!")

            elif valor_saque < 0:
                print("Saque apenas com valores positivos.")

            else:
                numero_saques += 1
                saldo -= valor_saque
                extrato += "Saque de -R$ {:.2f}\n".format(valor_saque)
                print("SAQUE REALIZADO COM SUCESSO!")

        else:
            print("Limite de Saque excedido!")
     

    elif opcao == "e":
        print("\nExtrato\n")
        print(extrato)
        print(f"Seu Saldo Total é de R$ {saldo:.2f}")
        

    elif opcao == "q":
        print("\nSaindo...")
        print("\nObrigado por ser nosso Cliente!")
        break

    else:
        print("Operação inválida, por favor selecione a opção desejada.")