from models.medico import Medico
from repositories.medico_repository import medicoRepo

class medicoController:
    
    def __init__(self):
        self.Medico_repo = medicoRepo()

    def criar_Medico(self, medico_id, nome, especialidade, crm):
        Medico = Medico(medico_id = medico_id, nome = nome, especialidade = especialidade, crm = crm)
        return self.Medico_repo._create_Medico(Medico)

    def buscar_Medico(self, medico_id):
        return self.Medico_repo._find_Medico_by_id(medico_id)

    def lista_Medicos(self):
        return self.Medico_repo._list_Medicos()

    def atualizar_Medico(self, medico_id, nome, especialidade, crm):
        u_Medico = Medico(medico_id = medico_id, nome = nome, especialidade = especialidade, crm = crm)
        return self.Medico_repo._update_Medico(u_Medico, id)
    
    def remover_Medico(self, medico_id):
        return self.Medico_repo._delete_Medico(medico_id)
    
    
