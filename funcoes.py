contador = 0  # variável global para controlar o limite de 3 saques diários
extrato_deposito = []
extrato_saque = []
saldo_atual = 0


def funcao_saldo(saldo):
    global extrato_deposito
    if saldo != 0:
        extrato_deposito.append(saldo)
    if saldo_atual in extrato_deposito:
        extrato_deposito.remove(saldo_atual)
    return saldo


def saque(saldo):
    global extrato_saque
    global contador
    global saldo_atual

    contador += 1
    saldo_saque = saldo

    if contador > 3:
        print("Limite de saques diários atingido. Tente novamente após 24 horas.")
    else:

        while True:

            valor_saque = float(input("Digite o valor à ser sacado: "))

            if valor_saque <= 0 or valor_saque > 500:
                print("Valor inválido. Tente novamente.")

            elif valor_saque > saldo_saque:
                print(
                    f"Impossível sacar o valor desejado. Saldo atual: {saldo_saque:.2f}"
                )
                # depois vejo isso
                break

            else:
                extrato_saque.append(valor_saque)
                saldo_saque -= valor_saque
                print(f"Saque de R${valor_saque:.2f} aprovado.")
                print()
                saldo_atual = saldo_saque
                return saldo_saque


def extrato():
    print(f"SALDO ATUAL: R${saldo_atual:.2f}")
    print()
    print("SAQUES: ")
    for contador in range(len(extrato_saque)):
        print(f"R${extrato_saque[contador]:.2f}\n")
    print()
    print("DEPÓSITOS: ")
    for contador in range(len(extrato_deposito)):
        print(f"R${extrato_deposito[contador]:.2f}\n")
