class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

    def __str__(self):
        fav = "Sim" if self.favorito else "Não"
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, Favorito: {fav}"

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self):
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        favorito = input("É favorito? (s/n): ").lower() == 's'
        contato = Contato(nome, telefone, email, favorito)
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for i, contato in enumerate(self.contatos, start=1):
                print(f"{i}. {contato}")

    def editar_contato(self):
        self.listar_contatos()
        if not self.contatos:
            return
        try:
            index = int(input("Digite o número do contato que deseja editar: ")) - 1
            if 0 <= index < len(self.contatos):
                nome = input("Digite o novo nome: ")
                telefone = input("Digite o novo telefone: ")
                email = input("Digite o novo email: ")
                favorito = input("É favorito? (s/n): ").lower() == 's'
                self.contatos[index].nome = nome
                self.contatos[index].telefone = telefone
                self.contatos[index].email = email
                self.contatos[index].favorito = favorito
                print("Contato atualizado com sucesso!")
            else:
                print("Contato não encontrado.")
        except ValueError:
            print("Entrada inválida.")

    def marcar_desmarcar_favorito(self):
        self.listar_contatos()
        if not self.contatos:
            return
        try:
            index = int(input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
            if 0 <= index < len(self.contatos):
                self.contatos[index].favorito = not self.contatos[index].favorito
                estado = "favorito" if self.contatos[index].favorito else "não favorito"
                print(f"Contato marcado como {estado}.")
            else:
                print("Contato não encontrado.")
        except ValueError:
            print("Entrada inválida.")

    def listar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if not favoritos:
            print("Nenhum contato favorito.")
        else:
            for i, contato in enumerate(favoritos, start=1):
                print(f"{i}. {contato}")

    def deletar_contato(self):
        self.listar_contatos()
        if not self.contatos:
            return
        try:
            index = int(input("Digite o número do contato que deseja deletar: ")) - 1
            if 0 <= index < len(self.contatos):
                del self.contatos[index]
                print("Contato deletado com sucesso!")
            else:
                print("Contato não encontrado.")
        except ValueError:
            print("Entrada inválida.")

    def menu(self):
        while True:
            print("\n--- MENU ---")
            print("1. Adicionar Contato")
            print("2. Listar Contatos")
            print("3. Editar Contato")
            print("4. Marcar/Desmarcar Favorito")
            print("5. Listar Favoritos")
            print("6. Deletar Contato")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.adicionar_contato()
            elif opcao == '2':
                self.listar_contatos()
            elif opcao == '3':
                self.editar_contato()
            elif opcao == '4':
                self.marcar_desmarcar_favorito()
            elif opcao == '5':
                self.listar_favoritos()
            elif opcao == '6':
                self.deletar_contato()
            elif opcao == '7':
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()
