from views.main_view import MainView
from controllers.paciente_controller import PacienteController

class MainController:
    def __init__(self, root):
        self.root = root
        self.main_view = MainView(self.root)
        self.setup_main_view()

    def setup_main_view(self):
        self.main_view.btn_paciente.config(command=self.open_paciente_management)
        self.main_view.btn_medico.config(command=self.open_medico_management)
        self.main_view.btn_consulta.config(command=self.open_consulta_management)


    def open_paciente_management(self):
        PacienteController(self.root)

    def open_medico_management(self):
        PacienteController(self.root)

    def open_consulta_management(self):
        PacienteController(self.root)