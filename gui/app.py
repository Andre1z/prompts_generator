import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, THEME_COLOR
from utils.md_generator import generate_project_report, save_report_to_file

class PromptApp:
    def __init__(self, root):
        """Inicializa la ventana principal."""
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=THEME_COLOR)

        # Sección principal con paneles
        self.paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True)

        # Panel izquierdo: formulario
        self.frame_left = ttk.Frame(self.paned, padding=10)
        self.paned.add(self.frame_left, weight=1)
        self._create_form_section()

        # Panel derecho: salida del prompt
        self.frame_right = ttk.Frame(self.paned, padding=10)
        self.paned.add(self.frame_right, weight=1)
        self._create_output_section()

        # Variable para almacenar la carpeta seleccionada
        self.selected_folder = None

    def _create_form_section(self):
        """Crea la sección del formulario en la interfaz."""
        ttk.Label(self.frame_left, text="Configuración del Prompt", font=("Arial", 12, "bold")).pack(anchor="w")

        self.txt_contexto = self._create_text_input("Contexto", "Explica la situación o problema.")
        self.txt_objetivo = self._create_text_input("Objetivo", "Define claramente lo que quieres lograr.")
        self.txt_restricciones = self._create_text_input("Restricciones", "Especifica tecnologías y limitaciones.")
        self.txt_formato = self._create_text_input("Formato de salida", "Define si necesitas código, explicación, JSON, etc.")

        ttk.Button(self.frame_left, text="Seleccionar carpeta del proyecto", command=self.select_project_folder).pack(fill=tk.X, pady=5)
        ttk.Button(self.frame_left, text="Generar Prompt", bootstyle=SUCCESS, command=self.generate_prompt).pack(fill=tk.X, pady=10)

    def _create_text_input(self, label_text, desc_text):
        """Crea un campo de entrada de texto."""
        frame = ttk.Frame(self.frame_left)
        frame.pack(fill=tk.X, pady=5)
        ttk.Label(frame, text=label_text, font=("Arial", 10, "bold")).pack(anchor="w")
        ttk.Label(frame, text=desc_text, font=("Arial", 8)).pack(anchor="w")
        txt = tk.Text(frame, height=3)
        txt.pack(fill=tk.X, pady=2)
        return txt

    def _create_output_section(self):
        """Crea la sección de salida del prompt."""
        ttk.Label(self.frame_right, text="Salida del Prompt", font=("Arial", 12, "bold")).pack(anchor="w")
        self.txt_output = tk.Text(self.frame_right, wrap="word", state=tk.NORMAL)
        self.txt_output.pack(fill=tk.BOTH, expand=True)
        
        frame_buttons = ttk.Frame(self.frame_right)
        frame_buttons.pack(fill=tk.X, pady=5)
        ttk.Button(frame_buttons, text="Copiar", command=self.copy_report).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        ttk.Button(frame_buttons, text="Guardar", command=self.save_report).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

    def select_project_folder(self):
        """Permite seleccionar una carpeta y muestra su estructura y código en pantalla sin guardarlo automáticamente."""
        folder_selected = filedialog.askdirectory(title="Selecciona la carpeta del proyecto")
        if folder_selected:
            self.selected_folder = folder_selected
            project_report = generate_project_report(folder_selected)
            
            self.txt_output.config(state=tk.NORMAL)
            self.txt_output.delete("1.0", tk.END)
            self.txt_output.insert(tk.END, project_report)
            self.txt_output.config(state=tk.DISABLED)

            messagebox.showinfo("Éxito", "Estructura y código del proyecto generados correctamente.")
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ninguna carpeta.")

    def generate_prompt(self):
        """Genera un prompt basado en los datos ingresados y la estructura del proyecto."""
        prompt = "Crea / modifica un software informático en base a los parámetros que a continuación te voy a indicar:\n\n"
        prompt += f"Contexto: {self.txt_contexto.get('1.0', tk.END).strip()}\n"
        prompt += f"Objetivo: {self.txt_objetivo.get('1.0', tk.END).strip()}\n"
        prompt += f"Restricciones: {self.txt_restricciones.get('1.0', tk.END).strip()}\n"
        prompt += f"Formato de salida: {self.txt_formato.get('1.0', tk.END).strip()}\n"

        if self.selected_folder:
            prompt += "\n===== Project Structure & Code =====\n"
            prompt += generate_project_report(self.selected_folder)

        self.txt_output.config(state=tk.NORMAL)
        self.txt_output.delete("1.0", tk.END)
        self.txt_output.insert(tk.END, prompt)
        self.txt_output.config(state=tk.DISABLED)

    def copy_report(self):
        """Copia el prompt generado al portapapeles."""
        report_text = self.txt_output.get("1.0", tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(report_text)
        messagebox.showinfo("Portapapeles", "Reporte copiado al portapapeles.")

    def save_report(self):
        """Permite al usuario elegir dónde guardar el reporte."""
        report_text = self.txt_output.get("1.0", tk.END)
        save_report_to_file(report_text)

if __name__ == "__main__":
    root = ttk.Window(themename="flatly")
    app = PromptApp(root)
    root.mainloop()