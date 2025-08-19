# Tutorial de Git e GitHub com python

# - cria-se uma pasta local
# - abre pelo cmd
# - mkdir meu-projeto
# - cd meu-projeto
# - git init // Inicializa o git nesta pasta
# - echo "print('Hello World')" > hello.py // Cria arquivo python com cmd
# - gits status // para ver os arquivos untracked, nao rastreado pelo git
# - git add hello.py // comando para o git comecar a rastrear aquele arquivo que criamos
# - git add . // olha todos os arquivos da pasta e prepare eles para virar um ponto de salvamento
# - git commit -m "Adiciona o arquivo hello.py" // cria um ponto de salvamento com mensagem de commit para descricao do que esta sendo adicionado
# - git log // acessa historico de salvamento do meu repositorio git, conseguimos ver se o commit funcionou por aqui
# - hash // identificador unico do commit (commit - 9a8d$%&^&98a9f89s8g9s <- cod hexadecimal)
# - git branch -M main // renomeia a branch atual para main
# - git remote add origin https://github.com/usuario/meu-projeto.git // adiciona o repositório remoto
# - git push -u origin main // envia as alterações locais para o repositório remoto
print("Iniciando o tutorial de Git e GitHub com Python...")