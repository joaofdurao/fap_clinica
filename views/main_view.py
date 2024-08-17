from tkinter import Frame, Label, Button

class MainView:
    def __init__(self, root):
        self.root = root
        
        main_frame = Frame(root)
        main_frame.pack(fill="both", expand=True)
        
        self.title_label = Label(main_frame, text="FAP - Clínica", font=("Arial", 72))
        self.title_label.place(relx=0.5, rely=0.3, anchor="center")
        
        btn_width = 20
        btn_height = 2
        btn_font = ("Arial", 14)
        button_spacing = 0.12  

        self.btn_paciente = Button(main_frame, text="Paciente", width=btn_width, height=btn_height, font=btn_font)
        self.btn_paciente.place(relx=0.5, rely=0.5, anchor="center")
        
        self.btn_medico = Button(main_frame, text="Medico", width=btn_width, height=btn_height, font=btn_font)
        self.btn_medico.place(relx=0.5, rely=0.5 + button_spacing, anchor="center")
        
        self.btn_consulta = Button(main_frame, text="Consulta", width=btn_width, height=btn_height, font=btn_font)
        self.btn_consulta.place(relx=0.5, rely=0.5 + 2 * button_spacing, anchor="center")