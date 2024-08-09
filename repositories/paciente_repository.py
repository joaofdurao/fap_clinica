from models.paciente import Paciente 

class PacienteRepository:
    def __init__(self):
        self.pacientes = []  # Lista para armazenar pacientes em memória
        self.next_id = 1     # ID automático para novos pacientes

    def _create(self, paciente):
        """
        Cria um novo paciente e o adiciona à lista.
        """
        paciente.id = self.next_id
        self.next_id += 1
        self.pacientes.append(paciente)
        return paciente

    def _read(self, id_paciente):
        """
        Obtém um paciente da lista pelo ID.
        """
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return paciente
        return None

    def _update(self, paciente_atualizado):
        """
        Atualiza um paciente existente na lista.
        """
        for i, paciente in enumerate(self.pacientes):
            if paciente.id == paciente_atualizado.id:
                self.pacientes[i] = paciente_atualizado
                return paciente_atualizado
        return None

    def _delete(self, id_paciente):
        """
        Remove um paciente da lista pelo ID.
        """
        for i, paciente in enumerate(self.pacientes):
            if paciente.id == id_paciente:
                del self.pacientes[i]
                return True
        return False

    def _list_all(self):
        """
        Lista todos os pacientes.
        """
        return self.pacientes

