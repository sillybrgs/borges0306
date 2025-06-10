from flask import Blueprint, request, jsonify
from services.usuario_services import *

usuarios_bp = Blueprint('usuarios', __name__)
@usuarios_bp.route('/usuarios', methods=['POST'])
def criar():
    dados = request.json
    novo_usuario = criar_usuario(dados)
    return jsonify(novo_usuario.to_dict()), 201

@usuarios_bp.route('/usuarios', methods=['GET'])
def listar():
    lista = listar_usuarios()
    return jsonify(lista), 200

@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['GET'])
def listar_um(id_usuario):
    usuario = listar_um_usuario(id_usuario)
    return jsonify(usuario.to_dict()), 200

usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def atualizar(id_usuario):
    usuario = atualizar_usuario(id_usuario, request.json)
    return jsonify(usuario.to_dict()), 200