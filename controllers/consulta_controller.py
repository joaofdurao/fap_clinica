from datetime import datetime
from tkinter import END, Toplevel, messagebox
from models.consulta import Consulta
from views.consulta_view import ConsultaView
from repositories.consulta_repository import ConsultaRepo

class ConsultaController:
    BR_FMT_DATE_TIME = "%d/%m/%Y %H:%M"
    BR_FMT_DATE = "%d/%m/%Y"
    BR_FMT_TIME = "%H:%M"

    def __init__(self, root):
        self.root = root
        self.consulta_repo = ConsultaRepo()
        self.consulta_view = ConsultaView(Toplevel(self.root))
        self.setup_main_view()

    def setup_main_view(self):
        self.consulta_view.list_bt.config(command=self.show_all)
        self.consulta_view.find_bt.config(command=self.show_by_id)
        self.consulta_view.create_bt.config(command=self.insert_consulta)
        self.consulta_view.update_bt.config(command=self.update_slc_consulta)
        self.consulta_view.delete_bt.config(command=self.remove_consulta)

    def show_all(self):
        for i in self.consulta_view.treeview.get_children():
            self.consulta_view.treeview.delete(i)

        consultas = self.get_all_consultas()
        for consulta in consultas:
            self.consulta_view.treeview.insert('', 'end', values=(consulta[0], datetime.strftime(consulta[1], self.BR_FMT_DATE_TIME), consulta[2], consulta[3],
                                                                  consulta[4], consulta[5], consulta[6], consulta[7]))
        self.delete_inputs()

    def show_by_id(self, consulta_id=None):
        for i in self.consulta_view.treeview.get_children():
            self.consulta_view.treeview.delete(i)

        if not consulta_id:
            consulta_id = self.consulta_view.id_entry.get()

        consulta = self.get_consulta_by_id(consulta_id)
        self.consulta_view.treeview.insert('', 'end', values=(consulta[0], datetime.strftime(consulta[1], self.BR_FMT_DATE_TIME), consulta[2], consulta[3],
                                                              consulta[4], consulta[5], consulta[6], consulta[7]))
        self.delete_inputs()

    def insert_consulta(self):
        data = self.consulta_view.data_entry.get()
        data = datetime.strptime(data, self.BR_FMT_DATE).date()
        hora = self.consulta_view.hora_entry.get()
        hora = datetime.strptime(hora, self.BR_FMT_TIME).time()
        data_hora = datetime.combine(data, hora)
        medico_id = self.consulta_view.medico_id_entry.get()
        paciente_id = self.consulta_view.paciente_id_entry.get()

        try:
            consulta = Consulta(data_hora=data_hora, medico_id=medico_id, paciente_id=paciente_id)
            sucesso = self.consulta_repo.create_consulta(consulta)
            if sucesso:
                messagebox.showinfo("Sucesso", "Consulta criada com sucesso.")
                lconsulta = self.consulta_repo.find_last_consulta()
                self.show_by_id(lconsulta[0])
            else:
                messagebox.showerror("Erro", "Erro ao criar Consulta")

        except Exception as e:
            messagebox.showerror("Erro", f'Erro ao criar Consulta: {e}')

    def get_all_consultas(self):
        return self.consulta_repo.list_consultas()

    def get_consulta_by_id(self, consulta_id):
        return self.consulta_repo.find_consulta_by_id(consulta_id)

    def update_slc_consulta(self):
        selected_item = self.consulta_view.treeview.focus()
        if not selected_item:
            messagebox.showwarning("Aviso", "Nenhum item selecionado")
            return
        
        data = self.consulta_view.data_entry.get()
        hora = self.consulta_view.hora_entry.get()
        medico_id = self.consulta_view.medico_id_entry.get()
        paciente_id = self.consulta_view.paciente_id_entry.get()
        slc_consulta = self.consulta_view.treeview.item(selected_item, 'values')

        if data and hora:
            data = datetime.strptime(data, self.BR_FMT_DATE).date()
            hora = datetime.strptime(hora, self.BR_FMT_TIME).time() 
            data_hora = datetime.combine(data, hora)
        elif data:
            data = datetime.strptime(data, self.BR_FMT_DATE).date()
            hora = datetime.strptime(slc_consulta[1], self.BR_FMT_DATE_TIME).time()
            data_hora = datetime.combine(data, hora) 
        elif hora:
            data = datetime.strptime(slc_consulta[1], self.BR_FMT_DATE_TIME).date()
            hora = datetime.strptime(hora, self.BR_FMT_TIME).time() 
            data_hora = datetime.combine(data, hora) 
        else:
            data_hora = datetime.strptime(slc_consulta[1], self.BR_FMT_DATE_TIME) 

        updt_consulta = Consulta(id=slc_consulta[0], data_hora=slc_consulta[1], medico_id=slc_consulta[2], paciente_id=slc_consulta[5])

        if data_hora and updt_consulta.data_hora != data_hora:
            updt_consulta.data_hora = data_hora

        if medico_id and updt_consulta.medico_id != medico_id:
            updt_consulta.medico_id = medico_id

        if paciente_id and updt_consulta.paciente_id != paciente_id:
            updt_consulta.paciente_id = paciente_id

        try: 
            sucesso = self.consulta_repo.update_consulta(updt_consulta)
            if sucesso:
                messagebox.showinfo("Sucesso", "Consulta atualizada com sucesso.")
                self.show_by_id(updt_consulta.id)
            else:
                messagebox.showerror("Erro", "Erro ao atualizar Consulta.")

        except Exception as e:
            messagebox.showerror("Erro", f'Erro ao atualizar Consulta: {e}')

    def remove_consulta(self):
        selected_item = self.consulta_view.treeview.focus()
        if not selected_item:
            messagebox.showwarning("Aviso", "Nenhum item selecionado")
            return

        try:
            consulta_id = self.consulta_view.treeview.item(selected_item, 'values')[0]
            sucesso = self.consulta_repo.delete_consulta(consulta_id)
            if sucesso:
                messagebox.showinfo("Sucesso", "Consulta deletada com sucesso.")
                self.show_all()
            else:
                messagebox.showerror("Erro", "Erro ao deletar Consulta.")
        except Exception as e:
            messagebox.showerror("Erro", f'Erro ao deletar Consulta: {e}')

    def delete_inputs(self):
        self.consulta_view.id_entry.delete(0, END)
        self.consulta_view.data_entry.delete(0, END)
        self.consulta_view.hora_entry.delete(0, END)
        self.consulta_view.medico_id_entry.delete(0, END)
        self.consulta_view.paciente_id_entry.delete(0, END)
