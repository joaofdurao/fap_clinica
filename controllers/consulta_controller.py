from models.consulta import Consulta
from repositories.consulta_repository import ConsultaRepo

class ConsultaController:

    def __init__(self):
        self.consulta_repo = ConsultaRepo()

    def criar_consulta(self, data_hora, medico, paciente):
        consulta = Consulta(data_hora=data_hora, fk_medico_id=medico, fk_paciente_id=paciente)
        return self.consulta_repo._create_consulta(consulta)

    def buscar_consulta(self, consulta_id):
        return self.consulta_repo._find_consulta_by_id(consulta_id)

    def lista_consultas(self):
        return self.consulta_repo._list_consultas()

    def atualizar_consulta(self, id,data_hora, medico, paciente):
        u_consulta = Consulta(data_hora=data_hora, fk_medico_id=medico, fk_paciente_id=paciente)
        return self.consulta_repo._update_consulta(u_consulta, id)
    
    def remover_consulta(self, consulta_id):
        return self.consulta_repo._delete_consulta(consulta_id)