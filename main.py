from funcoes import saque

print("DEPÓSITO: [d]\nSAQUE:    [s]\nEXTRATO:  [e]\nSAIR:     [q]")
saldo = 1000

while True:

    opcao = input("Escolha uma das opções acima: ")[0].lower()

    match opcao:
        case "d":
            print("Depósito")

        case "s":
            print("Saque")
            print(saque(saldo))

        case "e":
            print("Extrato")

        case "q":
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida. Tente novamente.")
