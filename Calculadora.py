# -*- coding: utf-8 -*-
'''
Calculadora
Autor: Yuri Sousa
Função: Fazer contas: soma, divisão, multiplicação, subtração, Numero Elevado
'''
print ("----CALCULADORA DO YURI v2.0 ----")

sair = False

while sair == False:

    num1 = input ("Digite o primeiro número")
    texto1 = num1
    num1 = int (num1)
    operador = input ("digite o operador")
    num2 = input ("digite o segundo numero")
    texto2 = num2
    num2 = int (num2)
    print (texto1 + operador + texto2)

    # + soma
    if operador == "+":
        operação = num1 + num2
    # - subtração
    if operador == "-":
        operação = num1 - num2
    # / divisão
    if operador == "/":
        operação = num1 / num2
    # * Multiplicação
    if operador == "*":
        operação = num1 * num2
    # Numero Elevado   
    if operador == "**":
        operação = num1 ** num2
        
    print ("Resultado: ")
    print (operação)
    
    teste = input ("Deseja sair (n/s): ")
    if teste == "n":
        sair = False
    if teste == "s":
        sair = True