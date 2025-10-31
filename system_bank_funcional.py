import textwrap

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                valor=valor,
                limite=limite,
                numero_saques=numero_saques,
                limites_saques=LIMITE_SAQUES
            )
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            create_user(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = create_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                print(f"Conta criada com sucesso!! AG: {conta["agencia"]} CONTA: {conta["numero_conta"]}")
        
        elif opcao == "lc":
            list_contas(contas)
            
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")  

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo_usuário
    [nc]\tCria uma nova Conta
    [lc]\tLista Contas
    => """
    return input(textwrap.dedent(menu))
    
def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Operação OK! Depósito de {valor:.2f} realizado.")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limites_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limites_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nOperação OK! saque de {valor:.2f} realizado.")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
        print("Seu Extrato:")    
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def create_user(usuarios):
    print("\n================ Novo  Usuário ================")  
    cpf = input("Informe o CPF (somente número): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = filtra_cpf(cpf, usuarios)

    if usuario:      
        print("Ops!! usuário já existe")
        return
    
    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco":endereco
        })
    print(f'\n Cadastrado com sucesso!! \n CPF: {cpf} \n NOME: {nome}')
    
def filtra_cpf(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return cpf
        return None

def create_conta(agencia, numero_conta, usuarios):
    print("\n================ Nova CONTA ================")  
    cpf = input("Informe o CPF (somente número): ")
    user = filtra_cpf(cpf, usuarios)

    if user:
        return {"agencia": agencia, "numero_conta": numero_conta, "cpf": cpf}
    
    print(f"Usuário não existe!!!")
    
def list_contas(contas):
    for conta in contas:
        linha = f'''
            AGENCIA: {conta["agencia"]}
            NUMERO_CONTA: {conta["numero_conta"]} 
            CPF: {conta["cpf"]}
        '''
        print("=" * 100)
        print(textwrap.dedent(linha))

main()





