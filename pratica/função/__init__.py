from time import sleep


def interface(msg):
    tam = len(msg)+5
    print('~'*tam)
    print(msg.center(tam))
    print('~'*tam)


def leiaint(msg):
    check = False
    value = 0
    while True:
        number = str(input(msg))
        if number.isnumeric():
            value = int(number)
            check = True
        else:
            print('\033[31m[ERRO] Valor inválido\033[m.')
        if check:
            break
    return value


def deposito():
    print('=== \033[:34mDepóssito\033[m === ')
    bank = leiaDinheiro('Fazer um depósito\nInforme o valor: R$ ')
    verify = conta2() + bank
    conta(verify)
    sleep(0.5)
    print('\033[32mNovo valor adicionado\033[m.')


def retirada():
    print('=== \033[:34mRetiraa\033[m ===')

    verify = conta2()
    while True:
        bank = leiaDinheiro('Quanto deseja sacar? MAX R$ 2000\nSaque: R$ ')
        if verify == 0:
            print(f'Seu saldo é {moedas(verify)}')
            try:
                opc = str(input('Deseja fazer um depósito?\nEscolha [S/N]: ')).strip().upper()[0]
                if opc in 'S':
                    deposito()
                    break
                if opc in 'N':
                    print('Voltando ao Menu Principal...')
                    sleep(2)
                    interface('ATM - Caixa Eletrônico')
                else:
                    print('\033[:31m[ERRO] Opção inválidda\033[m.')
            except:
                print('Apenas [S/N]')
        elif verify < bank:
            print(f'Não é possivel efetuar o saque.\nseu saldo é {moedas(verify)}')
        else:
            print('\033[32mSaque efetuado com sucesso\033[m.')
            transação = verify - bank
            conta(transação)
        break


def conta(valor):
    convert = str(valor)
    with open("conta.txt", "w") as arquivo:
        arquivo.write(convert)


def conta2():
    with open("conta.txt", "r") as arquivo:
        dinheiro = arquivo.read()
    return float(dinheiro)


def moedas(valor='0', moeda='R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')


def leiaDinheiro(msg):
    check = False
    while not check:
        dinheiro = str(input(msg)).replace(',','.').strip()
        if dinheiro.isalpha() or dinheiro == '':
            print(f'\033[1:31m[ERRO] Valor inválido, {dinheiro} não permitido\033[m.')
        else:
            check = True
            return float(dinheiro)
