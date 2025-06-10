from models.usuario import Usuario

usuario = []
#Variavel de controle dos IDs dos usuários
id_usuario = 0

#função de atualização dos ids dos usuários
def gerar_id_usuario():
    global id_usuario
    id_usuario += 1
    return id_usuario  
def criar_usuario(dados):
    global usuario
    for u in usuario:
        if u.email == dados['email']:
            return None, "EMAIL_DUPLICADO"
        return None, "EMAIL_DUPLICADO"
    novo_usuario = Usuario(gerar_id_usuario(), dados['nome'], dados['email'], dados['senha'])
    usuario.append(novo_usuario)
    return novo_usuario, None

def listar_usuarios():
    lista = []
    for u in usuario:
        lista.append(u.to_dict())
    return lista

def listar_um_usuario(id_usuario):
    for u in usuario:
        if u.id == id_usuario:
            return u
    return None

def atualizar_usuario(id_usuario, dados):
    for u in usuario:
        if u.id == id_usuario:
            u.nome = dados.get('nome', u.nome)
            u.email = dados.get('email', u.email)
            u.senha = dados.get('senha', u.senha)
            return u
        
def deletar_usuario(id_usuario):
    global usuario
    usuario = listar_um_usuario(id_usuario)
    if usuario:
        usuario.remove(usuario)
    return True if usuario else False