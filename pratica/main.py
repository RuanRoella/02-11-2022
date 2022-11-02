from função import *
from time import sleep

interface('ATM - Caixa Eletrônico')

while True:
    opc = leiaint("""[1] Ver Salo
[2] Depósito
[3] Retirada
[4] Sair
Escolha: """)
    match opc:
        case 1:
            print('==== \033[34mSALDO\033[m ====')
            print(f' {moedas(conta2())}')
            print('==== \033[:33m*****\033[m ====')
            while conta2() == 0:
                try:
                    opc = str(input('Deseja adicionar um saldo?\nEscolha [S/N]: ')).strip().upper()[0]
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
            continue
        case 2:
            deposito()
            print()
            sleep(2)
            continue
        case 3:
            retirada()
            sleep(2)
            continue
        case 4:
            print('-- Finalizando --')
            sleep(2)
            print('-- ATÉ LOGO --')
            break
        case other:
            print('\033[31mOpção inválida\033[m.')

