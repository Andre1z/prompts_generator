import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Lista de extensiones de archivos permitidos
ALLOWED_EXTENSIONS = ('.py', '.js', '.html', '.css', '.php', '.java', '.sql')

# Mapeo de extensiones a etiquetas de lenguajes para bloques de código Markdown
LANG_MAPPING = {
    '.py': 'python',
    '.js': 'javascript',
    '.html': 'html',
    '.css': 'css',
    '.php': 'php',
    '.java': 'java',
    '.sql': 'sql'
}

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

def get_code_content(directory, depth=1):
    """Genera el contenido de archivos permitidos en formato Markdown."""
    report_lines = []
    folder_name = os.path.basename(directory) if os.path.basename(directory) else directory
    header = "#" * depth  # Un "#" por cada nivel de profundidad
    report_lines.append(f"{header} {folder_name}")

    # Procesar archivos permitidos en la carpeta actual
    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) and item.lower().endswith(ALLOWED_EXTENSIONS):
            extension = os.path.splitext(item)[1].lower()
            language = LANG_MAPPING.get(extension, '')
            report_lines.append(f"**{item}**")
            try:
                with open(item_path, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
            except Exception as e:
                content = f"Error al leer el archivo: {e}"
            report_lines.append(f"```{language}")
            report_lines.append(content)
            report_lines.append("```")

    # Procesar subdirectorios
    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            report_lines.append(get_code_content(item_path, depth + 1))

    return "\n".join(report_lines)

def generate_project_report(directory):
    """Genera un reporte en Markdown con estructura y contenido de archivos."""
    if not directory:
        return "No se ha seleccionado una carpeta."

    markdown_report = f"# Estructura del Proyecto\n\n```\n{get_project_structure(directory)}\n```\n\n"
    markdown_report += "===== Code Report (Interleaved) =====\n"
    markdown_report += get_code_content(directory)
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