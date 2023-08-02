from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nif = Column(String, unique=True, nullable=False)
    nome = Column(String, nullable=False)
    data_nascimento = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    contas = relationship("Conta", back_populates="usuario", cascade="all, delete")

    @classmethod
    def novo_usuario(cls, nif, nome, data_nascimento, endereco):
        return cls(nif=nif, nome=nome, data_nascimento=data_nascimento, endereco=endereco)


class Conta(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True)
    agencia = Column(String, nullable=False)
    numero_conta = Column(Integer, nullable=False)
    saldo = Column(Float, default=0)
    limite = Column(Float, default=500)
    extrato = Column(String, default="")
    numero_saques = Column(Integer, default=0)
    limite_saques = Column(Integer, default=3)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship("Usuario", back_populates="contas")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tKZ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.limite_saques

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tKZ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tKZ {self.saldo:.2f}")
        print("==========================================")
