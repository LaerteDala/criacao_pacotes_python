from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from banco import Banco
from menu import menu

app = Flask(__name__)

engine = create_engine('sqlite:///db.sqlite', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

banco = Banco()

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    novo_usuario = banco.criar_usuario(session, data['nif'], data['nome'], data['data_nascimento'], data['endereco'])
    return jsonify({'message': 'Usuário criado com sucesso!', 'usuario_id': novo_usuario.id})

# Adicione mais rotas para as outras operações (criar conta, depósito, saque, extrato, listar contas)

if __name__ == '__main__':
    app.run(debug=True)
