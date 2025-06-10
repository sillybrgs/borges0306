from flask import Blueprint, request, jsonify
from services.usuario_services import *
from utils.mensagens_erro import ERROS 

usuarios_bp = Blueprint('usuario', __name__)
@usuarios_bp.route('/usuario', methods=['POST'])
def criar():
    dados = request.json
    novo_usuario, erro = criar_usuario(dados)
    if erro:
        erro_info = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": erro_info["mensagem"], "detalhes": erro_info.get("detalhes", "")}), erro_info["status"]
    return jsonify(novo_usuario.to_dict()), 201

@usuarios_bp.route('/usuario', methods=['GET'])
def listar():
    lista = listar_usuarios()
    return jsonify(lista), 200

@usuarios_bp.route('/usuario/<int:id_usuario>', methods=['GET'])
def listar_um(id_usuario):
    usuario = listar_um_usuario(id_usuario)
    return jsonify(usuario.to_dict()), 200

usuarios_bp.route('/usuario/<int:id_usuario>', methods=['PATCH','PUT'])
def atualizar(id_usuario):
    usuario = atualizar_usuario(id_usuario, request.json)
    return jsonify(usuario.to_dict()), 200

@usuarios_bp.route('/usuario/<int:id_usuario>', methods=['DELETE'])
def deletar(id_usuario):
    sucesso = deletar_usuario(id_usuario)
    if sucesso:
        return jsonify({'message': 'Usuário deletado com sucesso.'}), 204
    else:
        return jsonify({'message': 'Usuário não encontrado.'}), 404