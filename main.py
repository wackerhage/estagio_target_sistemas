#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2
# valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem
# que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem
# avisando se o número informado pertence ou não a sequência. IMPORTANTE: Esse número pode ser informado
# através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

'''#Lista que ira armazenar os elementos da sequencia de Fibonacci
fib_sequencia = []

#Valores iniciais da Sequencia que darao inicio ao algoritmo
a = 0
b = 1

try:
    while True:
        # Pede um numero ao usuario
        numero = int(input("Digite um numero: "))

        #Cria um looping onde, enquanto o valor de "a" for menor ou igual ao numero do input, ele continuara o looping
        while a <= numero:
            #A funcao append ira incrementar o valor de "a" na lista fib_sequencia
            fib_sequencia.append(a)
            #O valor de "a" sera "b" e o valor de "b" sera "b" + "a", deixando o valor inicial de "a" para tras
            a, b = b, a + b
            #O looping ira ocorrer ate o numero de entrada, com o valor de "a" sempre se tornando a soma de "b" + "a"
        for elemento in fib_sequencia:
            if numero == elemento:
                print("Este numero pertence a sequencia de Fibonacci!!!")
        print(f"A sequencia de Fibonacci ate o numero {numero} tem a seguinte ordem: {fib_sequencia}")
except ValueError:
    print("Numero invalido, por favor tente novamente.")'''

#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja
# maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua
# preferência ou pode ser previamente definida no código;

'''
while True:
    contador = 0
    answer = input("Informe uma frase ou palavra: ")
    answer = answer.lower()

    for letra in answer:
        if "a" in letra:
            contador += 1
    if contador >= 1:
        print(f"A letra 'a' consta {contador} na palavra ou frase digitada.")
    else:
        print("A letra 'a' nao existe nesta palavra ou frase.")'''

#3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1;
# enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

'''indice = 12
soma = 0
k = 1

#looping enquanto a variavel for menor que o indice 12, ira incrementar 1 
# a cada looping e fazer a soma de k na variavel soma
while k < indice:
    k = k + 1
    soma = soma + k

print(soma)'''

#O valor da variavel soma sera 77

#4) Descubra a lógica e complete o próximo elemento:
#a) 1, 3, 5, 7, ___
#R.: 9 (somente numeros impares)
#b) 2, 4, 8, 16, 32, 64, ____
#R.: 128 (Numero multiplicado por 2, resultando no proximo elemento da lista)
#c) 0, 1, 4, 9, 16, 25, 36, ____
#R.: 49 (Sequencia de quadrados perfeitos)
#d) 4, 16, 36, 64, ____
#R.: 100 (Quadrado de numeros pares)
#e) 1, 1, 2, 3, 5, 8, ____
#R.: 13 (sequencia de fibonacci)
#f) 2, 10, 12, 16, 17, 18, 19, ____
#R.: 200 (Numeros com inicio da letra "D")

#5) Você está em uma sala com três interruptores,
# cada um conectado a uma lâmpada em salas diferentes.
# Você não pode ver as lâmpadas da sala em que está, mas pode
# ligar e desligar os interruptores quantas vezes quiser.
# Seu objetivo é descobrir qual interruptor controla qual lâmpada.
# Como você faria para descobrir, usando apenas duas idas até uma
# das salas das lâmpadas, qual interruptor controla cada lâmpada?
#R.:
# Ligar o interruptor A apenas por alguns minutos e desligar
# Ligar o interruptor B e deixar ligado
# O interruptor C ficara desligado
# Iria ate a sala 1,
#   se a lampada estiver apagada, entao o interruptor da sala 1 seria o interruptor C
#   se a lampada estiver quente, mas desligada, o interruptor da sala seria o interruptor A
#   se a lampada estiver ligada, o interruptor seria B
# Fazer este processo na outra sala, ou seja um looping de 2 vezes, entao descobriria qual sala esta
# com qual interruptor.

interruptor_A = True
interruptor_B = False
interruptor_C = False

#variantes
lampada_1 = 1 #lampada ligada
lampada_2 = 0 #lampada desligada
lampada_3 = 0.5 #Valor da lampada que foi desligada minutos depois

if interruptor_A == True and lampada_1:
    print("A lampada 1 esta conectada no interruptor A.")
elif interruptor_B == False and lampada_2:
    print("A lampada 2 esta conectada no interruptor B.")
elif interruptor_C == False and lampada_3:
    print("A lampada 3 esta conectada no interruptor C.")





