def separaEmPar(frase):
    par = ''
    pares = []
    frase = frase.replace(' ', '').replace(',', '').replace('.', '').replace('!', '').replace('?', '')
    for letra in frase:
        if par == '':
            par = letra
        else:
            if par == letra:
                par = par + "X"
                pares.append(par)
                par = letra
            else:
                par = par + letra
                pares.append(par)
                par = ''
    if len(par) == 1:
        pares.append(par + "X")

    return pares


def modificaAlfabeto(palavra_chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
    alfabeto_modificado = alfabeto
    palavra = ''
    for i in palavra_chave:
        if i in alfabeto:
            alfabeto_modificado = alfabeto_modificado.replace(i, '')
            if i not in palavra:
                palavra = palavra + i

    return palavra + alfabeto_modificado


def percorreMatrizComPalavraChave(alfabeto):
    matriz = [alfabeto[0:5], alfabeto[5:10], alfabeto[10:15], alfabeto[15:20], alfabeto[20:]]

    return matriz


def criptografarMensagem(matriz, par):
    _linha = 0
    _coluna = 0

    for linha, value_linha in enumerate(matriz):
        for coluna, value_coluna in enumerate(value_linha):
            if par[0] in value_coluna:
                _coluna = coluna

    for linha, value_linha in enumerate(matriz):
        for coluna, value_coluna in enumerate(value_linha):
            if par[1] in value_coluna:
                _linha = linha

    cripted = matriz[_linha][_coluna]

    for linha, value_linha in enumerate(matriz):
        for coluna, value_coluna in enumerate(value_linha):
            if par[1] in value_coluna:
                _coluna = coluna

    for linha, value_linha in enumerate(matriz):
        for coluna, value_coluna in enumerate(value_linha):
            if par[0] in value_coluna:
                _linha = linha

    cripted = cripted + matriz[_linha][_coluna]

    return cripted


print("Digite a palavra a ser cifrada: ")
frase = str(input()).upper()
print("Digite a sua chave: ")
palavra_chave = str(input()).upper()
alfabeto = modificaAlfabeto(palavra_chave)
print(alfabeto)
matriz = percorreMatrizComPalavraChave(alfabeto)
par = separaEmPar(frase)
critpted_mensagem = criptografarMensagem(matriz, par[0])

while True:

    print("1 - Escolher uma tabela de cifra nova")
    print("2 - Introduzir uma mensagem para cifrar")
    print("3 - Ver a mensagem cifrada")
    print("4 - Decifrar a mensagem")
    print("5 - Ver o alfabeto")
    print("6 - Terminar")

    opcao = int(input())

    if opcao == 1:
        palavra_chave = str(input()).upper()
        alfabeto = modificaAlfabeto(palavra_chave)
        matriz = percorreMatrizComPalavraChave(alfabeto)

    elif opcao == 2:
        frase = str(input()).upper()

    elif opcao == 3:
        print("A palavra criptografada é: " + critpted_mensagem + '\n\n')

    elif opcao == 4:
        print("Deseja decifrar a mensagem ja existente ?")
        print("1 - Sim")
        print("2 - Não")

        if int(input()) == 2:
            print("Digite a palavra a ser cifrada: ")
            frase = str(input()).upper()
            par = separaEmPar(frase)
            print("A palavra descriptografada é: " + criptografarMensagem(matriz, par[0]) + '\n\n')
        else:
            print("A palavra descriptografada é: " + criptografarMensagem(matriz, critpted_mensagem) + '\n\n')

    elif opcao == 5:
        print("O alfabeto atual é: " + alfabeto)

    elif opcao == 6:
        break
