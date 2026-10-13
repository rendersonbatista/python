def PDV():
    produto = str(input("Nome do produto: "))
    preco = float(input("Valor do produto: "))
    quantidade = int(input("Quantidade do produto: "))
    formaPagamento = int(input("[1] Dinheiro, [2] Pix, [3]cartão: "))
    valorTotal = preco * quantidade

    if formaPagamento == 1:
        valorCliente = float(input("Valor recebido do cliente: "))
        troco = valorCliente - valorTotal 

        if valorCliente < valorTotal:
            print("Valor abaixo do valor total")
        else:
            print(f"O valor total da compra: {valorTotal}")
            print(f"Troco do cliente: {troco}")
    elif formaPagamento == 2:
        print(f"Forma de pagamento no pix")
        print("Compra realizada com sucesso")
    elif formaPagamento == 3:
        print(f"Fomra de pagamento no cartão")
        print("Compra realizada com sucesso")
    else:
        print("Forma de pagamento INVÁLIDO")

        print(f"O valor total da compra: {valorTotal}")

    finaliza = int(input("Finalizar [1]- Sim, [2]-Não: "))

    if finaliza == 1:
        cliente = False
        print("Operação realizada com sucesso")
    elif finaliza == 2:
        cliente = True

        while cliente == True:
            PDV()

    else:
        print("opção inválida")


PDV()

