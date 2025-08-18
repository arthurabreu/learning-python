import pickle
import pathlib

# salvando arquivos pickle
minha_lista = [0, 1, 2, 3]
meu_dict = {'a': 1, 'b': 2, 'c': 3}

# wb - writes in bytes
# ab - appends in bytes
# rb - reads in bytes
# construct a path to the dados.pickle file inside this script's directory
dados_path = pathlib.Path(__file__).parent / 'dados.pickle'

with dados_path.open('wb') as f:
    pickle.dump((minha_lista, meu_dict), f)

# lendo arquivos pickle
with dados_path.open('rb') as f:
    lista_carregada, dict_carregado = pickle.load(f)

print(lista_carregada)
print(dict_carregado)

# salvando a instancia de uma classe com pickle
class MinhaClasse:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

minha_instancia = MinhaClasse("João", 30)

with dados_path.open('wb') as f:
    pickle.dump(minha_instancia, f)

# lendo a instancia de uma classe com pickle
with dados_path.open('rb') as f:
    instancia_carregada = pickle.load(f)

print(instancia_carregada.nome)
print(instancia_carregada.idade)