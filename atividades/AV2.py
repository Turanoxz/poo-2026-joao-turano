class Veiculo:
    def __init__(self, modelo: str, placa: str, valor_diaria: float):
        self.__modelo = None
        self.__placa = None
        self.__valor_diaria = None
        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_valor_diaria(valor_diaria)

    def get_modelo(self):
        return self.__modelo

    def get_placa(self):
        return self.__placa

    def get_valor_diaria(self):
        return self.__valor_diaria

    def set_modelo(self, modelo):
        if not isinstance(modelo, str) or not modelo.strip():
            raise ValueError('Modelo inválido')
        self.__modelo = modelo.strip()

    def set_placa(self, placa):
        if not isinstance(placa, str) or not placa.strip():
            raise ValueError('Placa inválida')
        self.__placa = placa.strip()

    def set_valor_diaria(self, valor):
        try:
            valor = float(valor)
        except Exception:
            raise ValueError('Valor da diária deve ser numérico')
        if valor <= 0:
            raise ValueError('Valor da diária deve ser maior que zero')
        self.__valor_diaria = valor

    def calcular_aluguel(self, dias):
        try:
            dias = int(dias)
        except Exception:
            raise ValueError('Dias deve ser um número inteiro')
        if dias <= 0:
            raise ValueError('Quantidade de dias deve ser maior que zero')
        return self.__valor_diaria * dias

    def __str__(self):
        return f"{self.get_modelo()} - {self.get_placa()} (R$ {self.get_valor_diaria():.2f}/dia)"


class Carro(Veiculo):
    def __init__(self, modelo: str, placa: str, valor_diaria: float, portas: int):
        super().__init__(modelo, placa, valor_diaria)
        self.__portas = None
        self.set_portas(portas)

    def get_portas(self):
        return self.__portas

    def set_portas(self, portas):
        try:
            portas = int(portas)
        except Exception:
            raise ValueError('Portas deve ser inteiro')
        if portas <= 0:
            raise ValueError('Portas deve ser maior que zero')
        self.__portas = portas

    def calcular_aluguel(self, dias):
        base = super().calcular_aluguel(dias)
        taxa_limpeza = 50.0
        return base + taxa_limpeza

    def __str__(self):
        return f"Carro: {super().__str__()} - {self.get_portas()} portas"


class Moto(Veiculo):
    def __init__(self, modelo: str, placa: str, valor_diaria: float, cilindradas: int):
        super().__init__(modelo, placa, valor_diaria)
        self.__cilindradas = None
        self.set_cilindradas(cilindradas)

    def get_cilindradas(self):
        return self.__cilindradas

    def set_cilindradas(self, cilindradas):
        try:
            cilindradas = int(cilindradas)
        except Exception:
            raise ValueError('Cilindradas deve ser inteiro')
        if cilindradas <= 0:
            raise ValueError('Cilindradas deve ser maior que zero')
        self.__cilindradas = cilindradas

    def calcular_aluguel(self, dias):
        base = super().calcular_aluguel(dias)
        desconto = 0.10
        return base * (1 - desconto)

    def __str__(self):
        return f"Moto: {super().__str__()} - {self.get_cilindradas()} cc"


def le_int(prompt):
    while True:
        try:
            v = input(prompt).strip()
            if v == '':
                print('Entrada vazia. Tente novamente.')
                continue
            return int(v)
        except ValueError:
            print('Valor inválido. Informe um número inteiro.')


def le_float(prompt):
    while True:
        try:
            v = input(prompt).strip()
            if v == '':
                print('Entrada vazia. Tente novamente.')
                continue
            return float(v)
        except ValueError:
            print('Valor inválido. Informe um número (p.ex.: 123.45)')


def main():
    frota = []

    while True:
        print('\n=== AV2: Gestão de Frota e Locação ===')
        print('1 - Cadastrar Carro')
        print('2 - Cadastrar Moto')
        print('3 - Listar Veículos')
        print('4 - Calcular aluguel para todos (polimórfico)')
        print('5 - Calcular aluguel para um veículo')
        print('6 - Sair')

        opc = input('Escolha uma opção: ').strip()
        if not opc:
            print('Opção vazia. Tente novamente.')
            continue
        try:
            opc_int = int(opc)
        except ValueError:
            print('Opção inválida. Digite um número.')
            continue

        try:
            if opc_int == 1:
                modelo = input('Modelo do carro: ')
                placa = input('Placa: ')
                valor = le_float('Valor da diária: ')
                portas = le_int('Quantidade de portas: ')
                try:
                    carro = Carro(modelo, placa, valor, portas)
                    frota.append(carro)
                    print('Carro cadastrado com sucesso.')
                except Exception as e:
                    print(f'Erro ao cadastrar carro: {e}')

            elif opc_int == 2:
                modelo = input('Modelo da moto: ')
                placa = input('Placa: ')
                valor = le_float('Valor da diária: ')
                cilind = le_int('Cilindradas: ')
                try:
                    moto = Moto(modelo, placa, valor, cilind)
                    frota.append(moto)
                    print('Moto cadastrada com sucesso.')
                except Exception as e:
                    print(f'Erro ao cadastrar moto: {e}')

            elif opc_int == 3:
                if not frota:
                    print('Nenhum veículo cadastrado.')
                else:
                    for idx, v in enumerate(frota, 1):
                        print(f'{idx} - {v}')

            elif opc_int == 4:
                if not frota:
                    print('Nenhum veículo na frota.')
                    continue
                dias = le_int('Número de dias para calcular aluguel: ')
                for v in frota:
                    try:
                        valor = v.calcular_aluguel(dias)
                        print(f'{v.get_modelo()} ({v.get_placa()}): R$ {valor:.2f}')
                    except Exception as e:
                        print(f'Erro ao calcular para {v}: {e}')

            elif opc_int == 5:
                if not frota:
                    print('Nenhum veículo cadastrado.')
                    continue
                for idx, v in enumerate(frota, 1):
                    print(f'{idx} - {v}')
                sel = le_int('Escolha o número do veículo: ')
                sel_i = sel - 1
                if sel_i < 0 or sel_i >= len(frota):
                    print('Seleção inválida.')
                    continue
                dias = le_int('Número de dias: ')
                try:
                    valor = frota[sel_i].calcular_aluguel(dias)
                    print(f'Valor do aluguel: R$ {valor:.2f}')
                except Exception as e:
                    print(f'Erro ao calcular aluguel: {e}')

            elif opc_int == 6:
                print('Saindo...')
                break
            else:
                print('Opção inexistente. Tente novamente.')

        except Exception as e:
            print(f'Ocorreu um erro inesperado: {e}')


if __name__ == '__main__':
    main()
