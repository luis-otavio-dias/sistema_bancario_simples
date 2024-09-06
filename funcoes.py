def saque(saldo):
    saldo_atual = saldo
    contador = 0
    while True:

        valor_saque = int(input("Digite o valor à ser sacado: "))
        saldo_atual -= valor_saque

        if contador == 3:
            print("Limite de saques diários atingido. Tente novamente após 24 horas.")
            break

        if valor_saque <= 0 or valor_saque > 500:
            saldo_atual += valor_saque
            print("Valor inválido. Tente novamente.")

        elif valor_saque > saldo_atual:
            print(f"Impossível sacar o valor desejado. Saldo atual: {saldo_atual:.2f}")

        else:
            return f"Saque de R${valor_saque:.2f} aprovado.\nSaldo atual: {saldo_atual:.2f}"
