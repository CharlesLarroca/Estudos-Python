from contatos import add_contact, show_contacts, update_contact, delete_contact

def menu():
  while True:
    print('\nEscolha uma Opção:')
    print('\n1. Adicionar contato.')
    print('2. Listar todos os contatos.')
    print('3. Atualizar contato.')
    print('4. Excluir contato.')
    print('5. Sair')

    opcao = input('\nSelecione uma opção: ')

    if opcao == '1':
      nome = input('Digite o nome do contato: ')
      email = input('Digite o email do contato: ')
      telefone = input('Digite o telefone do contato: ')
      add_contact(nome, email, telefone)
    
    elif opcao == '2':
      show_contacts()

    elif opcao == '3':
      id_contact = input('Digite o ID do contato: ')
      nome = input('Digite o nome do contato: ')
      email = input('Digite o email do contato: ')
      telefone = input('Digite o telefone do contato: ')
      update_contact(id_contact, nome, email, telefone)
    
    elif opcao == '4':
      id_contact = input('Digite o ID do contato: ')
      delete_contact(id_contact)
    
    elif opcao == '5':
      print('Saindo...')
      break

    else:
      print('Opção inválida!')

menu()