class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        desconto = self.preco * (porcentagem / 100)
        self.preco -= desconto
        print(f"Desconto de {porcentagem}% aplicado em {self.nome}!")


class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor


class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


livro1 = Livro("Entendendo Algoritmos", 80.0, "Aditya Y. Bhargava")
tech1 = Eletronico("Mouse Gamer", 150.0, "5V")

livro1.aplicar_desconto(15)
print(f"Novo preço do livro '{livro1.nome}': R$ {livro1.preco:.2f}\n")

tech1.aplicar_desconto(10)
print(f"Novo preço do produto '{tech1.nome}': R$ {tech1.preco:.2f}")
