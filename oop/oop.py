import random

class Academia:
    def __init__(self):
        # Pesos pares de 10 a 34 (cada um terá 2 unidades)
        self.pesos = [i for i in range(10, 36) if i % 2 == 0]
        # porta_halteres: chave = peso nominal, valor = lista com 2 slots (cada slot = peso ou 0 se vazio)
        self.porta_halteres = {}
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        # Cada peso começa com suas 2 unidades no lugar
        self.porta_halteres = {p: [p, p] for p in self.pesos}

    def snapshot(self):
        """
        Retorna string formatada mostrando estado (ex: 10:[10, 0] 12:[12,12] ...)
        """
        partes = []
        for p in self.pesos:
            partes.append(f"{p}:{self.porta_halteres[p]}")
        return " ".join(partes)

    def listar_halteres(self):
        """Lista achatada de halteres presentes na prateleira (cada unidade conta)."""
        return [p for p, slots in self.porta_halteres.items() for v in slots if v != 0]

    def listar_espacos(self):
        """
        Retorna lista de pesos que possuem pelo menos 1 espaço vazio (algum slot == 0).
        (Mantemos mesma ideia de 'pos' sendo o próprio peso)
        """
        return [p for p, slots in self.porta_halteres.items() if any(v == 0 for v in slots)]

    def halteres_em_uso(self):
        """
        Retorna lista de halteres (pesos) atualmente fora (um item por unidade ausente).
        """
        em_uso = []
        for p, slots in self.porta_halteres.items():
            faltando = sum(1 for v in slots if v == 0)
            em_uso.extend([p] * faltando)
        return em_uso

    def pegar_haltere(self, peso):
        """
        Retira UMA unidade do peso indicado (se disponível).
        Retorna o peso ou 0 se não achar.
        """
        if peso not in self.porta_halteres:
            return 0
        slots = self.porta_halteres[peso]
        for i, v in enumerate(slots):
            if v != 0:
                slots[i] = 0  # marca slot vazio
                return peso
        return 0  # nenhum disponível

    def devolver_haltere(self, pos, peso):
        """
        Devolve UMA unidade do halter 'peso' ao conjunto de slots de 'pos' (que é o próprio peso).
        Preferência: primeiro slot vazio; se cheio, sobrescreve o primeiro (degradação).
        """
        if pos not in self.porta_halteres:
            return
        slots = self.porta_halteres[pos]
        for i, v in enumerate(slots):
            if v == 0:
                slots[i] = peso
                return
        # Se chegou aqui, não havia espaço (ambos ocupados) — sobrescreve o primeiro (raro/anômalo)
        slots[0] = peso

    def calcular_caos(self):
        """
        Com dois halteres idênticos por peso, não há como ficar 'fora de lugar' (sem diferenciação de slot).
        Retornamos 0.0 para manter compatibilidade.
        """
        return 0.0

    def verificar_invariantes(self):
        """
        Garante:
        - Cada slot é 0 ou peso correto (nunca outro número).
        """
        for p, slots in self.porta_halteres.items():
            for v in slots:
                if v not in (0, p):
                    print(f"ALERTA: slot com valor inesperado: peso {p} contém {v}")

class Usuario:
    def __init__(self, tipo, academia: Academia):
        self.tipo = tipo  # 1 organizado, 2 bagunceiro
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        print("Estado ANTES de pegar:", self.academia.snapshot())
        disponiveis = self.academia.listar_halteres()
        if not disponiveis:
            print("Nenhum haltere disponível.")
            return
        escolhido = random.choice(disponiveis)
        self.peso = self.academia.pegar_haltere(escolhido)
        print(f"Usuário pegou halter de {self.peso} kg.")
        print("Estado DEPOIS de pegar:", self.academia.snapshot())

    def finalizar_treino(self):
        if self.peso == 0:
            print("Usuário não estava com halter.")
            return

        print("Estado ANTES de devolver:", self.academia.snapshot())

        if self.tipo == 1:
            # Organizado: tenta devolver no mesmo peso (sempre válido aqui)
            self.academia.devolver_haltere(self.peso, self.peso)
        else:
            # Bagunceiro: pode devolver em qualquer peso (inclusive 'misturando', mas invariantes impedem)
            # Para simular bagunça real, poderíamos escolher outro peso aleatório — mantemos correto por enquanto:
            destino = random.choice(self.academia.pesos)
            self.academia.devolver_haltere(destino, self.peso)

        self.peso = 0
        self.academia.verificar_invariantes()
        print("Estado DEPOIS de devolver:", self.academia.snapshot())
        print("Treino finalizado.")

# Exemplo de uso
if __name__ == "__main__":
    academia = Academia()
    usuarios = [Usuario(1, academia) for _ in range(3)] + [Usuario(2, academia) for _ in range(2)]

    for u in usuarios:
        print(f"\nUsuário tipo {u.tipo} iniciando treino...")
        u.iniciar_treino()
        u.finalizar_treino()
        print("Halteres em uso agora:", academia.halteres_em_uso())
        print("Disponíveis (lista achatada):", academia.listar_halteres())
        print("Espaços com vaga (tem pelo menos 1 slot vazio):", academia.listar_espacos())