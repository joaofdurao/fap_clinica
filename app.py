from controllers.main_controller import MainController
from tkinter import Tk

def main():
    root = Tk()
    root.geometry("1080x720")
    root.title("FAP - Clínica")

    app = MainController(root)

    root.mainloop()

if __name__ == "__main__":
    main()