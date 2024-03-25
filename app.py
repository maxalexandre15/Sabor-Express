import os

restaurantes =[  {'nome':'Praça', 'categoria':'Japonesa', 'ativo': False},
                 {'nome':'Pizza Suprema', 'cetegoria':'Pizza', 'ativo': True},
                 {'nome':'Cantina', 'cetegoria':'Italiana', 'ativo': False}
            ]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restautante')
    print('4 Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()    

def opcao_invalida():
    print('Opção inválida')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' (len(texto) + 4) 
    print(linha)
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restautante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restautante}:')
    dados_do_restaurante = {'nome': nome_do_restautante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(nome_do_restautante)
    print(f'O restaurante {nome_do_restautante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def lista_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restautante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restautante in restaurantes:
         nome_restaurante = restautante['nome']
         categoria = restautante['categoria']
         ativo = 'ativado' if restautante['ativo'] else 'desativado'
         print(f'- {nome_restaurante.ljust(20)}' | {categoria.ljust(20)} | {ativo})

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurante:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')


    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha  uma opção: '))
        opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
           cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
             lista_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()        

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
   main()