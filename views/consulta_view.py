from tkinter import Entry, Frame, Label, Button
from tkinter.ttk import Scrollbar, Treeview

class ConsultaView:
      
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Consultas")
        
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.left_frame = Frame(self.main_frame)
        self.left_frame.pack(side="left", fill="y", padx=5, pady=5)
        
        #Entries
        Label(self.left_frame, text="Id").pack(anchor="w")
        self.id_entry = Entry(self.left_frame)
        self.id_entry.pack(fill="x", pady=5)

        Label(self.left_frame, text="Data -> DD/MM/AAAA").pack(anchor="w")
        self.data_entry = Entry(self.left_frame)
        self.data_entry.pack(fill="x", pady=5)

        Label(self.left_frame, text="Hora -> HH:MM").pack(anchor="w")
        self.hora_entry = Entry(self.left_frame)
        self.hora_entry.pack(fill="x", pady=5)

        Label(self.left_frame, text="ID do Médico").pack(anchor="w")
        self.medico_id_entry = Entry(self.left_frame)
        self.medico_id_entry.pack(fill="x", pady=5)

        Label(self.left_frame, text="ID do Paciente").pack(anchor="w")
        self.paciente_id_entry = Entry(self.left_frame)
        self.paciente_id_entry.pack(fill="x", pady=5)
        
        # Botões
        self.list_bt = Button(self.left_frame, text="Ver todos")
        self.list_bt.pack(fill="x", pady=5)
        self.find_bt = Button(self.left_frame, text="Buscar")
        self.find_bt.pack(fill="x", pady=5)
        self.create_bt = Button(self.left_frame, text="Inserir")
        self.create_bt.pack(fill="x", pady=5)
        self.update_bt = Button(self.left_frame, text="Atualizar Selecionado")
        self.update_bt.pack(fill="x", pady=5)
        self.delete_bt = Button(self.left_frame, text="Deletar Selecionado")
        self.delete_bt.pack(fill="x", pady=5)
        self.close_bt = Button(self.left_frame, text="Fechar")
        self.close_bt.pack(fill="x", pady=5)
        
        self.right_frame = Frame(self.main_frame)
        self.right_frame.pack(side="right", fill="both", expand=True)
        
        self.treeview_frame = Frame(self.right_frame)
        self.treeview_frame.pack(fill="both", expand=True)
        
        #Treeview e ScrollBar
        self.columns = ("ID", "Data e Hora", "ID Médico", "Nome Médico", "Especialidade", "ID Paciente", "Nome Paciente", "CPF Paciente")
        self.treeview = Treeview(self.treeview_frame, columns=self.columns, show="headings")
        self.treeview.pack(side="left", fill="both", expand=True)

        for col in self.columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=150, anchor="center")
        
        self.scrollbar = Scrollbar(self.treeview_frame, orient="vertical", command=self.treeview.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
