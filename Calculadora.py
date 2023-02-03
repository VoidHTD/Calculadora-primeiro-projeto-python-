print("Calculadora:")

print("")
while True:
    Numero1 = int(input('Primeiro Numero:'))
    Numero2 = int(input('Segundo Numero:'))

    opertation = input('''

    + para adição
    - para subtração
    * para multiplicação
    / para divisão]

    ''')
    
    print("")

    print("Resultado:")
    print("")

    if opertation == "+":

        Resultado = Numero1 + Numero2 
        print('{} + {} = {}'.format(Numero1, Numero2, Resultado))
        print("")

    elif opertation == "-":

        Resultado = Numero1 - Numero2
        print('{} - {} = {}'.format(Numero1, Numero2, Resultado))
        print("")
    
    elif opertation == "*":

            Resultado = Numero1 * Numero2
            print('{} * {} = {}'.format(Numero1, Numero2, Resultado))
            print("")

    elif opertation == "/":

                Resultado = Numero1 / Numero2
                print('{} / {} = {}'.format(Numero1, Numero2, Resultado))
                print("")

    else:
        print("Somente caracteres matematicos.")
        print("")
        


            
    

        


