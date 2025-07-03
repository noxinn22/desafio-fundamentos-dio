menu = """
========== Menu ==========

        Bem vindo ao banco Itaú!
        _________________________
        
       Selecione a opção desejada:

[d]- Deposito
[s]- Saque
[e]- Extrato
[x]- Sair

=>: """

saldo = 0
LIMITE_SAQUE = 3
numero_saques = 0
limite_valor_saque = 500
extrato = ""


while True:
   
    opcao = input (menu)
    if opcao == "d":
        valor = float(input("Insira o valor que deseja depositar:"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("valor invalido")
            
         
    opcao = input (menu)
    if opcao == "s":
        
        valor = float(input("Insira o valor que deseja sacar:"))
                     
        excedeu_saques = numero_saques >= LIMITE_SAQUE
        
        excedeu_limite = valor > limite_valor_saque
        
        excedeu_saldo = valor > saldo
        
        if excedeu_saques:
            print ("A operação falhou, o limite de saques foi excedido.")
            
        if excedeu_limite:
            print ("A operação falhou, o valor ultrapassou o limite diario de saques.")
            
        if excedeu_saldo:
            print("A operação falhou, você não tem saldo suficiente.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de: R$ {valor:.2f}\n"
            numero_saques +1
            
        else:
            print("A operação falhou! O valor informado é inválido.")
            
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "x":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
