import mysql.connector
from config.cursormysql import CursorMySql
from models.medico import Medico

class MedicoRepo():

    def _connect(self):
        return CursorMySql().create_connection()

    def _create_medico(self, medico: Medico):

        query = 'INSERT INTO medico (nome, especialidade, crm) VALUES (%s, %s, %s)'
        values = tuple(medico.nome, medico.especialidade, medico.crm)
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

    def _find_medico_by_id(self, id_medico):
 
        query = 'SELECT * FROM medico WHERE id = %s'
        self.conn, self.cursor = self._connect()
        try:
            self.cursor.execute(query, (id_medico,))
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
    
    def _list_medico(self):
        query = 'SELECT * FROM medico'
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

    def _update_medico(self, medico: Medico, id_medico):
   
        query = 'UPDATE medico SET nome = %s, especialidade = %s, crm = %s WHERE id = %s'
        values = tuple(medico.nome, medico.especialidade, medico.crm, id_medico)
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

    def _delete_medico(self, id_medico):
   
        query = f"DELETE FROM medico WHERE id = {id_medico}"
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
