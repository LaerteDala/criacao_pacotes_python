from models import Usuario, Conta

class Banco:
    def __init__(self):
        self.agencia = "0001"
        self.numero_conta = 1

    def criar_usuario(self, session):
        cpf = input("Informe o NIF (somente número): ")
        usuario = self.filtrar_usuario(session, cpf)

        if usuario:
            print("\n@@@ Já existe usuário com esse NIF! @@@")
            return None

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        novo_usuario = Usuario.novo_usuario(nif=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
        session.add(novo_usuario)
        session.commit()
        print("=== Usuário criado com sucesso! ===")
        return novo_usuario

    def filtrar_usuario(self, session, nif):
        return session.query(Usuario).filter_by(nif=nif).first()

    def criar_conta(self, session, usuario):
        if not usuario:
            print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
            return None

        nova_conta = Conta(agencia=self.agencia, numero_conta=self.numero_conta, usuario=usuario)
        session.add(nova_conta)
        session.commit()
        self.numero_conta += 1
        print("\n=== Conta criada com sucesso! ===")
        return nova_conta

    def listar_contas(self, contas):
        for conta in contas:
            linha = f"""\
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero_conta}
                Titular:\t{conta.usuario.nome}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))