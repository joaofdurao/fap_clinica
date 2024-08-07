class Paciente:
    def __init__(self, id_paciente = None, cpf = None, nome = None, data_nascimento = None, telefone = None):
        self.id_paciente = id_paciente
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone

    def __str__(self):
        return (f'O id do paciente: {self.id_paciente}\n'
                f'CPF: {self.cpf}\n'
                f'Nome: {self.nome}\n'
                f'Data de nascimento: {self.data_nascimento}\n'
                f'Telefone: {self.telefone}')

