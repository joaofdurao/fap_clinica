import mysql.connector
from config.cursormysql import CursorMySql
from models.paciente import Paciente

class PacienteRepo():

    def _connect(self):
        return CursorMySql().create_connection()

    def create_paciente(self, paciente: Paciente):
        query = 'INSERT INTO paciente (nome, cpf, data_nascimento, telefone) VALUES (%s, %s, %s, %s)'
        values = (paciente.nome, paciente.cpf, paciente.data_nascimento, paciente.telefone)
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

    def find_paciente_by_id(self, paciente_id):
 
        query = 'SELECT * FROM paciente WHERE id = %s'
        self.conn, self.cursor = self._connect()
        try:
            self.cursor.execute(query, (paciente_id,))
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
    
    def find_last_paciente(self):
        query = 'SELECT * FROM paciente WHERE id = (SELECT MAX(id) FROM paciente)'
        self.conn, self.cursor = self._connect()
        try:
            self.cursor.execute(query)
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


    def list_paciente(self):
        query = 'SELECT * FROM paciente'
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

    def update_paciente(self, paciente: Paciente):
   
        query = 'UPDATE paciente SET cpf = %s, nome = %s, data_nascimento = %s, telefone = %s WHERE id = %s'
        values = (paciente.cpf, paciente.nome, paciente.data_nascimento, paciente.telefone, paciente.id)
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

    def delete_paciente(self, paciente_id):
   
        query = f"DELETE FROM paciente WHERE id = {paciente_id}"
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