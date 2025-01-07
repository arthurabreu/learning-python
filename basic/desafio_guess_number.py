# Desafio - Crie um programa que:
# - Pergunte um número para o usuário
# - O programa deve gerar um número aleatório entre 1 e 100
# - O programa deve dizer se o número gerado é maior, menor ou igual ao número do usuário
# - O programa deve perguntar se o usuário quer jogar novamente

import random
print(f"\n\n {'-' * 10} Bem vindo ao jogo de adivinhação! {'-' * 10} \n\n")
print(f"{'*' * 10} Tente adivinhar o número que estou pensando, entre 1 e 100, em 5 tentativas... {'*' * 10} \n\n")

number_of_tries = 5 

def ask_user_number():
    return int(input('Digite um número: '))

def generate_random_number():
    return random.randint(1, 100) 

def compare_numbers(random_number):
    global number_of_tries
    while number_of_tries > 0:
        user_number = ask_user_number()
        if user_number == random_number:
            print(f'Você acertou o número! {random_number}')
            reset_game()
            return
        elif random_number > user_number:
            print(f'O número é maior que {user_number}')
        else:
            print(f'O número é menor que {user_number}')
        number_of_tries -= 1
        if number_of_tries > 0:
            print(f'Você ainda possui {number_of_tries} tentativas.')
    print('Você esgotou suas tentativas!')
    reset_game()

def reset_game():
    global number_of_tries
    number_of_tries = 5   
    play_again = input('Quer jogar novamente? (s/n) \n\n')
    if play_again.lower() == 's':
        start_game()
    elif play_again.lower() == 'n':
        print('Obrigado por jogar! Até a próxima!')

def start_game():
    compare_numbers(generate_random_number())

if __name__ == "__main__":
    start_game()