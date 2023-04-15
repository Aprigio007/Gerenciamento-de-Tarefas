#Aqui eu importo as bibliotecas necessarias
from os import system
import sqlite3

#conectando o banco na variavel tarefas e criando o cursoe
tarefas = sqlite3.connect('tarefas.db')
cursor = tarefas.cursor()

#Tentando criar a tabela, se ja existir nao fazer nada
try:
    cursor.execute('CREATE TABLE tarefas (tarefas text, id integer)')
except:
    pass

#Criando uma funcao para limpar a tela    
def l():
    system('clear')

#Iniciando o loop principal        
while True:
    #Criando o menu
    l()
    print('-=' * 20)
    print('TAREFAS'.center(40))
    print('-=' * 20)
    print('1- Adicionar Tarefa')
    print('2- Editar tarefa')
    print('3- Remover tarefa')
    print('4- Ver tarefas')
    
    #Tentando ler a entrada do usuario, se nao conseguir ler, pedir denovo
    while True:
        try:
            opc = int(input('--> '))
        except:
            print('Digite um valor valido')
        else:
            break
     #Verificando se a opcao é igual a 1       
    if opc == 1:
        #Pedindo as informacoes ao usuario
        l()
        tarefa = input('Digite a tarefa que deseja adicionar:\n')
        #Selecionando tudo da tabela tarefas
        cursor.execute('SELECT * FROM tarefas')
        #colocando tudo da tahela dentro de uma variavel
        tarefas_adicionar = cursor.fetchall()
        #[('Jigar', 1), ('Vsufke', 3), ('Hdgd', 3)]
        
        #definindo o id, que nada mais é que a quantidade de tarefas mais 1
        id = len(tarefas_adicionar) + 1
        #verificando se a ultima tarefa possui o id igual a da tarefa a dicionar, se sim, adicionar 1 ao id. E se der algum erro, não fazer nada.
        try:
            if tarefas_adicionar[len(tarefas_adicionar) - 1][1] == id:
                id += 1
        except:
            pass
        
            
        
        #Tentando inserir na tabela, se nao conseguir, informar ao usuario
        try:
            cursor.execute(f'INSERT INTO tarefas VALUES ("{tarefa}", {id})')
        except:
            print('Houve um erro ao adicionar a tarefa')
        else:
           #fazendo o commit do banco de dados
            tarefas.commit()
            print('Tarefa adicionada com sucesso')
            print('\n' * 3)
        input('Aperte Enter para Voltar')
   
     #Verificando se a entrada for igual  2         
    elif opc == 2:
        l()
        while True:
            #Tentando pedir as informacoes ao usuario, se nao conseguir, informar um erro
            try:
                id = int(input('Qual é o id da tarefa que deseja editar? '))
            except:
                print('Digite um valor valido')
            else:
                break
        #pedindo ao usuario para informar a tarefa a editar        
        tarefa_editada = input('Digite a nova tarefa: ') 
        
         #Tentando inserie os novos dados na tabela         
        try:
            cursor.execute(f'UPDATE tarefas SET tarefas = "{tarefa_editada}" WHERE id = {id}') 
        except:
            #informando um erro ao usuario ae nao conseguir
            print('Houve um erro ao editar')
        else:
            #fazendo o commit do banco e informando ao usuario que deu certo edutar
            tarefas.commit()
            print('Tarefa editada com sucesso')
            print('\n' * 3)
        input('Aperte Enter para voltar')
        
     #Verificando se a entrada for igual a 3   
    elif opc == 3:
        l()
        while True:
            
            #Tentando pedir a entrada ao usuario
            try:
                id = int(input('Qual é o id da tarefa que deseja excluir? '))
            #informando uma mensagem de erro se der errado    
            except:
                print('Digite um valor valido')
            else:
                break
         #Tentando deletar onde o id é igual a entrada do usuario       
        try:
            cursor.execute(f'DELETE FROM tarefas WHERE id = {id}')
         
         #informand9 uma mensagem de erro ao usuario se ocorrer um erro   
        except:
            print('Houve um erro ao deletar tarefa')
        else:
            #Fazendo o commit do banco
            tarefas.commit()
            print('Tarefa deletada com sucesso')
            print('\n' * 3)
        input('Aperte Enter para voltar')
     
    #verificando se a entrada for igual a 4       
    elif opc == 4:
        l()
        print('-=' * 30)
        #Selecionando tudo da tabela
        cursor.execute('SELECT * FROM tarefas')
        #Colando o select na variavek abaixo
        mostrar_tarefas = cursor.fetchall()
        #fazendo uma varredura na variavel para mostrar ao usuario
        for tarefa in mostrar_tarefas:
            #mostrando as tarefas
            print(f'{tarefa[1]} - {tarefa[0]}')
        print('\n' * 3)
        input('Aperte Enter para voltar')                                                                                                                                                                 