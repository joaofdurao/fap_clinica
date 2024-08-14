import tkinter as tk

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
        print("Abrir Paciente")

    def abrir_medico(self):
        print("Abrir Medico")

    def abrir_consulta(self):
        print("Abrir Consulta")


class TelaPaciente(tk.Frame):
    def __init__(self, master, manager):
        super().__init__(master)
        self.manager = manager
        self.canvas = tk.Canvas(self, width=1080, height=720)
        self.canvas.pack(fill="both", expand=True)

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