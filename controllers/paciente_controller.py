from tkinter import END, Toplevel, messagebox
from datetime import datetime
from models.paciente import Paciente
from views.paciente_view import PacienteView
from repositories.paciente_repository import PacienteRepo


class PacienteController:
    BR_FMT_DATE = '%d/%m/%Y'

    def __init__(self, root):
        self.root = root
        self.paciente_repo = PacienteRepo()
        self.user_view = PacienteView(Toplevel(self.root))
        self.setup_main_view()

    def setup_main_view(self):
        self.user_view.list_bt.config(command=self.show_all)
        self.user_view.find_bt.config(command=self.show_by_id)
        self.user_view.create_bt.config(command=self.insert_paciente)
        self.user_view.update_bt.config(command=self.update_slc_paciente)
        self.user_view.delete_bt.config(command=self.remove_paciente)
       
    def show_all(self):
        for i in self.user_view.treeview.get_children():
            self.user_view.treeview.delete(i)

        pacientes = self.get_all_pacientes()
        for paciente in pacientes:
            self.user_view.treeview.insert('', 'end', values=(paciente.id, paciente.nome, paciente.cpf, 
                                                                paciente.data_nascimento.strftime(self.BR_FMT_DATE), 
                                                                paciente.telefone))
        self.delete_inputs()

    def show_by_id(self, paciente_id=None):
        for i in self.user_view.treeview.get_children():
            self.user_view.treeview.delete(i)

        if not paciente_id:
            paciente_id = self.user_view.id_entry.get()

        fpaciente = self.get_paciente_by_id(paciente_id)
        paciente = Paciente(fpaciente[0], fpaciente[1], fpaciente[2], fpaciente[3], fpaciente[4])
        self.user_view.treeview.insert('', 'end', values=(paciente.id, paciente.nome, paciente.cpf, 
                                                                paciente.data_nascimento.strftime(self.BR_FMT_DATE), 
                                                                paciente.telefone))
        self.delete_inputs()

    def insert_paciente(self):
        nome = self.user_view.nome_entry.get()
        cpf = self.user_view.cpf_entry.get()
        dt_nascimento = self.user_view.dt_nasc_entry.get()
        dt_nascimento = datetime.strptime(dt_nascimento, self.BR_FMT_DATE)
        telefone = self.user_view.telefone_entry.get()
        telefone = f'({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}'

        try:
            paciente = Paciente(cpf=cpf, nome=nome, data_nascimento=dt_nascimento, telefone=telefone)
            sucesso = self.paciente_repo.create_paciente(paciente)
            if sucesso:
                messagebox.showinfo("Sucesso", "Paciente criado com sucesso.")
                lpaciente = self.paciente_repo.find_last_paciente()
                self.show_by_id(lpaciente[0])
            else:
                messagebox.showerror("Erro", "Erro ao criar Paciente")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar Paciente: {e}")

    def get_all_pacientes(self):
        pacientes_dict_list = self.paciente_repo.list_paciente()
        pacientes_obj_list = [
            Paciente(paciente[0], paciente[1], paciente[2], paciente[3], paciente[4])
            for paciente in pacientes_dict_list
        ]
        return pacientes_obj_list

    def get_paciente_by_id(self, paciente_id):
        return self.paciente_repo.find_paciente_by_id(paciente_id)

    def update_slc_paciente(self):
        selected_item = self.user_view.treeview.focus()
        if not selected_item:
            messagebox.showwarning("Aviso", "Nenhum item selecionado")
            return
        
        nome = self.user_view.nome_entry.get()
        cpf = self.user_view.cpf_entry.get()
        dt_nascimento = self.user_view.dt_nasc_entry.get()
        telefone = self.user_view.telefone_entry.get()
        slc_paciente = self.user_view.treeview.item(selected_item, 'values')
        
        if dt_nascimento:
            dt_nascimento = datetime.strptime(dt_nascimento, self.BR_FMT_DATE)
        else:
            dt_nascimento = datetime.strptime(slc_paciente[3], self.BR_FMT_DATE) 

        updt_paciente = Paciente(id=slc_paciente[0], nome=slc_paciente[1], cpf=slc_paciente[2], 
                                       data_nascimento=slc_paciente[3], telefone=slc_paciente[4])
        
        if nome and updt_paciente.nome != nome:
            updt_paciente.nome = nome

        if cpf and updt_paciente.cpf != cpf:
            updt_paciente.cpf = cpf

        if dt_nascimento and updt_paciente.data_nascimento != dt_nascimento:
            updt_paciente.data_nascimento = dt_nascimento

        if telefone and updt_paciente.telefone != telefone:
            updt_paciente.telefone = telefone

        try: 
            sucesso = self.paciente_repo.update_paciente(updt_paciente)
            if sucesso:
                messagebox.showinfo("Sucesso", "Paciente atualizado com sucesso.")
                self.show_by_id(updt_paciente.id)
            else:
                messagebox.showerror("Erro", "Erro ao atualizar Paciente.")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar Paciente: {e}")

    def remove_paciente(self):
        selected_item = self.user_view.treeview.focus()
        if not selected_item:
            messagebox.showwarning("Aviso", "Nenhum item selecionado")
            return
        
        try:
            paciente_id = self.user_view.treeview.item(selected_item, 'values')[0]
            sucesso = self.paciente_repo.delete_paciente(paciente_id)
            if sucesso:
                messagebox.showinfo("Sucesso", "Paciente deletado com sucesso.")
                self.show_all()
            else:
                messagebox.showerror("Erro", "Erro ao deletar Paciente.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar Paciente: {e}")

    def delete_inputs(self):
        self.user_view.id_entry.delete(0, END)
        self.user_view.nome_entry.delete(0, END)
        self.user_view.cpf_entry.delete(0, END)
        self.user_view.dt_nasc_entry.delete(0, END)
        self.user_view.telefone_entry.delete(0, END)
