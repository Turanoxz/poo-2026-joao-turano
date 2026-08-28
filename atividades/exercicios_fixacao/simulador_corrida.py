from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass


class Carro(Veiculo):
    def acelerar(self):
        print(f"Carro {self.modelo}: acelera e o motor grita.")


class Moto(Veiculo):
    def acelerar(self):
        print(f"Moto {self.modelo}: pega o vacuo e ultrapassa.")


class Caminhao(Veiculo):
    def acelerar(self):
        print(f"Caminhão {self.modelo}: pisa fundo no pedal.")


class CarroEletrico(Veiculo):
    def acelerar(self):
        print(f"Carro elétrico {self.modelo}: mete o drift na curva.")


if __name__ == "__main__":
    pista_de_corrida = [
        Carro("GTR"),
        Moto("Yamaha R1"),
        Caminhao("Mercedes"),
        CarroEletrico("Tesla")
    ]

    print("Simulação de corrida iniciada!\n")
    for veiculo in pista_de_corrida:
        veiculo.acelerar()
