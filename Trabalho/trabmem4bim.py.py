#Universidade da Região de Joinville - UNIVILLE
#Departamento de Informática
#Curso de Bacharelado em Engenharia de Software
#Disciplina: APC – Algoritmos e Programação de Computadores
#Professor: Walter Silvestre Coan
#Serie: 2B Noturno
#Aluno: Francisco Marcello Ribeiro Lima

#Trabalho sobre Algoritmos de Gerenciamento de Memória

import random

memoria = [' '] * 100
#memoria = [' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x']
opcao = 0
tamanho = 0
letra = ''
naoencontrado = 'Nao foi encontrado espaco suficiente para alocar estas informacoes'
for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '

#Prints dos espacos de memoria, separados em blocos de 20 slots cada
for i in range(0,20):
    print(memoria[i], end="|")
print()
for i in range(20,40):
    print(memoria[i], end="|")
print()
for i in range(40,60):
    print(memoria[i], end="|")
print()
for i in range(60,80):
    print(memoria[i], end="|")
print()
for i in range(80,100):
    print(memoria[i], end="|")
print()

#Menu do programa
while(opcao != 4):
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    if opcao == 4:
        print("Programa encerrado!")
        break
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utilizada")
    letra = input()

    if(opcao == 1): 
        #Lógica da primeira escolha
        #Programa é alocado na primeira partição grande o suficiente
        inicio = 0
        maiorespaco = 0
        while inicio < 100:
            if memoria[inicio] == " ":
                #print(f"ini: {inicio}", end=" ")
                fim = inicio + 1
                while fim < 100:
                    if memoria[fim] != " ":
                        #print(f"fim: {fim}", end=" ")
                        tamanhoespaco = fim - inicio
                        if tamanhoespaco > maiorespaco:
                                    #salva informacoes do tamanho do maior espaco
                                    maiorespaco = tamanhoespaco
                        #print(f"tamanhoespaco: {tamanhoespaco}")
                        if tamanhoespaco >= tamanho:
                            #verifica se o tamanho do espaco eh grande o suficiente
                            #se sim, entao grava a letra na qtd do tamanho
                            for j in range (inicio, inicio + tamanho):
                                memoria[j] = letra
                            #se achou o espaco para alocar a informacao ele adiciona 100
                            #na variavel fim, acabando com a repeticao da estrutura while
                            fim += 100
                        inicio = fim
                        break
                    fim += 1
            inicio += 1
        if tamanho > maiorespaco:
            #detecta que nenhum espaco foi grande o suficiente para alocar a informacao
            print(naoencontrado)
        pass
    else:
        if (opcao == 2):
            #Lógica da melhor escolha
            #Programa é alocado na menor partição grande o suficiente
            inicio = 0
            maiorespaco = 0
            while inicio < 100:
                if memoria[inicio] == " ":
                    #print(f"ini: {inicio}", end=" ")
                    fim = inicio + 1
                    while fim < 100:
                        if memoria[fim] != " ":
                            #print(f"fim: {fim}", end=" ")
                            tamanhoespaco = fim - inicio
                            if tamanhoespaco > maiorespaco:
                                    #salva informacoes do tamanho do maior espaco
                                    maiorespaco = tamanhoespaco
                            #print(f"tamanhoespaco: {tamanhoespaco}")
                            if tamanhoespaco == tamanho:
                            #verifica se o tamanho do espaco eh igual ao tamanho da informacao
                            #se sim, entao grava a letra na qtd do tamanho
                                for j in range (inicio, inicio + tamanho):
                                    memoria[j] = letra
                                #se achou o espaco para alocar a informacao ele adiciona 100
                                #na variavel fim, acabando com a repeticao da estrutura while
                                fim += 100
                            inicio = fim
                            break
                        fim += 1
                inicio += 1
            if tamanho > maiorespaco:
                #detecta que nenhum espaco foi grande o suficiente para alocar a informacao
                print(naoencontrado)
            pass
        else:
            if(opcao == 3):
                #Lógica da pior escolha
                #Programa é alocado na maior partição grande o suficiente
                inicio = 0
                maiorespaco = 0
                while inicio < 100:
                    if memoria[inicio] == " ":
                        #print(f"ini: {inicio}", end=" ")
                        fim = inicio + 1
                        while fim < 100:
                            if memoria[fim] != " ":
                                #print(f"fim: {fim}", end=" ")
                                tamanhoespaco = fim - inicio
                                if tamanhoespaco > maiorespaco:
                                    maiorespaco = tamanhoespaco
                                    inimaiorespaco = inicio
                                    #verifica se o tamanho do espaco e maior que o maior ja salvo
                                    #se sim, entao salva o tamanho do maior espaco e o seu inicio
                                    #print(f"tamanhoespaco: {tamanhoespaco}")
                                inicio = fim
                                break
                            fim += 1
                    inicio += 1
                if maiorespaco >= tamanho:
                    #verifica se o tamanho do maior espaco e maior ou igual ao tamanho
                    #se sim, adiciona a informacao no espaco detectado
                    for j in range (inimaiorespaco, inimaiorespaco + tamanho):
                        memoria[j] = letra
                else:
                    #senao, informa que nenhum espaco foi grande o suficiente para alocar a informacao
                    print(naoencontrado)
                pass
    # Aqui você deve imprimir todo o conteúdo da variável memória
    print("Estado atual da memória:")
    for i in range(0,20):
        print(memoria[i], end="|")
    print()
    for i in range(20,40):
        print(memoria[i], end="|")
    print()
    for i in range(40,60):
        print(memoria[i], end="|")
    print()
    for i in range(60,80):
        print(memoria[i], end="|")
    print()
    for i in range(80,100):
        print(memoria[i], end="|")
    print()