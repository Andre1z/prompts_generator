import os
import tkinter as tk
from tkinter import filedialog, messagebox

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

def generate_project_report(directory):
    """Genera un reporte en Markdown sin guardarlo automáticamente."""
    if not directory:
        return "No se ha seleccionado una carpeta."

    markdown_report = f"# Estructura del Proyecto\n\n```\n{get_project_structure(directory)}\n```"
    return markdown_report

def save_report_to_file(report_text):
    """Permite al usuario elegir dónde guardar el archivo de reporte."""
    file_path = filedialog.asksaveasfilename(
        title="Guardar reporte",
        defaultextension=".md",
        filetypes=[("Markdown Files", "*.md"), ("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(report_text)
            messagebox.showinfo("Éxito", f"Reporte guardado en:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el reporte: {e}")