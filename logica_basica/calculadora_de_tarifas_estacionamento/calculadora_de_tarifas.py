'''Calculadora de Tarifas de Estacionamento
até 1 hora -> R$ 5,00
De 2 a 4 horas -> R$ 5,00 + R$ 3,00 por hora adicional
Acima de 4 horas -> R$ 15,00 (tarifa única diária)
'''
def calcular_tarifas():
    horas = float(input("Quantas horas seu carro ficou no estacionamento?"))
    cupom = input("Voce possui cupom de desconto? SIM ou NÃO").upper()
    valor_total = 0
    hora_adicional = int(horas - 2)
    if horas <=0:
        return "TEMPO INVÁLIDO"
    
    elif horas <= 1:
        valor_total = 5
    elif 2 <= horas <= 4:
        valor_total = 5 + 3 * int(hora_adicional)
    elif horas > 4:
        valor_total = 15
    if cupom == "SIM":
        valor_total -= 2
    return print(valor_total)

calcular_tarifas()



