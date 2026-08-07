class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas


meu_carro = Carro("Toyota", "Corolla", 4)
print(f"Marca: {meu_carro.marca} | Modelo: {meu_carro.modelo} | Portas: {meu_carro.qtd_portas}")
