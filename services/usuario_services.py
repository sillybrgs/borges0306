from models.usuario import Usuario

usuario = []
#Variavel de controle dos IDs dos usuários
id_usuario = 0

#função de atualização dos ids dos usuários
def gerar_id_usuario():
    global id_usuario
    id += 1
    return id_usuario  
def criar_usuario(dados):
    novo_usuario = Usuario(gerar_id_usuario(), dados['nome'], dados['email'], dados['senha'])
    usuario.append(novo_usuario)