class Caixa:
    def __init__(self, nome):
        self.nome = nome
    
    def processar_pagamento(self, metodo, valor):
        print(f"{self.nome} vai processar o pagamento...")
        metodo.pagar(valor)

# Classes de formas de pagamento
class CartaoCredito:
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} com cartão de crédito.")

class Dinheiro:
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} em dinheiro.")

class Pix:
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} via Pix.")

# Criando objetos
caixa = Caixa("Caixa do Supermercado")

cartao = CartaoCredito()
dinheiro = Dinheiro()
pix = Pix()

# Criando objeto do cupom
class Cupom:
    def imprimir(self):
        print("Cupom de desconto de R$10,00.")

cupom = Cupom()

# Teste de execução
caixa.processar_pagamento(cartao, 100.00)
caixa.processar_pagamento(dinheiro, 50.00)
caixa.processar_pagamento(pix, 75.00)

# Imprimir cupom
cupom.imprimir()
