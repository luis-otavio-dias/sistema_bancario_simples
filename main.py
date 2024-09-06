from funcoes import saque, funcao_saldo, extrato

print("DEPÓSITO: [d]\nSAQUE:    [s]\nEXTRATO:  [e]\nSAIR:     [q]")
saldo = funcao_saldo(saldo=0)  # por padrão 0

while True:

    opcao = input("Escolha uma das opções acima: ")[0].lower()

    match opcao:
        case "d":
            print()
            print("DEPÓSITO")
            saldo = float(input("Digite o valor à ser depositado: R$"))
            funcao_saldo(saldo)
            print()

        case "s":
            print()
            print("SAQUE")
            print("Valor de máximo de saque: R$500.00")
            print()
            saldo = funcao_saldo(saque(saldo))

        case "e":
            print()
            print("EXTRATO")
            extrato()

        case "q":
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida. Tente novamente.")
