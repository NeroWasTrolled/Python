import os
import csv

def cadastrar_cliente():
    dados = {} #criando o dicionário de dados, para armazenar clientes
    
    os.system('cls') or None #limpar tela
    print('------------------ CADASTRO DE CLIENTES ------------------')

    nome = input("Nome: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    dados[cpf] = [nome, rg]
    coluna = ['cpf', 'nome', 'rg']
    print(coluna)
    print(dados)

    files_exists = os.path.isfile("clientes.csv")

    with open('clientes.csv', 'a', newline='', encoding='utf-8') as clientes_csv:
        cadastrar = csv.DictWriter(clientes_csv, fieldnames=coluna, delimiter=';', lineterminator='\r\n')
        if not files_exists:
            cadastrar.writeheader()
        
        cadastrar.writerow({'cpf': cpf, 'nome': nome.title(), 'rg': rg})
    print("Cadastro realizado com sucesso!")

cadastrar_cliente()

def cadastrar_livro():
    return 0