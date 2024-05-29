import pyodbc
import os
global connection

def connect() -> bool:

    try:
        connection = pyodbc.connect(
            driver = "{SQL Server}",
            server = "regulos.cotuca.unicamp.br",
            database = "BD24329"
            uid = "BD24329",
            pwd = "BD24329"
        )
        return True
    except:
        return False
    
    def insert() -> bool:
        # curso é um  objeto que permite que nosso programa execute comandos SQL lá no servidor 
        cursor = connection.cursor()

        codigoProduto = imput("Código protudo:")
        nome = imput ("Nome")
        preço = float(input("Prreço:"))

      #criou um string com o comando INSERT

        comand = "INSERT INTO pratica.Produto(codigoProduto, nome, preço, inativo) + \
                   "(VALUES" + f" ({codigoProduto}, '{nome}', '{preço}', 0 "))
        
        try:
            #tentar executar o comando no banco de dados

            cursor.execute(comand)
            #ele vai aplicar as alteraçoes no namco de dados 
            cursor.comit()
            return True
        except:
            # em caso de erro 
        return False
    
    del main():

    if connect():

        option = -1
     def delete () -> bool:

        pass

      def select() -> bool:

        pass
      def main()-> bool
    
    if connect():

        while option !=0:
            option = 1

            print("0 - sair ")
            print("1 - Cadastrar novos produtos")
            print("2 - Alterar um produto")
            print("3 - Excluir um produto")
            print("4 - Listar os produtos")

            option = int("input("\nDigite a opção desejada:")
                         
                         if option == 1:
                         elif option ==2:
                         update()
                         elif option ==2:
                         update()
                         elif option ==3:
                         update()
                         elif option ==4:
    #fechou a conexão com o banco de dados
    #NUNCA ESQUEÇAM DE FAZER ISSO!!!
    connection.close()
    