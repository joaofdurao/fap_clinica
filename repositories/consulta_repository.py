import mysql.connector
from config.cursormysql import CursorMySql
from models.consulta import Consulta

class ConsultaRepo():

    def _connect(self):
        return CursorMySql().create_connection()

    def create_consulta(self, consulta: Consulta):

        query = 'INSERT INTO consulta (data_hora, medico_id, paciente_id) VALUES (%s, %s, %s)'
        values = (consulta.data_hora, consulta.medico_id, consulta.paciente_id)
        self.conn, self.cursor = self._connect()
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            return True
        except mysql.connector.Error:
            self.conn.rollback()
            return False
        finally:
            self.conn.close()

    def find_consulta_by_id(self, consulta_id):
 
        query = ('SELECT consulta.id, consulta.data_hora, '
                'medico.id AS medico_id, medico.nome AS medico_nome, medico.especialidade AS medico_especialidade, '
                'paciente.id AS paciente_id, paciente.nome AS paciente_nome, paciente.cpf AS paciente_cpf '
                'FROM consulta '
                'INNER JOIN medico ON consulta.medico_id = medico.id '
                'INNER JOIN  paciente ON consulta.paciente_id = paciente.id '
                'WHERE consulta.id = %s')
        self.conn, self.cursor = self._connect()
        try:
            self.cursor.execute(query, (consulta_id,))
            result = self.cursor.fetchone()
            if result:
                return result
            else:
                return None
        except mysql.connector.Error:
            return None
        finally:
            self.conn.close()

    def find_last_consulta(self):
        query = ('SELECT consulta.id, consulta.data_hora, '
                'medico.id AS medico_id, medico.nome AS medico_nome, medico.especialidade AS medico_especialidade, '
                'paciente.id AS paciente_id, paciente.nome AS paciente_nome, paciente.cpf AS paciente_cpf '
                'FROM consulta '
                'INNER JOIN medico ON consulta.medico_id = medico.id '
                'INNER JOIN paciente ON consulta.paciente_id = paciente.id '
                'WHERE consulta.id = (SELECT MAX(id) FROM consulta)')
        self.conn, self.cursor = self._connect()
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            if result:
                return result
            else:
                return None
        except mysql.connector.Error:
            return None
        finally:
            self.conn.close()
    
    def list_consultas(self):
        query = ('SELECT consulta.id, consulta.data_hora, '
                'medico.id AS medico_id, medico.nome AS medico_nome, medico.especialidade AS medico_especialidade, '
                'paciente.id AS paciente_id, paciente.nome AS paciente_nome, paciente.cpf AS paciente_cpf '
                'FROM consulta '
                'INNER JOIN medico ON consulta.medico_id = medico.id '
                'INNER JOIN  paciente ON consulta.paciente_id = paciente.id')
        self.conn, self.cursor = self._connect()
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if result:
                return result
            else:
                return None
        except mysql.connector.Error:
            return None
        finally:
            self.conn.close()

    def update_consulta(self, consulta: Consulta):
   
        query = 'UPDATE consulta SET data_hora = %s, medico_id = %s, paciente_id = %s WHERE id = %s'
        values = (consulta.data_hora, consulta.medico_id, consulta.paciente_id, consulta.id)
        self.conn, self.cursor = self._connect()

        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            return True
        except mysql.connector.Error:
            self.conn.rollback()
            return False
        finally:
            self.conn.close()

    def delete_consulta(self, consulta_id):
   
        query = f"DELETE FROM consulta WHERE id = {consulta_id}"
        self.conn, self.cursor = self._connect()

        try:
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except mysql.connector.Error:
            self.conn.rollback()
            return False
        finally:
            self.conn.close()