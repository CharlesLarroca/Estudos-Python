from db import connect

def add_contact(nome, email, telefone):
  conn = connect()
  if conn:
      try:
        with conn.cursor() as cursor:
          sql = "INSERT INTO contatos (nome, email, telefone) VALUES (%s, %s, %s)"
          cursor.execute(sql, (nome, email, telefone))
          conn.commit()
          print(f'Contato {nome} adicionado com sucesso.')
      except Exception as err:
         print(f'Erro ao adicionar o contato {nome}: {err}')
      finally:
         conn.close()

def show_contacts():
  conn = connect()
  if conn:
      try:
        with conn.cursor() as cursor:
          sql = "SELECT * FROM contatos"
          cursor.execute(sql)
          result = cursor.fetchall()
          if result:
            print(f'Lista de contatos\n')
            for contact in result:
              contact_id = contact['id']
              nome = contact['nome']
              email = contact['email']
              telefone = contact['telefone']
              print(f"ID: {contact_id}, Nome: {nome}, Email: {email}, Telefone: {telefone}")
          else:
             print('Lista de contatos está vazia.')
      except Exception as err:
         print(f'Erro ao apresentar contatos: {err}')
      finally:
         conn.close()

def update_contact(id, nome=None, email=None, telefone=None):
  conn = connect()
  if conn:
      try:
        with conn.cursor() as cursor:
          sql = "UPDATE contatos SET nome = %s, email = %s, telefone = %s WHERE id = %s"
          cursor.execute(sql, (nome, email, telefone, id))
          conn.commit()
          print(f'Contato {id} atualizado com sucesso.')
      except Exception as err:
         print(f'Erro ao atualizar o contato {nome}: {err}')
      finally:
         conn.close()

def delete_contact(id):
  conn = connect()
  if conn:
      try:
        with conn.cursor() as cursor:
          sql = "DELETE FROM contatos WHERE id = %s"
          cursor.execute(sql, (id))
          conn.commit()
          print(f'Contato {id} excluido com sucesso.')
      except Exception as err:
         print(f'Erro ao excluir o contato {id}: {err}')
      finally:
         conn.close()
   