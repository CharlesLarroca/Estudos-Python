import pymysql

def connect():
    try:
        print("Tentando conectar ao banco de dados...")
        conn = pymysql.connect(
            host='localhost',
            user="root",
            password="Drl4rr0c4#",
            database="lista_contatos",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        print('Conexão bem-sucedida!')
        return conn 
    except pymysql.MySQLError as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        # Imprimir detalhes do erro
        print(f"Erro número: {err.errno}")
        print(f"Mensagem de erro: {err.msg}")
        print(f"Erro SQL: {err.sqlstate}")

if __name__ == "__main__":
    connect()


