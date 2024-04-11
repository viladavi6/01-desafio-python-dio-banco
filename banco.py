import time

menu = '''
============= Menu =============

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

================================

Qual opção você deseja: '''


limite_saque_valor  = 500
limite_saque_dia = 3
total_saldo = 0
extrato = ''


    
while True:
      
    opcao = input(menu)
      
    if opcao == '1':   
        
        while True:
            try:
                valor = int(input('Digite o valor que você deseja depositar: '))
                break
            except ValueError:
                print('\nValor incorreto.\n')
            
        
        if valor > 0:
            total_saldo += valor
            extrato += f'Depósito realizado com sucesso: {valor:.2f}\n'
            print(f'\n{extrato}... Retornando ao menu principal \n')
            time.sleep(5)
        else:
            print('\nOperação falhou, retornando ao menu. \n')
            time.sleep(5)
    
    elif opcao == '2':
        
        while True:
            try:   
                saque = float(input('Digite o valor que você deseja sacar: '))
                break
            except ValueError:
                print('\nDigite um valor válido que deseja sacar.\n')
            
        
        if total_saldo >= saque and saque <= limite_saque_valor and limite_saque_dia > 0:
            total_saldo -= saque
            limite_saque_dia -= 1
            extrato += f'''
                ===================================================
                  
                Saque realizado com sucesso 
                Valor Sacado: {saque}
                Valor Disponível: {total_saldo}
                Quantidade de saque restante: {limite_saque_dia}
                  
                ===================================================
                  
                '''
            print(f'\n{extrato}\n Retornando ao menu...\n')
            time.sleep(5)
                
        elif total_saldo < saque and limite_saque_dia > 0:
            extrato += f'''
                ===================================================
                  
                Você não pode sacar porque não tem saldo suficiente 
                Valor Disponível: {total_saldo}
                Valor Solicitado: {saque}
                  
                ===================================================
                  
                '''
            print(extrato)
            print('\nRetornando ao menu...\n')
            time.sleep(5)
        elif limite_saque_valor < saque and limite_saque_dia > 0:
            print(f'''
                ===================================================
                  
                Você está tentando sacar mais que o seu limite
                Limite de saque em R${limite_saque_valor}
                  
                ===================================================
                ''')
            print('\nRetornando ao menu...\n')
            time.sleep(5)
        elif limite_saque_dia == 0:
            print('''
                    ===================================================
                  
                    Você já sacou 3 vezes, para aumentar sua quantidade
                            entre em contato com o seu gerente.
                  
                    ===================================================
                  
                  ''')
            print('\nRetornando ao menu...\n')
            time.sleep(5)
        elif saque == ValueError:
            print('\n Valor incorreto, voltando ao menu.\n')    
            time.sleep(10)
    if opcao == '3':
        
        if extrato == "":
            print(f'\nVocê tem R$ 0 disponível.')
            print('\nRetornando ao menu...\n')
            time.sleep(5)
        else:
            print(f'\nVocê tem R${total_saldo:,.2f} disponível.')
            print('\nRetornando ao menu...\n')
            time.sleep(5)
         
              
    if opcao == '0':
        break      
    
    
        
        
            




      

        


            

