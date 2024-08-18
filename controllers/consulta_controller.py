from tkinter import END, Toplevel, messagebox
from models.consulta import Consulta
from views.consulta_view import ConsultaView
from repositories.consulta_repository import ConsultaRepo

class ConsultaController:
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
            self.consulta_view.treeview.insert('', 'end', values=(consulta.id, consulta.data_hora, consulta.fk_medico_id, consulta.fk_paciente_id))
        self.delete_inputs()

    def show_by_id(self, consulta_id=None):
        for i in self.consulta_view.treeview.get_children():
            self.consulta_view.treeview.delete(i)

        if not consulta_id:
            consulta_id = self.consulta_view.id_entry.get()

        fconsulta = self.get_consulta_by_id(consulta_id)
        if fconsulta:
            consulta = Consulta(fconsulta[0], fconsulta[1], fconsulta[2], fconsulta[3])
            self.consulta_view.treeview.insert('', 'end', values=(consulta.id, consulta.data_hora, consulta.fk_medico_id, consulta.fk_paciente_id))
        else:
            messagebox.showerror("Erro", "Consulta não encontrada.")
        self.delete_inputs()

    def insert_consulta(self):
        data_hora = self.consulta_view.data_hora_entry.get()
        fk_medico_id = self.consulta_view.fk_medico_id_entry.get()
        fk_paciente_id = self.consulta_view.fk_paciente_id_entry.get()
        consulta = Consulta(data_hora=data_hora, fk_medico_id=fk_medico_id, fk_paciente_id=fk_paciente_id)

        sucesso = self.consulta_repo._create_consulta(consulta)
        if sucesso:
            messagebox.showinfo("Sucesso", "Consulta criada com sucesso.")
            self.show_all()
        else:
            messagebox.showerror("Erro", "Erro ao criar consulta.")

    def get_all_consultas(self):
        consultas_dict_list = self.consulta_repo._list_consultas()
        consultas_obj_list = [
            Consulta(consulta[0], consulta[1], consulta[2], consulta[3])
            for consulta in consultas_dict_list
        ]
        return consultas_obj_list

    def get_consulta_by_id(self, consulta_id):
        return self.consulta_repo._find_consulta_by_id(consulta_id)

    def update_slc_consulta(self):
        selected_item = self.consulta_view.treeview.focus()
        if not selected_item:
            messagebox.showerror("Erro", "Nenhum item selecionado.")
            return
        
        data_hora = self.consulta_view.data_hora_entry.get()
        fk_medico_id = self.consulta_view.fk_medico_id_entry.get()
        fk_paciente_id = self.consulta_view.fk_paciente_id_entry.get()
        slc_consulta = self.consulta_view.treeview.item(selected_item, 'values')
        
        updt_consulta = Consulta(id=slc_consulta[0], data_hora=data_hora, fk_medico_id=fk_medico_id, fk_paciente_id=fk_paciente_id)
        sucesso = self.consulta_repo._update_consulta(updt_consulta, slc_consulta[0])
        if sucesso:
            messagebox.showinfo("Sucesso", "Consulta atualizada com sucesso.")
            self.show_all()
        else:
            messagebox.showerror("Erro", "Erro ao atualizar consulta.")

    def remove_consulta(self):
        selected_item = self.consulta_view.treeview.focus()
        if not selected_item:
            messagebox.showerror("Erro", "Nenhum item selecionado.")
            return

        consulta_id = self.consulta_view.treeview.item(selected_item, 'values')[0]
        sucesso = self.consulta_repo._delete_consulta(consulta_id)
        if sucesso:
            messagebox.showinfo("Sucesso", "Consulta deletada com sucesso.")
            self.show_all()
        else:
            messagebox.showerror("Erro", "Erro ao deletar consulta.")

    def delete_inputs(self):
        self.consulta_view.id_entry.delete(0, END)
        self.consulta_view.data_hora_entry.delete(0, END)
        self.consulta_view.fk_medico_id_entry.delete(0, END)
        self.consulta_view.fk_paciente_id_entry.delete(0, END)
