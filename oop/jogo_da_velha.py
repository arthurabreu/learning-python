class JogoDaVelha:
    def __init__(self):
        # Inicializa o tabuleiro como uma matriz 3x3 preenchida com espaços em branco
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        # Define o jogador atual como "X"
        self.jogador_atual = "X"

    def mostrar_tabuleiro(self):
        # Exibe o tabuleiro no console
        for linha in self.tabuleiro:
            print("|".join(linha))  # Mostra a linha separada por "|"
            print("-" * 5)          # Linha separadora

    def jogada_valida(self, linha, coluna):
        # Verifica se a posição está dentro dos limites e se está vazia
        return 0 <= linha < 3 and 0 <= coluna < 3 and self.tabuleiro[linha][coluna] == " "

    def fazer_jogada(self, linha, coluna):
        # Realiza a jogada se for válida
        if self.jogada_valida(linha, coluna):
            self.tabuleiro[linha][coluna] = self.jogador_atual
            return True
        return False

    def verificar_vencedor(self):
        t = self.tabuleiro
        # Verifica linhas e colunas
        for i in range(3):
            if t[i][0] == t[i][1] == t[i][2] != " ":
                return t[i][0]  # Linha completa
            if t[0][i] == t[1][i] == t[2][i] != " ":
                return t[0][i]  # Coluna completa
        # Verifica diagonais
        if t[0][0] == t[1][1] == t[2][2] != " ":
            return t[0][0]
        if t[0][2] == t[1][1] == t[2][0] != " ":
            return t[0][2]
        return None  # Ninguém venceu ainda

    def tabuleiro_cheio(self):
        # Retorna True se não houver mais espaços vazios
        return all(cell != " " for row in self.tabuleiro for cell in row)

    def trocar_jogador(self):
        # Alterna entre os jogadores "X" e "O"
        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def jogar(self):
        # Loop principal do jogo
        while True:
            self.mostrar_tabuleiro()
            print(f"Jogador {self.jogador_atual}, informe linha e coluna (0, 1 ou 2):")
            try:
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
            except ValueError:
                print("Entrada inválida. Tente novamente.")
                continue
            if not self.fazer_jogada(linha, coluna):
                print("Jogada inválida. Tente novamente.")
                continue
            vencedor = self.verificar_vencedor()
            if vencedor:
                self.mostrar_tabuleiro()
                print(f"Jogador {vencedor} venceu!")
                break
            if self.tabuleiro_cheio():
                self.mostrar_tabuleiro()
                print("Empate!")
                break
            self.trocar_jogador()

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()