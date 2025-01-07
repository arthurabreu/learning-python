# Crie um programa que solicite ao usuário um nome de usuário e uma senha.
# Se ambos forem corretos, exiba uma mensagem de boas-vindas.
# Se o nome de usuário ou a senha estiverem incorretos, exiba uma mensagem de erro adequada.
# A mensagem é diferente quando o usuário esta incorretos ou a senha esta incorreta.
# O usuário e a senha corretos podem ser definidos como variaveis dentro do proprio codigo

correct_user = "admin"	
correct_password = "mrrobot"	
user = input('Digite seu usuário: ') == correct_user
password = input('Digite sua senha: ') == correct_password

def check_credentials(user, password):
    if user and password:
        return f'Bem-vindo {correct_user}!'
    elif user and password == False:
        return 'Senha incorreta.'
    else:
        return 'Usuário não cadastrado.'

print(check_credentials(user, password))