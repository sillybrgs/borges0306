from flask import Blueprint, request, jsonify
from services.usuario_services import *

usuarios_bp = Blueprint('usuarios', __name__)
@usuarios_bp.route('/usuarios', methods=['POST'])
def criar():
    dados = request.json
