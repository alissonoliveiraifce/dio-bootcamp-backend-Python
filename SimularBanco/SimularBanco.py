#Desafio Backend Python DIO
#Autor: Alisson Oliveira
#Descrição: Simular um sistema de banco com operações de saque, depósito e saldo. 
#Versão: 1.0

menu = """
    ### Banco DIO ###

    Digite o número da operação desejada:
    1 - Saldo
    2 - Depósito
    3 - Saque
    4 - Extrato
    5 - Sair
    
"""

saldo = 0
limite_por_saque = 500
LIMITE_DE_SAQUE = 3
numero_de_saques_do_dia = 0
numero_de_depositos_do_dia = 0

while True:
    print(menu)
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print(f"\nSeu saldo é de R${saldo:.2f}")
    
    elif opcao == '2':
        deposito = float(input("\nDigite o valor do depósito: R$"))
        saldo += deposito
        numero_de_depositos_do_dia += 1
        print(f"\nDepósito de R${deposito:.2f} efetuado com sucesso!")
        print(f"Saldo atual: R${saldo:.2f}")
    
    elif opcao == '3':
        if numero_de_saques_do_dia >= LIMITE_DE_SAQUE:
            print("\nLimite de saques diários atingido!")
            continue
        elif numero_de_saques_do_dia <= LIMITE_DE_SAQUE:
            saque = float(input("\nDigite o valor do saque: R$"))
            if saldo >= saque and saque <= limite_por_saque:
                saldo -= saque
                numero_de_saques_do_dia += 1
                print(f"\nSaque de R${saque:.2f} efetuado com sucesso!")
                print(f"Saldo atual: R${saldo:.2f}")
            elif saque > limite_por_saque:
                print(f"\nLimite de saque por operação é de R${limite_por_saque:.2f}!")
            else:
                print("\nSaldo insuficiente!")
                print(f"Saldo atual: R${saldo:.2f}")
    
    elif opcao == '4':
        print("\n--------- Extrato bancário: ---------")
        print(f"Saldo: R${saldo:.2f}")
        print(f"Limite por saque: R${limite_por_saque:.2f}")
        print(f"Limite de saques diários: {LIMITE_DE_SAQUE}")
        print(f"Saques realizados hoje: {numero_de_saques_do_dia} | Saques restantes: {LIMITE_DE_SAQUE - numero_de_saques_do_dia}")
        print(f"Depósitos realizados hoje: {numero_de_depositos_do_dia}")
        print("-" * 35 + "\n")        
    
    elif opcao == '5':
        print("\nSaindo do sistema...")
        print("Obrigado por utilizar o Banco DIO!\n")
        break
    
    else:
        print("\nOpção inválida!")
