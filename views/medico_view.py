from tkinter import Entry, Frame, Label, Button
from tkinter.ttk import Scrollbar, Treeview

class MedicoView:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Médicos")
        
        # Configuração do frame principal
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Frame esquerdo para os campos de entrada e botões
        self.left_frame = Frame(self.main_frame)
        self.left_frame.pack(side="left", fill="y", padx=5, pady=5)
        
        # Campos de entrada para os dados do médico
        Label(self.left_frame, text="Id").pack(anchor="w")
        self.id_entry = Entry(self.left_frame)
        self.id_entry.pack(fill="x", pady=5)

        Label(self.left_frame, text="Nome").pack(anchor="w")
        self.nome_entry = Entry(self.left_frame)
        self.nome_entry.pack(fill="x", pady=5)

        Label(self.left_frame, text="Especialidade").pack(anchor="w")
        self.espacialidade_entry = Entry(self.left_frame)
        self.espacialidade_entry.pack(fill="x", pady=5)

        Label(self.left_frame, text="CRM").pack(anchor="w")
        self.crm_entry = Entry(self.left_frame)
        self.crm_entry.pack(fill="x", pady=5)

        # Botões
        self.list_bt = Button(self.left_frame, text="Ver todos")
        self.list_bt.pack(fill="x", pady=5)
        self.find_bt = Button(self.left_frame, text="Buscar")
        self.find_bt.pack(fill="x", pady=5)
        self.create_bt = Button(self.left_frame, text="Inserir")
        self.create_bt.pack(fill="x", pady=5)
        self.update_bt = Button(self.left_frame, text="Atualizar Selecionado")
        self.update_bt.pack(fill="x", pady=5)
        self.delete_bt = Button(self.left_frame, text="Deletar Selecionados")
        self.delete_bt.pack(fill="x", pady=5)
        self.close_bt = Button(self.left_frame, text="Fechar")
        self.close_bt.pack(fill="x", pady=5)
        
        # Frame direito para a exibição dos dados
        self.right_frame = Frame(self.main_frame)
        self.right_frame.pack(side="right", fill="both", expand=True)
        
        # Frame para embalar o Treeview e a Scrollbar
        self.treeview_frame = Frame(self.right_frame)
        self.treeview_frame.pack(fill="both", expand=True)
        
        # Treeview para mostrar os dados dos médicos
        self.columns = ("ID", "Nome", "Especialidade", "CRM")
        self.treeview = Treeview(self.treeview_frame, columns=self.columns, show="headings")
        self.treeview.pack(side="left", fill="both", expand=True)

        # Configura as colunas do Treeview
        for col in self.columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=150, anchor="center")
        
        # Barra de rolagem para o Treeview
        self.scrollbar = Scrollbar(self.treeview_frame, orient="vertical", command=self.treeview.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
