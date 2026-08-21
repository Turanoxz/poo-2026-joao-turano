class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, novo_salario):
        if novo_salario > 0:
            self.__salario_base = novo_salario

    def calcular_salario_final(self):
        return self.__salario_base


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    def calcular_salario_final(self):
        return super().get_salario_base() + self.bonus_gestao


class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, nivel):
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel

    def calcular_salario_final(self):
        if self.nivel == "Senior":
            return super().get_salario_base() + 1500
        return super().get_salario_base()


gerente = Gerente("Brian", "G001", 8000, 2000)
desenvolvedor = Desenvolvedor("Pericles", "D001", 6000, "Senior")

# coiso de ve o salario final, brian e muito aura.
gerente.set_salario_base(-100)
print(f"salario base depois de mudar: R$ {gerente.get_salario_base():.2f}")

print(f"{gerente.nome}: R$ {gerente.calcular_salario_final():.2f}")
print(f"{desenvolvedor.nome}: R$ {desenvolvedor.calcular_salario_final():.2f}")