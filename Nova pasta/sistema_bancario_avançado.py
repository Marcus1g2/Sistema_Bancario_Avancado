def menu():
    menu = """
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair
     """
    return int(input(menu))


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(valor)
        print(f"Tem disponível agora: R$ {saldo:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        numero_saques += 1
        if valor <= saldo:
            saldo -= valor
            extrato.append(-valor)
            print("Saque realizado com sucesso!")
        else:
            print("Erro, valor não disponível. Por favor, consulte seu saldo!")
    else:
        print("Quantidade de saques excedidas")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================\n")

    saldo_acumulado = 0
    for pExtrato in extrato:
        saldo_acumulado += pExtrato
        if pExtrato > 0:
            print(f"Depósito: R$ {pExtrato:.2f}")
        else:
            print(f"Saque: R$ {abs(pExtrato):.2f}")

    print(f"\nSaldo atual: R$ {saldo_acumulado:.2f}")
    print("==========================================")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = int(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = int(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 6:
            cpf = int(input("Informe o CPF (somente número): "))
            if any(usuario['cpf'] == cpf for usuario in usuarios): #any retorna true se for verdadeira  condição
                print("\nJá existe usuário com esse CPF!")
            else:
                nome = input("Informe o nome completo: ")
                data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
                endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

                usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
                print("=== Usuário criado com sucesso! ===")

        elif opcao == 4:
            numero_conta = len(contas) + 1 #Aqui, len(contas) retorna o número de elementos (contas bancárias) na lista contas, e o código adiciona 1 para gerar um número de conta único.
            cpf = int(input("Informe o CPF do usuário: "))
            usuario = next((u for u in usuarios if u["cpf"] == cpf), None)  # u antes do for variavel temporaria
            #None é um valor especial em Python que representa a ausência de valor ou a falta de um valor válido. No seu código, está sendo usado como um valor padrão retornado pela função

            if usuario:
                print("\n=== Conta criada com sucesso! ===")
                contas.append({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario})
            else:
                print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

        elif opcao == 5:
            for conta in contas:
                print("=" * 100)
                print(f"Agência:\t{conta['agencia']}\nC/C:\t\t{conta['numero_conta']}\nTitular:\t{conta['usuario']['nome']}")

        elif opcao == 7:
            break

        else:
            print("Operação inválida, por favor, selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
