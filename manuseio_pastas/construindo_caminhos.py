from pathlib import Path
import os
import shutil 

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


# Encontrando arquivos e diretórios
caminho6 = Path.home() / 'Downloads'
print(caminho6)

caminho7 = Path.home()
for arquivo in caminho7.glob('**/*'):
    if arquivo.is_file():
        if arquivo.name == 'arquivo_primeira_pasta.txt':
            print(f'Arquivo encontrado: {arquivo}')

# tamanho do arquivo
os.path.getsize(caminho7)
def return_file_size(path, profundidade=0):
    """
    Retorna o tamanho dos arquivos em um diretório e suas subpastas.
    
    :param path: Caminho do diretório.
    :param profundidade: Nível de profundidade para listar os arquivos.
    :return: Tamanho total dos arquivos encontrados.
    """
    total_size = 0
    for item in path.rglob('*'):
        if item.is_file():
            total_size += item.stat().st_size
            if item.parent.name == 'Downloads' and profundidade == 1:
                print(f'Arquivo: {item}, Tamanho: {item.stat().st_size} bytes')
    return total_size
return_file_size(Path.home() / 'Downloads', profundidade=1)

# copiando, movendo e removendo arquivos

# copiando arquivo com copyfile
pasta_atual = Path(__file__).parent
caminho_arquivo_origem = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino1' / 'texto.txt'

shutil.copyfile(caminho_arquivo_origem, caminho_arquivo_destino)

# copiando arquivo com copy
shutil.copy(caminho_arquivo_origem, caminho_arquivo_destino)

# copiando arquivo com copy2
shutil.copy2(caminho_arquivo_origem, caminho_arquivo_destino)

# movendo arquivos
shutil.move(caminho_arquivo_destino, pasta_atual / 'destino2' / 'texto.txt')

# deletando arquivos
caminho_arquivo_para_deletar = pasta_atual / 'destino2' / 'texto.txt'

# criando pasta
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino4'
caminho_pasta_destino.mkdir(parents=True, exist_ok=True)

# criando pasta com todas as pastas anteriores necessarias
caminho_pasta_destino2 = pasta_atual / 'destino5' / 'subpasta'
caminho_pasta_destino2.mkdir(parents=True) # cria todas as pastas necessárias, se não existirem

# copiando pasta
shutil.copytree(pasta_atual / 'destino1', pasta_atual / 'destino1' / 'destino5') # copia a pasta destino1 para destino5 dentro de destino1

# deletando pastas vazias
shutil.rmtree(caminho_pasta_destino, ignore_errors=True)  # remove a pasta destino4 e seu conteúdo

# deletando pastas com conteúdo
shutil.rmtree(caminho_pasta_destino2, ignore_errors=True)  # remove a pasta destino5 e seu conteúdo

# compactando arquivos
import zipfile
caminho_zip = pasta_atual / 'destino1' / 'arquivo.zip'

# descompactando arquivos
with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
    zip_ref.extractall(pasta_atual / 'destino1' / 'descompactado')

# compactando arquivos com shutil
shutil.make_archive(pasta_atual / 'destino1' / 'arquivo', 'zip', pasta_atual / 'destino1')

# descompactando arquivos com shutil
shutil.unpack_archive(pasta_atual / 'destino1' / 'arquivo.zip', pasta_atual / 'destino1' / 'descompactado_shutil')

# organizando arquivos por extensão
from collections import defaultdict
def organizar_arquivos_por_extensao(diretorio):
    """
    Organiza arquivos por extensão em subpastas dentro do diretório especificado.
    
    :param diretorio: Caminho do diretório onde os arquivos serão organizados.
    """
    diretorio = Path(diretorio)
    extensoes = defaultdict(list)

    # Agrupa arquivos por extensão
    for arquivo in diretorio.glob('*.*'):
        if arquivo.is_file():
            extensao = arquivo.suffix.lower()
            extensoes[extensao].append(arquivo)

    # Cria subpastas e move os arquivos
    for ext, arquivos in extensoes.items():
        pasta_ext = diretorio / ext.lstrip('.')
        pasta_ext.mkdir(exist_ok=True)
        for arquivo in arquivos:
            shutil.move(arquivo, pasta_ext / arquivo.name)

# lendo arquivos de texto
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    print(lista_compras.read())

# lendo linha a linha
with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    for linha in lista_compras:
        print(linha.strip())
        print(lista_compras.readline())

# lendo todas as linhas
with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    for linha in lista_compras:
        print(lista_compras.readlines())

# escrevendo em arquivos de texto
with open(pasta_atual / 'lista_de_compras.txt', 'a') as lista_compras:
    lista_compras.write('\n- tomate\n- cebola\n- alface')

# escrevendo linha a linha
with open(pasta_atual / 'lista_de_compras.txt', 'a') as lista_compras:
    for item in ['- tomate', '- cebola', '- alface']:
        lista_compras.write(f'\n{item}')


