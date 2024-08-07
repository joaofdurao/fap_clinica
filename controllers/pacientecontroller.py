from repositories.pacienterepository import PacienteRepository

class PacienteController:
    def __init__(self):
        self.paciente_repo = PacienteRepository()

    def create(self, nome, cpf, dt_nascimento, telefone):
        jogador = {
            'nome': nome,
            'cpf': cpf,
            'dt_nascimento': dt_nascimento,
            'telefone': telefone
        }
        return self.paciente_repo._create(jogador)

    def read(self, id_paciente):
        
    def update(self, id_paciente, novo_paciente):
       
    def delete(self, id_paciente):
        
    def list_all(self):
        