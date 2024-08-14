from models.paciente import Paciente
from repositories.paciente_repository import pacienteRepo

class pacienteController:

    def __init__(self):
        self.Paciente_repo = pacienteRepo()

    def criar_paciente(self, id_paciente, cpf, nome, data_nascimento, telefone):
        Paciente = Paciente(id_paciente=id_paciente, cpf=cpf, nome=nome, data_nascimento=data_nascimento,telefone=telefone)
        return self.Paciente_repo._create_Paciente(Paciente)

    def buscar_Paciente(self, Paciente_id):
        return self.Paciente_repo._find_Paciente_by_id(Paciente_id)

    def lista_Pacientes(self):
        return self.Paciente_repo._list_Pacientes()

    def atualizar_Paciente(self, id_paciente, cpf, nome, data_nascimento, telefone):
        u_Paciente = Paciente(id_paciente=id_paciente, cpf=cpf, nome=nome, data_nascimento=data_nascimento,telefone=telefone)
        return self.Paciente_repo._update_Paciente(u_Paciente, id)
    
    def remover_Paciente(self, Paciente_id):
        return self.Paciente_repo._delete_Paciente(Paciente_id)