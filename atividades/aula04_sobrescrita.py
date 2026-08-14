"""
Sistema de Bônus de Funcionários
Desafio prático de sobrescrita de métodos em Python

Demonstra conceitos de herança e polimorfismo através da sobrescrita
de métodos em diferentes tipos de funcionários.
"""


class Funcionario:
    """
    Superclasse que representa um funcionário genérico.
    
    Atributos:
        nome (str): Nome do funcionário
        salario_base (float): Salário base mensal
    """
    
    def __init__(self, nome, salario_base):
        """
        Inicializa um funcionário.
        
        Args:
            nome: Nome do funcionário
            salario_base: Salário base em reais
        """
        self.nome = nome
        self.salario_base = salario_base
    
    def calcular_bonus(self):
        """
        Calcula o bônus padrão do funcionário.
        
        Returns:
            float: 5% do salário base como bônus
        """
        return self.salario_base * 0.05


class Gerente(Funcionario):
    """
    Subclasse que representa um gerente.
    
    Sobrescreve o método calcular_bonus() para incluir um bônus
    adicional de R$ 1.000,00 além do bônus padrão.
    """
    
    def calcular_bonus(self):
        """
        Calcula o bônus do gerente.
        
        Returns:
            float: 5% do salário base + R$ 1.000,00
        """
        bonus_padrao = super().calcular_bonus()
        return bonus_padrao + 1000.00


class Vendedor(Funcionario):
    """
    Subclasse que representa um vendedor.
    
    Atributos adicionais:
        total_vendas (float): Valor total de vendas realizadas
    
    Sobrescreve o método calcular_bonus() para calcular baseado
    no volume de vendas, ignorando o bônus padrão.
    """
    
    def __init__(self, nome, salario_base, total_vendas):
        """
        Inicializa um vendedor.
        
        Args:
            nome: Nome do vendedor
            salario_base: Salário base em reais
            total_vendas: Total de vendas realizadas em reais
        """
        super().__init__(nome, salario_base)
        self.total_vendas = total_vendas
    
    def calcular_bonus(self):
        """
        Calcula o bônus do vendedor baseado no total de vendas.
        
        Returns:
            float: 10% do total de vendas
        """
        return self.total_vendas * 0.10


# Exemplo de uso e testes
if __name__ == "__main__":
    # Criando instâncias
    func1 = Funcionario("João Silva", 2000.00)
    gerente = Gerente("Maria Santos", 3000.00)
    vendedor = Vendedor("Pedro Costa", 2500.00, 5000.00)
    
    # Exibindo informações e bônus
    print("=" * 60)
    print("SISTEMA DE BÔNUS DE FUNCIONÁRIOS")
    print("=" * 60)
    
    print(f"\nFuncionário Comum:")
    print(f"  Nome: {func1.nome}")
    print(f"  Salário Base: R$ {func1.salario_base:.2f}")
    print(f"  Bônus (5%): R$ {func1.calcular_bonus():.2f}")
    
    print(f"\nGerente:")
    print(f"  Nome: {gerente.nome}")
    print(f"  Salário Base: R$ {gerente.salario_base:.2f}")
    print(f"  Bônus (5% + R$ 1.000,00): R$ {gerente.calcular_bonus():.2f}")
    
    print(f"\nVendedor:")
    print(f"  Nome: {vendedor.nome}")
    print(f"  Salário Base: R$ {vendedor.salario_base:.2f}")
    print(f"  Total de Vendas: R$ {vendedor.total_vendas:.2f}")
    print(f"  Bônus (10% das vendas): R$ {vendedor.calcular_bonus():.2f}")
    
    print("\n" + "=" * 60)
