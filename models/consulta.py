class Consulta:
    def __init__(self, id=None, data_hora=None, fk_medico_id=None, fk_paciente_id=None):
        self.id = id
        self.data_hora = data_hora
        self.fk_medico_id = fk_medico_id
        self.fk_paciente_id = fk_paciente_id