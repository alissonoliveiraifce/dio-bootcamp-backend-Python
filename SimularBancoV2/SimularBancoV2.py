#Desafio Backend Python DIO
#Autor: Alisson Oliveira
#Descrição: Simular um sistema de banco com operações de saque, depósito e saldo. 
#Versão: 2.0
import random

def menu(): 
    print("""
    #################### DIO BANK ####################

    Digite o número da operação desejada:
    1 - Saldo                       2 - Depósito
    3 - Saque                       4 - Extrato
    5 - Novo cliente                6 - Nova conta
    7 - Listar contas               8 - Sair
    """)
    opcao = input("Escolha uma opção: ")
    return opcao

def consultar_saldo(saldo):
    print(f"\nSeu saldo é de R${saldo:.2f}")
    
def realizar_deposito(saldo):
    deposito = float(input("\nDigite o valor do depósito: R$"))
    saldo += deposito
    print(f"\nDepósito de R${deposito:.2f} efetuado com sucesso!")
    print(f"Saldo atual: R${saldo:.2f}")
    return saldo

def realizar_saque(saldo, limite_por_saque, numero_de_saques_do_dia, LIMITE_DE_SAQUE):
    if numero_de_saques_do_dia >= LIMITE_DE_SAQUE:
        print("\nLimite de saques diários atingido!")
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
    return saldo, numero_de_saques_do_dia

def extrato_bancario(saldo, limite_por_saque, LIMITE_DE_SAQUE, numero_de_saques_do_dia, numero_de_depositos_do_dia, contas):
    print("\n--------- Extrato bancário: ---------")
    print(f"Saldo: R${saldo:.2f}")
    print(f"Limite por saque: R${limite_por_saque:.2f}")
    print(f"Limite de saques diários: {LIMITE_DE_SAQUE}")
    print(f"Saques realizados hoje: {numero_de_saques_do_dia} | Saques restantes: {LIMITE_DE_SAQUE - numero_de_saques_do_dia}")
    print(f"Depósitos realizados hoje: {numero_de_depositos_do_dia}")
    print("-" * 35 + "\n")
    
def novo_cliente(clientes):
    #validar se cliente já existe
    cpf = input("Digite o CPF do cliente: ")
    for cliente in clientes:
        if cliente["cpf"] == cpf: 
            print("\nCliente já cadastrado!")
            return clientes
    
    #continuar cadastro após validacao
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    clientes.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("\nCliente cadastrado com sucesso!")
    return clientes
    
    
def nova_conta(agencia, clientes):
    cpf = input("Digite o CPF do cliente: ")
    validacao = False
    for cliente in clientes:
        if  cliente["cpf"] == cpf:
            validacao = True
            break
            
    if validacao: 
        numero_conta = random.randint(1000, 9999)
        conta = {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente["nome"]}
        print(f"\nConta criada com sucesso!\nAgência: {agencia} | Número da conta: {numero_conta} | Cliente: {cliente['nome']}")
        return conta
    else:
        return print("\nCliente inexistente!")
            
                
    
def listar_contas(contas):
    print("\n--------- Lista de contas: ---------")
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Número da conta: {conta['numero_conta']} | Cliente: {conta['cliente']}")

def main ():
    saldo = 0
    limite_por_saque = 500
    LIMITE_DE_SAQUE = 3
    numero_de_saques_do_dia = 0
    numero_de_depositos_do_dia = 0
    clientes = []
    contas = []
    AGENCIA = "0001"
    
    while True:
        opcao = menu()

        if opcao == '1':
            consultar_saldo(saldo)
    
        elif opcao == '2':
            saldo = realizar_deposito(saldo)
            numero_de_depositos_do_dia += 1
    
        elif opcao == '3':
            saldo, numero_de_saques_do_dia = realizar_saque(saldo, limite_por_saque, numero_de_saques_do_dia, LIMITE_DE_SAQUE)
            
        elif opcao == '4':
            extrato_bancario(saldo, limite_por_saque, LIMITE_DE_SAQUE, numero_de_saques_do_dia, numero_de_depositos_do_dia, contas)    
    
        elif opcao == '5':
            novo_cliente(clientes)
                        
        elif opcao == '6':
            conta = nova_conta(AGENCIA, clientes)
            contas.append(conta)
        
        elif opcao == '7':
            listar_contas(contas)
        
        elif opcao == '8':
            print("\nSaindo do sistema...")
            print("Obrigado por utilizar o Banco DIO!\n")
            break
        
        #Opção secreta para testes
        elif opcao == "9":
            print("\nClientes cadastrados: ")
            print(clientes)
            print("\nContas cadastradas: ")
            print(contas)
    
        else:
            print("\nOpção inválida!")
            print(clientes)

main()
