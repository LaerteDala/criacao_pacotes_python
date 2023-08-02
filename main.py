from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from banco import Banco
from menu import menu


def main():
    engine = create_engine('sqlite:///banco.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    banco = Banco()

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            conta = session.query(conta).get(int(input("Informe o número da conta: ")))
            conta.depositar(valor)
            session.commit()

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            conta = session.query(conta).get(int(input("Informe o número da conta: ")))
            conta.sacar(valor)
            session.commit()

        elif opcao == "e":
            conta = session.query(conta).get(int(input("Informe o número da conta: ")))
            conta.exibir_extrato()

        elif opcao == "nu":
            banco.criar_usuario(session)

        elif opcao == "nc":
            cpf = input("Informe o CPF do usuário: ")
            usuario = banco.filtrar_usuario(session, cpf)
            banco.criar_conta(session, usuario)

        elif opcao == "lc":
            contas = session.query(conta).all()
            banco.listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
