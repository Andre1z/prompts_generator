import os
import tkinter as tk
from tkinter import filedialog

def get_project_structure(directory, indent=0):
    """Genera la estructura de la carpeta en formato Markdown."""
    markdown_content = ""
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        prefix = " " * indent + ("- " if os.path.isdir(item_path) else "- 📄 ")
        markdown_content += f"{prefix}{item}\n"
        if os.path.isdir(item_path):
            markdown_content += get_project_structure(item_path, indent + 4)  # Aumentar indentación
    return markdown_content

def select_folder_and_generate_prompt():
    """Permite al usuario seleccionar una carpeta y genera un archivo Markdown con su estructura."""
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    folder_selected = filedialog.askdirectory(title="Selecciona la carpeta del proyecto")

    if folder_selected:
        markdown_prompt = f"# Estructura del Proyecto\n\n```\n{get_project_structure(folder_selected)}\n```"
        save_path = os.path.join(folder_selected, "project_structure.md")
        
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(markdown_prompt)
        
        print(f"Prompt generado y guardado en: {save_path}")
    else:
        print("No se seleccionó ninguna carpeta.")

# Ejemplo de uso
if __name__ == "__main__":
    select_folder_and_generate_prompt()