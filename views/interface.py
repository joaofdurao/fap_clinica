import tkinter as tk
from tkinter import messagebox

class Janela(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1080x720")
        self.title("FAP - Clínica")
        self.tela_atual = None
        self.jogador = None
        self.perguntas_list = []
        
        self.mudar_tela(TelaMenuInicial(self, self))

    def mudar_tela(self, nova_tela):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = nova_tela
        self.tela_atual.pack()


class TelaMenuInicial(tk.Frame):
    def __init__(self, master, manager):
        super().__init__(master)
        self.manager = manager
        self.pacientes = []  # Lista para armazenar pacientes
        self.proximo_id = 1  # Inicializa o ID do próximo paciente
        
        self.canvas = tk.Canvas(self, width=1080, height=720)
        self.canvas.pack(fill="both", expand=True)
        
        self.title_label = tk.Label(self.canvas, text="FAP - Clínica", font=("Arial", 72))
        self.title_label.place(relx=0.5, rely=0.3, anchor="center")
        
        btn_width = 20
        btn_height = 2
        btn_font = ("Arial", 14)
        button_spacing = 0.12  

        self.btn_paciente = tk.Button(self.canvas, text="Paciente", width=btn_width, height=btn_height, font=btn_font, command=self.abrir_paciente)
        self.btn_paciente.place(relx=0.5, rely=0.5, anchor="center")
        
        self.btn_medico = tk.Button(self.canvas, text="Medico", width=btn_width, height=btn_height, font=btn_font, command=self.abrir_medico)
        self.btn_medico.place(relx=0.5, rely=0.5 + button_spacing, anchor="center")
        
        self.btn_consulta = tk.Button(self.canvas, text="Consulta", width=btn_width, height=btn_height, font=btn_font, command=self.abrir_consulta)
        self.btn_consulta.place(relx=0.5, rely=0.5 + 2 * button_spacing, anchor="center")

    def abrir_paciente(self):
        self.janela_cadastro_paciente = tk.Toplevel(self)
        self.janela_cadastro_paciente.title("Cadastro de Paciente")
        self.janela_cadastro_paciente.geometry("400x350")

        tk.Label(self.janela_cadastro_paciente, text="CPF:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_cpf = tk.Entry(self.janela_cadastro_paciente)
        self.entry_cpf.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.janela_cadastro_paciente, text="Nome:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_nome = tk.Entry(self.janela_cadastro_paciente)
        self.entry_nome.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.janela_cadastro_paciente, text="Data de Nascimento:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_data_nasc = tk.Entry(self.janela_cadastro_paciente)
        self.entry_data_nasc.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.janela_cadastro_paciente, text="Telefone:").grid(row=3, column=0, padx=10, pady=5)
        self.entry_telefone = tk.Entry(self.janela_cadastro_paciente)
        self.entry_telefone.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.janela_cadastro_paciente, text="Salvar", command=self.salvar_dados).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.janela_cadastro_paciente, text="Listar Pacientes", command=self.listar_pacientes).grid(row=5, column=0, columnspan=2, pady=10)

    def salvar_dados(self):
        cpf = self.entry_cpf.get()
        nome = self.entry_nome.get()
        data_nasc = self.entry_data_nasc.get()
        telefone = self.entry_telefone.get()

        if not cpf or not nome or not data_nasc or not telefone:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos.")
            return
        
        paciente = {
            "id": self.proximo_id,
            "cpf": cpf,
            "nome": nome,
            "data_nasc": data_nasc,
            "telefone": telefone
        }
        self.pacientes.append(paciente)
        self.proximo_id += 1  # Incrementa o ID para o próximo paciente
        
        messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
        self.janela_cadastro_paciente.destroy()

    def listar_pacientes(self):
        janela_lista = tk.Toplevel(self)
        janela_lista.title("Lista de Pacientes")
        janela_lista.geometry("600x400")
        
        listbox = tk.Listbox(janela_lista, width=80, height=20)
        listbox.pack(padx=10, pady=10)

        for paciente in self.pacientes:
            listbox.insert(tk.END, f"ID: {paciente['id']}, CPF: {paciente['cpf']}, Nome: {paciente['nome']}, Data Nasc: {paciente['data_nasc']}, Telefone: {paciente['telefone']}")

    def abrir_medico(self):
        print("Abrir Medico")

    def abrir_consulta(self):
        print("Abrir Consulta")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Menu Inicial")
    tela = TelaMenuInicial(root, None)
    tela.pack(fill="both", expand=True)
    root.mainloop()

    # -> Bt cad Paciente
    # -> bt pesquisa paciente
    # -> bt atualizar paciente
    # -> remover paciente



class TelaFim(tk.Frame):
    def __init__(self, master, manager):
        super().__init__(master, bg="purple", width=400, height=800)
        self.manager = manager

        frame_central = tk.Frame(self, bg="purple")
        frame_central.place(relx=0.5, rely=0.5, anchor="center") 

        mensagem = "Parabéns!\nVocê ganhou 1 milhão de reais!"
        label_fim = tk.Label(frame_central, text=mensagem, font=("Arial", 18), fg="white", bg="purple")
        label_fim.pack(pady=20)

        botao_reiniciar = tk.Button(frame_central, text="Reiniciar", command=self.reiniciar, width=20, height=2, bg="yellow", fg="black", font=("Arial", 12))  
        botao_reiniciar.pack(pady=10)

    def reiniciar(self):
        self.manager.contador = 0
        self.manager.perguntas_list = []
        self.destroy()
        self.manager.mudar_tela(TelaMenuInicial(self.master, self.manager))