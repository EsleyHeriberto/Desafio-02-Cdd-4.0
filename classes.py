import random

class Jogador():
    def __init__(self, nome):
        self.nome = nome
        self.escolha = None

    def escolher(self):
        escolhas = ["Pedra", "Papel", "Tesoura"]
        self.escolha = random.choice(escolhas)
        print(f"{self.nome} escolheu {self.escolha}")
        return self.escolha

class JogadorHumano(Jogador):
    def escolher(self):
        while True:
            escolha = input(f"{self.nome}, escolha entre Pedra, Papel ou Tesoura: ").capitalize()
            if escolha in ["Pedra", "Papel", "Tesoura"]:
                self.escolha = escolha
                print(f"{self.nome} escolheu {self.escolha}")
                return self.escolha
            else:
                print("Escolha inválida, tente novamente.")

class Jogo():
    def __init__(self):
        self.JogadorHumano = JogadorHumano("Pessoa")
        self.computador = Jogador("O computador")

    def determinarVencedor(self, escolha1, escolha2):
        if escolha1 == escolha2:
            return "Empate"
        elif (escolha1 == "Pedra" and escolha2 == "Tesoura") or (escolha1 == "Papel" and escolha2 == "Pedra") or (escolha1 == "Tesoura" and escolha2 == "Papel"):
            return f"{self.JogadorHumano.nome} venceu!"
        else:
            return f"{self.computador.nome} venceu!"

    def jogar(self):
        escolha1 = self.JogadorHumano.escolher()
        escolha2 = self.computador.escolher()
        resultado = self.determinarVencedor(escolha1, escolha2)
        print(resultado)
