from pathlib import Path
import os

# Criar caminho para a primeira pasta
caminho = Path('primeira_pasta')
caminho2 = Path('primeira_pasta/segunda_pasta')
caminho3 = Path('primeira_pasta/segunda_pasta')
print(caminho)
print(caminho2)
print(type(caminho2))
print(caminho3) 
print('\n')

# Acessar ou criar caminho para os arquivos na segunda_pasta
arquivo = caminho2 / 'arquivo.txt'
print(arquivo)
print('\n')
    
for name in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    caminho_arquivo = caminho / name
    print(caminho_arquivo)
    print('\n')

home = Path.home()
print(home)
print('\n')

# Caminhos absolutos - É o caminho completo que leva até um arquivo ou diretório a partir da raiz do sistema de arquivos
caminho_absoluto = Path.cwd() / 'primeira_pasta'
print(caminho_absoluto)
print('\n')

# Caminho relativo - É o caminho que leva até um arquivo ou diretório a partir do diretório atual
caminho_relativo = Path('primeira_pasta')
print(caminho_relativo)
print('\n')

# Retornando o current working directory
cwd = Path.cwd()
print(cwd)
print('\n')

# Esse caminho é absoluto?
print(cwd.is_absolute())
print('\n')

# Retornando o caminho da primeira pasta
print(caminho)
print('\n')

# Esse caminho é absoluto?
print(caminho.is_absolute())
print('\n')

# Transformando um caminho relativo em absoluto
caminho_absoluto = caminho.resolve()
print(caminho_absoluto)
print('\n')

# Mudar o cwd
os.chdir(Path.home())
print(Path.cwd())
print('\n')

# Garantindo que estamos retornando o caminho para a pasta do script
print(__file__) # retorna todo o caminho do arquivo que estou rodando no momento
print(Path(__file__).resolve().parent) # retorna o caminho do diretório onde o arquivo está

# Trabalhando com partes de caminho
caminho4 = Path('primeira_pasta/segunda_pasta/arquivo.txt')
print(caminho4)
print(caminho4.parts)

caminho5 = Path(__file__)
print(caminho5.anchor) # retorna a parte do caminho que indica o drive ou o ponto de montagem
print(caminho5.parent) # caminho do diretório pai
print(caminho5.name) # nome do arquivo
print(caminho5.stem) # base do nome do arquivo
print(caminho5.suffix) # sufixo do nome do arquivo
print(caminho5.suffixes) # sufixo do nome do arquivo
print(caminho5.drive) # drive do caminho
