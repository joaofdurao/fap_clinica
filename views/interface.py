import tkinter as tk

class Janela(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("480x800")
        self.title("FAP - Clinica")
        self.tela_atual = None
        self.jogador = None
        self.perguntas_list = []
        
        self.mudar_tela(TelaInicio(self, self))

    def mudar_tela(self, nova_tela):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = nova_tela
        self.tela_atual.pack()

class TelaInicio(tk.Frame):
    def __init__(self, master, manager):
        super().__init__(master)
        self.manager = manager
        self.canvas = tk.Canvas(self, width=480, height=800, bg="purple")
        self.canvas.pack(fill="both", expand=True)

        botao_jogar = tk.Button(self, text="Jogar", command=self.jogar, width=30, height=2, bg="yellow", fg="black", font=("Arial", 14))
        self.canvas.create_window(240, 600, anchor="center", window=botao_jogar)


    def jogar(self):
        self.manager.mudar_tela(TelaFim(self.master, self.manager)) 

class TelaFim(tk.Frame):
    def __init__(self, master, manager):
        super().__init__(master, bg="purple", width=400, height=800)
        self.manager = manager

        frame_central = tk.Frame(self, bg="purple")
        frame_central.place(relx=0.5, rely=0.5, anchor="center") 

        mensagem = "Parabéns!\nVocê ganhou 1 milhão de reais!"
        label_fim = tk.Label(frame_central, text=mensagem, font=("Arial", 18), fg="white", bg="purple")
        label_fim.pack(pady=20)

        botao_reiniciar = tk.Button(frame_central, text="Reiniciar", command=self.reiniciar, width=20, height=2, bg="yellow", fg="black", font=("Arial", 12))  # Define a cor de fundo como amarelo, o texto como preto e a fonte como Arial tamanho 12
        botao_reiniciar.pack(pady=10)

    def reiniciar(self):
        self.manager.contador = 0
        self.manager.perguntas_list = []
        self.destroy()
        self.manager.mudar_tela(TelaInicio(self.master, self.manager))