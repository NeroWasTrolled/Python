import cadastro as c #definindo um alias para cadastro
import listar, movimentacao, relatorio, remover

resposta = 's'

while resposta == 's':
    menu = '''------------------ BLIBIOTECA TDS 10 ------------------
    \r[1] Cadastrar Cliente
    \r[2] Listar Cliente
    \r[3] Cadastrar Livro
    \r[4] Listar livros
    \r[5] Realizar Empréstimo
    \r[6] Lista de Empréstimo
    \r[7] Relatório de Livros Atrasados
    \r[8] Remover Cliente
    \r[9] Remover Livro
    '''
    
    print(menu)

    opcao = int(input('Entre com uma opção: ')) #escolher a opção digitada

    if opcao == 1:
        c.cadastrar_cliente()
    elif opcao == 2:
        listar.listar_cliente()
    elif opcao == 3:
        c.cadastrar_livro()
    elif opcao == 4:
        listar.listar_livros()
    elif opcao == 5:
        movimentacao.realizar_emprestimo()
    elif opcao == 6:
        listar.listar_emprestimo()
    elif opcao == 7:
        relatorio.relatorio_atrasados()
    elif opcao == 8:
        remover.remover_cliente()
    elif opcao == 9:
        remover.remover_livro()


    resposta = input("\nDeseja continuar? [s/n]")