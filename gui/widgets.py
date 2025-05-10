import tkinter as tk

class CustomButton(tk.Button):
    """Botón personalizado con estilo."""
    def __init__(self, parent, text, command=None, **kwargs):
        super().__init__(
            parent, 
            text=text, 
            command=command, 
            font=("Arial", 12, "bold"), 
            bg="#2ecc71", 
            fg="white",
            padx=10, 
            pady=5, 
            relief="raised",
            **kwargs
        )

class CustomLabel(tk.Label):
    """Etiqueta personalizada con estilo."""
    def __init__(self, parent, text, **kwargs):
        super().__init__(
            parent, 
            text=text, 
            font=("Arial", 14), 
            bg="#3498db", 
            fg="white", 
            padx=10, 
            pady=5,
            **kwargs
        )

class CustomTextBox(tk.Text):
    """Área de texto personalizada."""
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent, 
            font=("Arial", 12), 
            wrap="word", 
            height=5, 
            width=50, 
            bg="white", 
            fg="black",
            padx=5, 
            pady=5,
            **kwargs
        )

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Widgets de Prueba")
    
    label = CustomLabel(root, "¡Hola, bienvenido!")
    label.pack(pady=10)

    text_box = CustomTextBox(root)
    text_box.pack(pady=10)

    button = CustomButton(root, "Aceptar", command=lambda: print("Botón presionado"))
    button.pack(pady=10)

    root.mainloop()