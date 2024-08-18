from tkinter import END, Toplevel, messagebox
from models.medico import Medico
from views.medico_view import MedicoView
from repositories.medico_repository import MedicoRepo

class MedicoController:
    def __init__(self, root):
        self.root = root
        self.medico_repo = MedicoRepo()
        self.user_view = MedicoView(Toplevel(self.root))
        self.setup_main_view()

    def setup_main_view(self):
        self.user_view.list_bt.config(command=self.show_all)
        self.user_view.find_bt.config(command=self.show_by_id)
        self.user_view.create_bt.config(command=self.insert_medico)
        self.user_view.update_bt.config(command=self.update_slc_medico)
        self.user_view.delete_bt.config(command=self.remove_medico)

    def show_all(self):
        for i in self.user_view.treeview.get_children():
            self.user_view.treeview.delete(i)

        medicos = self.get_all_medicos()
        for medico in medicos:
            self.user_view.treeview.insert('', 'end', values=(medico.id, medico.nome, medico.especialidade, medico.crm))
        self.delete_inputs()

    def show_by_id(self, medico_id=None):
        for i in self.user_view.treeview.get_children():
            self.user_view.treeview.delete(i)

        if not medico_id:
            medico_id = self.user_view.id_entry.get()

        fmedico = self.get_medico_by_id(medico_id)
        if fmedico:
            medico = Medico(fmedico[0], fmedico[1], fmedico[2], fmedico[3])
            self.user_view.treeview.insert('', 'end', values=(medico.id, medico.nome, medico.especialidade, medico.crm))
        self.delete_inputs()

    def insert_medico(self):
        nome = self.user_view.nome_entry.get()
        crm = self.user_view.crm_entry.get()
        especialidade = self.user_view.especialidade_entry.get()
        
        try:
            medico = Medico(nome=nome, crm=crm, especialidade=especialidade)
            sucesso = self.medico_repo.create_medico(medico)    
            if sucesso:
                messagebox.showinfo("Sucesso", "Médico criado com sucesso.")
                lmedico = self.medico_repo.find_last_medico()
                self.show_by_id(lmedico[0])
            else:
                messagebox.showerror("Erro", "Erro ao criar médico")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar médico: {e}")

    def get_all_medicos(self):
        medicos_dict_list = self.medico_repo.list_medico()
        medicos_obj_list = [
            Medico(medico[0], medico[1], medico[2], medico[3])
            for medico in medicos_dict_list
        ]
        return medicos_obj_list

    def get_medico_by_id(self, medico_id):
        return self.medico_repo.find_medico_by_id(medico_id)

    def update_slc_medico(self):
        selected_item = self.user_view.treeview.focus()
        if not selected_item:
            messagebox.showwarning("Aviso", "Nenhum item selecionado")
            return
        
        nome = self.user_view.nome_entry.get()
        especialidade = self.user_view.especialidade_entry.get()
        crm = self.user_view.crm_entry.get()
        slc_medico = self.user_view.treeview.item(selected_item, 'values')

        updt_medico = Medico(id=slc_medico[0], nome=slc_medico[1], especialidade=slc_medico[2], crm=slc_medico[3])
        
        if nome and updt_medico.nome != nome:
            updt_medico.nome = nome

        if especialidade and updt_medico.especialidade != especialidade:
            updt_medico.especialidade = especialidade

        if crm and updt_medico.crm != crm:
            updt_medico.crm = crm
        
        try: 
            sucesso = self.medico_repo.update_medico(updt_medico)
            if sucesso:
                messagebox.showinfo("Sucesso", "Médico atualizado com sucesso.")
                self.show_by_id(updt_medico.id)
            else:
                messagebox.showerror("Erro", "Erro ao atualizar médico.")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar médico: {e}")

    def remove_medico(self):
        selected_item = self.user_view.treeview.focus()
        if not selected_item:
            messagebox.showwarning("Aviso", "Nenhum item selecionado")
            return
        try:
            medico_id = self.user_view.treeview.item(selected_item, 'values')[0]
            sucesso = self.medico_repo.delete_medico(medico_id)
            if sucesso:
                messagebox.showinfo("Sucesso", "Médico deletado com sucesso.")
                self.show_all()
            else:
                messagebox.showerror("Erro", "Erro ao deletar médico.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar médico: {e}")

    def delete_inputs(self):
        self.user_view.id_entry.delete(0, END)
        self.user_view.nome_entry.delete(0, END)
        self.user_view.especialidade_entry.delete(0, END)
        self.user_view.crm_entry.delete(0, END)
