from models.medico import Medico
#Não sei oq importar do repositório ainda

class Medicocontroller:
    
    def __init__(self):
        self.medicos = []

    def create(self, medico):
        self.medicos.append(medico)
        return medico

    def read(self, medico_id):
        for medico in self.medicos:
            if medico.medico_id == medico_id:
                return medico
        return None

    def update(self, medico_id, nome=None, especialidade=None, crm=None):
        medico = self.read(medico_id)
        if medico:
            if nome:
                medico.nome = nome
            if especialidade:
                medico.especialidade = especialidade
            if crm:
                medico.crm = crm
            return medico
        return None

    def delete(self, medico_id):
        medico = self.read(medico_id)
        if medico:
            self.medicos.remove(medico)
            return True
        return False
