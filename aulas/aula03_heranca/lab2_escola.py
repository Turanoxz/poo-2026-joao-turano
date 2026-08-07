class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir_perfil(self):
        print(f"--- {self.nome} ({self.email}) ---")


class Professor(Pessoa):
    def __init__(self, nome, cpf, email, disciplina):
        super().__init__(nome, cpf, email)
        self.disciplina = disciplina


class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, matricula):
        super().__init__(nome, cpf, email)
        self.matricula = matricula


prof = Professor("Brian", "123.456.789-00", "brian@escola.com", "Desenvolvimento de Sistemas")
aluno = Aluno("Lucas", "987.654.321-11", "lucas@aluno.com", "2026001")

prof.exibir_perfil()
print(f"Disciplina ministrada: {prof.disciplina}\n")

aluno.exibir_perfil()
print(f"Nº de Matrícula: {aluno.matricula}")
