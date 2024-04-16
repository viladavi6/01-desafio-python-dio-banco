import time
import random as rd

def menu():
    print(f'''\n
============= Menu =============

[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNovo Usuário
[5]\tCadastrar conta
[6]\tListar conta
[0]\tSair

================================
''')

def retornar_menu():
    print('\nRetornando ao menu...')
    time.sleep(5)

def deposito(total_saldo, valor, extrato):
    if valor > 0:
        total_saldo += valor
        extrato += f'\nDepósito realizado com sucesso: {valor:.2f}\n'
        print(f'\n{extrato}\n')
    return total_saldo, extrato

def sacar(*, saque, total_saldo, extrato, limite_saque_valor, limite_saque_dia):
    sem_saldo = total_saldo < saque
    sem_limite = saque > limite_saque_valor
    sem_saque = limite_saque_dia == 0

    if sem_limite:
        print(f'''
                ===================================================
                  
                Você está tentando sacar mais que o seu limite
                Limite de valor em R${limite_saque_valor}
                Para aumentar seu limite de saque, entre em contato
                com o seu gerente.
                  
                ===================================================
                ''')
    elif sem_saldo:
        print(f'''
                ===================================================
                  
                Você não pode sacar porque não tem saldo suficiente 
                Valor Disponível: {total_saldo}
                Valor Solicitado: {saque}
                  
                ===================================================
                  
                ''')
    elif sem_saque:
        print('''
                    ===================================================
                  
                    Você já sacou 3 vezes, para aumentar sua quantidade
                            entre em contato com o seu gerente.
                  
                    ===================================================
                  
                  ''')
    elif saque > 0:
        total_saldo -= saque
        limite_saque_dia -= 1
        extrato += f'''\n
                ===================================================
                  
                Saque realizado com sucesso 
                Valor Sacado: {saque}
                Valor Disponível: {total_saldo}
                Quantidade de valor restante: {limite_saque_dia}
                  
                ===================================================
                \n  
                '''
        print(f'\n{extrato}\n')
    return total_saldo, extrato, limite_saque_dia

def extratos(total_saldo, *, extrato):
    if extrato == "":
        print(f'\nVocê tem R$ 0 disponível.')
    else:
        print(f'\nVocê tem R${total_saldo:,.2f} disponível.')
        print(f'\nAqui estão suas últimas movimentações: \n{extrato}\n')

def filtrar_usuario(cpf, usuario):
    usuarios_filtrados = [usuarios for usuarios in usuario if usuarios['CPF'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(usuario, AGENCIA, numero_conta_final):
    print('\nPara cadastrar uma conta é necessário ter criado um usuário: ')
    print('\nCaso queira voltar ao menu é só digitar 0 em qualquer operação: ')
    time.sleep(5)
    
    while True:
        try:
            cpf = input('\nDigite o seu CPF para prosseguir: ')
            usuario = filtrar_usuario(cpf, usuario)
            
            if cpf == '0':
                retornar_menu()
                return None
            elif not usuario: 
                print("\nCPF não cadastrado. Por favor, cadastre seu usuário primeiro.")
                retornar_menu()
                return None
            elif usuario:
                print('\nCriando dados bancários: ')
                numero_conta = rd.randint(10000, 99999)
                numero_conta2 = rd.randint(0, 9)
                numero_conta_final = f"{numero_conta}-{numero_conta2}"
                print(f'''===============================
          
                                Conta criada com sucesso:
                                Obrigado pela preferência!
                                Agência: {AGENCIA}
                                Nº da Conta: {numero_conta_final}
                        
                            ===============================''')
                retornar_menu()
                return {'Agência': AGENCIA, 'Número da conta': numero_conta_final, 'usuario': usuario} 
        except ValueError:
            print('\nDigite um cpf válido, ou cadastre seu usuário.')
            
def criacao_usuario(usuario):
    while True:
        try:
            print('\nCaso queira voltar ao menu é só digitar 0 em qualquer operação: ')
            time.sleep(5)
            
            cpf = input('\nInforme somente os números do seu CPF(12345678912): ')
            usuarios = filtrar_usuario(cpf, usuario)
            if cpf == '0':
                retornar_menu()
                break
            elif usuarios:
                print('Já existe este usuário')
                retornar_menu()
                return None
            else:
                nome = input('\nInforme seu nome completo: ')
                if nome == '0': 
                    retornar_menu()
                    break
                data_nascimento = input('\nInforme sua data de nascimento neste formato (d/m/a): ')
                if data_nascimento == '0':
                    retornar_menu()
                    break
                rua = input('\nInforme seu endereço (Rua): ')
                if rua == '0':
                    retornar_menu()
                    break
                numero = input('\nInforme o número da sua residência: ')
                if numero == '0':
                    retornar_menu()
                    break
                bairro = input('\nInforme o seu bairro: ')
                if bairro == '0':
                    retornar_menu()
                    break
                cidade = input('\nInforme a sua cidade: ')
                if cidade == '0':
                    retornar_menu()
                    break
                uf = input('\nInforme seu estado(UF): ')
                if uf == '0':
                    retornar_menu()
                    break
            
                print(f'\nUsuário Cadastrado com Sucesso. Obrigado pela preferência!\n')
                usuario.append({'Nome': nome, 'Data de Nascimento': data_nascimento, 'CPF': cpf, 'Rua': rua, 'Número': numero, 'Bairro': bairro, 'Cidade': cidade, 'UF': uf})
                retornar_menu()
                break
        except ValueError:
            print('\nInsira um valor válido: ')

def listar_contas(contas):
    for conta in contas:
        linha = f'''
        Agência:\t{conta['Agência']}
        C/C:\t\t{conta['Número da conta']}
        Titular:\t{conta['usuario']['Nome']}
        '''
        print('=' * 100)
        print(linha)

def iniciar():
    limite_saque_valor  = 500
    limite_saque_dia = 3
    total_saldo = 0
    extrato = ''
    usuario = [] 
    contas = []
    AGENCIA = '0001'  

    print('\nBem vindo! Qual o serviço que você deseja?\n ')
    
    while True:
        menu()
        opcao = input('\n:')
        if opcao == '1':
            while True:
                try:
                    valor = float(input('Digite o valor que você deseja depositar: '))
                    total_saldo, extrato = deposito(total_saldo, valor, extrato)
                    retornar_menu()
                    break
                except ValueError:
                    print('\nValor incorreto.\n')
        elif opcao == '2':
            while True:
                try:   
                    saque = float(input('Digite o valor que você deseja sacar: '))
                    break
                except ValueError:
                    print('\nDigite um valor válido que deseja sacar.\n')
            total_saldo, extrato, limite_saque_dia = sacar(
                total_saldo=total_saldo, 
                saque=saque,
                limite_saque_valor=limite_saque_valor,
                limite_saque_dia=limite_saque_dia,
                extrato=extrato)
            retornar_menu()     
        elif opcao == '3':
            extratos(total_saldo, extrato=extrato)
            retornar_menu()
        elif opcao == '4':
            criacao_usuario(usuario=usuario)
        elif opcao == '5':
            numero_conta_final = ''
            conta = criar_conta(usuario, AGENCIA, numero_conta_final)
            if conta:
                contas.append(conta)
        elif opcao == '6':
            listar_contas(contas)
        elif opcao == '0':
            print('\n Obrigado pela preferência, tenha um ótimo dia!')
            break    
        elif opcao not in ('0', '1', '2', '3', '4', '5', '6'):
            print('\nOpção inválida\n')
            retornar_menu()

iniciar()