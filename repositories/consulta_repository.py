import mysql.connector
from config.cursormysql import CursorMySql
from models.consulta import Consulta

class ConsultaRepo():

    def _connect(self):
        return CursorMySql().create_connection()

    def _create_consulta(self, consulta: Consulta):

        query = 'INSERT INTO consulta (data_hora, fk_medico_id, fk_paciente_id) VALUES (%s, %s, %s)'
        values = tuple(consulta.data_hora, consulta.fk_medico_id, consulta.fk_paciente_id )
        self.conn, self.cursor = self._connect()
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Registro criado com sucesso")
            return True
        except mysql.connector.Error as e:
            print(f"Erro ao criar registro: {e}")
            self.conn.rollback()
            return False
        finally:
            self.conn.close()

    def _find_consulta_by_id(self, consulta_id):
 
        query = 'SELECT * FROM consulta WHERE id = %s'
        self.conn, self.cursor = self._connect()
        try:
            self.cursor.execute(query, (consulta_id,))
            result = self.cursor.fetchone()
            if result:
                return result
            else:
                print("Registro não encontrado")
                return None
        except mysql.connector.Error as e:
            print(f"Erro ao encontrar registro: {e}")
            return None
        finally:
            self.conn.close()
    
    def _list_consultas(self):
        query = 'SELECT * FROM consultas'
        self.conn, self.cursor = self._connect()
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if result:
                return result
            else:
                print("Registro não encontrado")
                return None
        except mysql.connector.Error as e:
            print(f"Erro ao encontrar registro: {e}")
            return None
        finally:
            self.conn.close()

    def _update_consulta(self, consulta: Consulta, consulta_id):
   
        query = 'UPDATE consulta SET data_hora = %s, fk_medico_id = %s, fk_paciente_id = %s WHERE id = %s'
        values = tuple(consulta.data_hora, consulta.fk_medico_id, consulta.fk_paciente_id, consulta_id)
        self.conn, self.cursor = self._connect()

        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Registro atualizado com sucesso")
            return True
        except mysql.connector.Error as e:
            print(f"Erro ao atualizar registro: {e}")
            self.conn.rollback()
            return False
        finally:
            self.conn.close()

    def _delete_consulta(self, consulta_id):
   
        query = f"DELETE FROM consulta WHERE id = {consulta_id}"
        self.conn, self.cursor = self._connect()

        try:
            self.cursor.execute(query)
            self.conn.commit()
            print("Registro excluído com sucesso")
            return True
        except mysql.connector.Error as e:
            print(f"Erro ao excluir registro: {e}")
            self.conn.rollback()
            return False
        finally:
            self.conn.close()