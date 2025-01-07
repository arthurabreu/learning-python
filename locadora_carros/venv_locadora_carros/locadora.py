import os

def mostrar_lista_de_carros(lista):
    for idx, carro in enumerate(lista, start=1):
        print(f"{idx} - {carro[0]} - R${carro[1]} por dia")

carros = [
    ["Fusca", 50],
    ["Gol", 70],
    ["Celta", 60],
    ["Uno", 65],
    ["Onix", 80],
    ["HB20", 75],
    ["Corolla", 100],
    ["Civic", 110],
    ["Cruze", 95],
    ["Compass", 120]
]

alugados = []

while True:
    print('===== LOCADORA DE CARROS =====')
    print('1 - Alugar Carro')
    print('2 - Devolver Carro')
    print('0 - Sair')
    try:
        op = int(input('Escolha uma opção: '))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        continue

    os.system('cls' if os.name == 'nt' else 'clear')

    if op == 0:
        print('Obrigado por usar a locadora!')
        break
    elif op == 1:
        if not carros:
            print('Nenhum carro disponível para alugar no momento.')
            continue

        mostrar_lista_de_carros(carros)
        
        try:
            print('Qual carro você deseja alugar? (Digite o número correspondente)')
            carro = int(input())
            if carro < 1 or carro > len(carros):
                raise IndexError

            print('Por quantos dias você deseja alugar este carro?')
            dias = int(input())
            
            os.system('cls' if os.name == 'nt' else 'clear')
            
            selected_car = carros.pop(carro - 1)
            alugados.append(selected_car)
            
            print(f'Você escolheu {selected_car[0]} por {dias} dias')
            print(f'O total a pagar é de R${selected_car[1] * dias}')
            
            print('Deseja confirmar o aluguel?')
            print('0 - SIM | 1 - NÃO')
            confirmar = int(input())
            if confirmar == 0:
                print('Carro alugado com sucesso!')
            else:
                carros.append(alugados.pop())
                print('Aluguel cancelado.')
        except IndexError:
            print("Seleção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")
    
    elif op == 2:
        if not alugados:
            print('Nenhum carro alugado no momento.')
            continue
        
        mostrar_lista_de_carros(alugados)
        
        try:
            print('Qual carro você deseja devolver? (Digite o número correspondente)')
            carro = int(input())
            if carro < 1 or carro > len(alugados):
                raise IndexError

            os.system('cls' if os.name == 'nt' else 'clear')
            
            selected_car = alugados.pop(carro - 1)
            carros.append(selected_car)
            
            print(f'Você devolveu {selected_car[0]} com sucesso!')
        except IndexError:
            print("Seleção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")
    
    else:
        print('Opção inválida. Tente novamente.')

    print('')
    print('======')
    print('0 - CONTINUAR | 1 - SAIR')
    try:
        continuar = int(input())
        if continuar == 1:
            print('Obrigado por usar a locadora!')
            break
    except ValueError:
        print("Entrada inválida. Encerrando o programa.")
        break
