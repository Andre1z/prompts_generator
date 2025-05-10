import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class CustomButton(ttk.Button):
    """Botón personalizado con estilo mejorado."""
    def __init__(self, parent, text, command=None, **kwargs):
        super().__init__(
            parent, 
            text=text, 
            command=command, 
            bootstyle=SUCCESS, 
            padding=(10, 5), 
            **kwargs
        )

class CustomLabel(ttk.Label):
    """Etiqueta personalizada con estilos coherentes."""
    def __init__(self, parent, text, **kwargs):
        super().__init__(
            parent, 
            text=text, 
            font=("Arial", 12), 
            padding=(5, 2), 
            **kwargs
        )

class CustomTextBox(tk.Text):
    """Área de texto personalizada con tamaño ajustado."""
    def __init__(self, parent, height=5, **kwargs):
        super().__init__(
            parent, 
            font=("Arial", 11), 
            wrap="word", 
            height=height, 
            width=50, 
            padx=5, 
            pady=5,
            **kwargs
        )

# Ejemplo de uso
if __name__ == "__main__":
    root = ttk.Window(themename="flatly")
    root.title("Widgets de Prueba")
    
    label = CustomLabel(root, "¡Bienvenido a la aplicación!")
    label.pack(pady=10)

    text_box = CustomTextBox(root)
    text_box.pack(pady=10)

    button = CustomButton(root, "Aceptar", command=lambda: print("Botón presionado"))
    button.pack(pady=10)

    root.mainloop()