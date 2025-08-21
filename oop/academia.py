import random
import seaborn as sns
import matplotlib.pyplot as plt

class Academia:
    def __init__(self):
        # Halteres pares de 10 a 34
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        # chave = posição esperada (peso), valor = peso presente (0 = vazio)
        self.porta_halteres = {}
        self.reiniciar_o_dia()
        # Para saber qual halter está em uso, mapeia: peso -> pos original
        self.halteres_em_uso = {}

    def reiniciar_o_dia(self):
        self.porta_halteres = {halter: halter for halter in self.halteres}
        self.halteres_em_uso = {}

    def listar_halteres(self):
        return [peso for peso in self.porta_halteres.values() if peso != 0]

    def listar_espacos(self):
        return [pos for pos, val in self.porta_halteres.items() if val == 0]

    def pegar_haltere(self, peso):
        for pos, val in self.porta_halteres.items():
            if val == peso:
                self.porta_halteres[pos] = 0
                self.halteres_em_uso[peso] = pos  # registra de onde saiu
                return peso
        return 0

    def devolver_haltere(self, pos, peso):
        if pos in self.porta_halteres:
            self.porta_halteres[pos] = peso
        if peso in self.halteres_em_uso:
            del self.halteres_em_uso[peso]

    def calcular_caos(self):
        deslocados = [pos for pos, val in self.porta_halteres.items() if val != 0 and pos != val]
        total_presentes = sum(1 for v in self.porta_halteres.values() if v != 0)
        return (len(deslocados) / total_presentes) if total_presentes else 0.0

    def rack_lista(self):
        """
        Retorna o rack como lista colorida:
        - Verde: halter correto no lugar
        - Vermelho: halter presente mas fora do lugar
        - Amarelo: posição vazia, mostra o número do halter que deveria estar ali
        """
        rack = []
        for halter in self.halteres:
            val = self.porta_halteres[halter]
            if val == 0:
                # Amarelo: posição vazia, mostra o número original do halter
                rack.append(f'\033[33m{halter}\033[0m')
            elif val == halter:
                # Verde: correto
                rack.append(f'\033[32m{val}\033[0m')
            else:
                # Vermelho: errado
                rack.append(f'\033[31m{val}\033[0m')
        return "[" + ", ".join(rack) + "]"

class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo  # 1 organizado, 2 bagunceiro
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        if not lista_pesos:
            self.peso = 0
            return
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_haltere(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()
        if self.peso == 0:
            return
        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_haltere(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolver_haltere(pos, self.peso)
        else:
            pos = random.choice(espacos)
            self.academia.devolver_haltere(pos, self.peso)
        self.peso = 0

if __name__ == "__main__":
    academia = Academia()
    usuarios = [Usuario(tipo=1, academia=academia) for _ in range(10)]
    usuarios += [Usuario(tipo=2, academia=academia) for _ in range(1)]
    random.shuffle(usuarios)

list_chaos = []

for k in range(50):
    academia.reiniciar_o_dia()
    for i in range(10):
        print(f"\n--- Rodada {i+1} ---")
        # Rack1: Estado inicial
        print(f"Rack1 - Estado inicial: {academia.rack_lista()}")
        random.shuffle(usuarios)
        # Rack2: Após embaralhar usuários (opcional, mas mostra que nada mudou ainda)
        print(f"Rack2 - Após embaralhar usuários (opcional, mas mostra que nada mudou ainda): {academia.rack_lista()}")
        # Rack3: Após todos iniciarem treino (pegam halteres)
        for user in usuarios:
            user.iniciar_treino()
        print(f"Rack3 - Após todos iniciarem treino (pegam halteres): {academia.rack_lista()}")
        # Rack4: Após todos finalizarem treino (devolvem halteres)
        for user in usuarios:
            user.finalizar_treino()
        print(f"Rack4 - Após todos finalizarem treino: {academia.rack_lista()}")
        print(f"Caos: {academia.calcular_caos():.0%}")
        list_chaos.append(academia.calcular_caos())
    # list_chaos.append(academia.calcular_caos())

sns.histplot(list_chaos, bins=20, color="skyblue")  # You can change bins and color
plt.xlabel("Caos (%)")           # Label for the x-axis
plt.ylabel("Frequência")         # Label for the y-axis
plt.title("Distribuição do Caos nas Simulações")  # Title for the plot
plt.tight_layout()               # Adjusts layout to fit everything
plt.show()

# Plot customization cheat-sheet (paste above your sns/plt calls)
# ---------------------------
# sns.histplot(list_chaos, bins=20, color="skyblue", edgecolor="white", alpha=0.9)
# plt.xlabel("Caos (%)", fontsize=12, color="black", labelpad=8, loc="center")
# plt.ylabel("Frequência", fontsize=12, color="black", labelpad=8)
# plt.title("Distribuição do Caos nas Simulações", fontsize=14, fontweight="bold", pad=12)
# plt.xlim(0, 1)                # limitar eixo x (ex: 0.0..1.0 se caos em fração)
# plt.ylim(0, None)             # limitar eixo y (None = automático)
# plt.grid(axis="y", alpha=0.25, linestyle="--")  # grades leves somente no eixo y
# plt.tight_layout()            # evita corte de labels/título
# plt.show()
#
# Notes:
# - color="..."         : muda cor das barras (ex: "skyblue", "#4c72b0")
# - bins=...            : número de bins/colunas do histograma
# - fontsize, color     : ajustam estilo do texto dos rótulos
# - labelpad, pad       : adicionam espaço entre rótulo/título e o eixo
# - loc for xlabel      : "left" | "center" | "right" (posicionamento do rótulo)
# - edgecolor, alpha    : ajuste fino da aparência das barras
# ---------------------------
# filepath: c:\Users\arthur\Documents\python\learning-python\oop\academia.py
# Plot customization cheat-sheet (paste above your sns/plt calls)
# ---------------------------
# sns.histplot(list_chaos, bins=20, color="skyblue", edgecolor="white", alpha=0.9)
# plt.xlabel("Caos (%)", fontsize=12, color="black", labelpad=8, loc="center")
# plt.ylabel("Frequência", fontsize=12, color="black", labelpad=8)
# plt.title("Distribuição do Caos nas Simulações", fontsize=14, fontweight="bold", pad=12)
# plt.xlim(0, 1)                # limitar eixo x (ex: 0.0..1.0 se caos em fração)
# plt.ylim(0, None)             # limitar eixo y (None = automático)
# plt.grid(axis="y", alpha=0.25, linestyle="--")  # grades leves somente no eixo y
# plt.tight_layout()            # evita corte de labels/título
# plt.show()
#
# Notes:
# - color="..."         : muda cor das barras (ex: "skyblue", "#4c72b0")
# - bins=...            : número de bins/colunas do histograma
# - fontsize, color     : ajustam estilo do texto dos rótulos
# - labelpad, pad       : adicionam espaço entre rótulo/título e o eixo
# - loc for xlabel      : "left" | "center" | "right" (posicionamento do rótulo)
# - edgecolor, alpha    : ajuste fino da aparência das