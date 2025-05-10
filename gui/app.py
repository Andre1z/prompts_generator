import tkinter as tk
from tkinter import messagebox
from config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, THEME_COLOR
from prompts.prompt_templates import PROMPT_TEMPLATES, get_prompt_template
from prompts.custom_prompts import get_custom_prompt, add_custom_prompt

class PromptApp:
    def __init__(self, root):
        """Inicializa la ventana principal."""
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=THEME_COLOR)

        # Etiqueta
        self.label = tk.Label(root, text="Selecciona un tipo de prompt:", font=("Arial", 14), bg=THEME_COLOR, fg="white")
        self.label.pack(pady=10)

        # Selector de prompt corregido
        self.prompt_type = tk.StringVar(root)
        self.prompt_type.set(next(iter(PROMPT_TEMPLATES)))  # Establecer valor por defecto
        self.prompt_menu = tk.OptionMenu(root, self.prompt_type, *PROMPT_TEMPLATES.keys())
        self.prompt_menu.pack(pady=10)

        # Botón para generar prompt
        self.generate_button = tk.Button(root, text="Generar Prompt", command=self.generate_prompt)
        self.generate_button.pack(pady=10)

        # Área de texto
        self.prompt_output = tk.Text(root, height=5, width=50)
        self.prompt_output.pack(pady=10)

        # Botón para guardar prompt personalizado
        self.save_button = tk.Button(root, text="Guardar Prompt", command=self.save_prompt)
        self.save_button.pack(pady=10)

    def generate_prompt(self):
        """Genera un prompt basado en la selección del usuario."""
        prompt_type = self.prompt_type.get()
        if prompt_type in PROMPT_TEMPLATES:
            prompt_text = get_prompt_template(prompt_type)
            self.prompt_output.delete("1.0", tk.END)
            self.prompt_output.insert(tk.END, prompt_text)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un tipo de prompt válido.")

    def save_prompt(self):
        """Guarda un prompt personalizado."""
        prompt_text = self.prompt_output.get("1.0", tk.END).strip()
        if prompt_text:
            add_custom_prompt("personalizado", prompt_text)
            messagebox.showinfo("Éxito", "Prompt guardado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "No hay texto para guardar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PromptApp(root)
    root.mainloop()