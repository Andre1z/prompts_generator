import tkinter as tk
from gui.app import PromptApp

def main():
    """Inicializa la aplicación GUI."""
    root = tk.Tk()
    app = PromptApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()