import mysql.connector
from config.cursormysql import CursorMySql
from models.medico import Medico

class MedicoRepo():

    def _connect(self):
        return CursorMySql().create_connection()

    def create_medico(self, medico: Medico):

        query = 'INSERT INTO medico (nome, especialidade, crm) VALUES (%s, %s, %s)'
        values = (medico.nome, medico.crm, medico.especialidade)
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

    def find_medico_by_id(self, id_medico):
 
        query = 'SELECT * FROM medico WHERE id = %s'
        self.conn, self.cursor = self._connect()
        try:
            self.cursor.execute(query, (id_medico,))
            result = self.cursor.fetchone()
            if result:
                return result
            else:
                return None
        except mysql.connector.Error:
            return None
        finally:
            self.conn.close()

    def find_last_medico(self):
        query = 'SELECT * FROM medico WHERE id = (SELECT MAX(id) FROM medico)'
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

    
    def list_medico(self):
        query = 'SELECT * FROM medico'
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

    def update_medico(self, medico: Medico):
   
        query = 'UPDATE medico SET nome = %s, especialidade = %s, crm = %s WHERE id = %s'
        values = (medico.nome, medico.especialidade, medico.crm, medico.id)
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

    def delete_medico(self, id_medico):
   
        query = f"DELETE FROM medico WHERE id = {id_medico}"
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
