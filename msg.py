from instagrapi import Client
from instagrapi.types import DirectMessage

login = '' #Usuario 
senha = '' #Senha

# Cria uma instancia do cliente
cl = Client()

# Realiza o login
cl.login(login, senha)

user_id_destinatario = cl.user_id_from_username('')    # Destinatario

# Envia uma mensagem direta
mensagem = 'Alarme'

# Envia a mensagem
result = cl.direct_send(mensagem, user_ids=[user_id_destinatario])

# Verifica se a mensagem foi enviada com sucesso
if isinstance(result, DirectMessage):
    print(f'Mensagem enviada com sucesso para o usuário {user_id_destinatario}')
else:
    print(f'Erro ao enviar mensagem: {result}')

# Logout (opcional)
cl.logout()
