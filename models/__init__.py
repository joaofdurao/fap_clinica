class Paciente:
    def __init__(self, id_paciente, cpf, nome, data_nascimento):
        self.id_paciente = id_paciente
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return (f'O id do paciente: {self.id_paciente}\n'
                f'CPF: {self.cpf}\n'
                f'Nome: {self.nome}\n'
                f'Data de nascimento: {self.data_nascimento}')

class PacienteRepository:
    def __init__(self):
        self.pacientes = {}

    def create(self, paciente):
        if paciente.id_paciente in self.pacientes:
            return f'Paciente com ID {paciente.id_paciente} já existe.'
        self.pacientes[paciente.id_paciente] = paciente
        return f'Paciente {paciente.nome} adicionado com sucesso.'

    def read(self, id_paciente):
        paciente = self.pacientes.get(id_paciente)
        if paciente:
            return paciente
        return 'Paciente não encontrado.'

    def update(self, id_paciente, novo_paciente):
        if id_paciente not in self.pacientes:
            return 'Paciente não encontrado.'
        self.pacientes[id_paciente] = novo_paciente
        return f'Paciente {id_paciente} atualizado com sucesso.'

    def delete(self, id_paciente):
        if id_paciente not in self.pacientes:
            return 'Paciente não encontrado.'
        del self.pacientes[id_paciente]
        return f'Paciente {id_paciente} deletado com sucesso.'

    def list_all(self):
        return list(self.pacientes.values())