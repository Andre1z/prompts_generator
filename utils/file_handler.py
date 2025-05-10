import os
import json

def load_json(file_path):
    """Carga un archivo JSON y devuelve su contenido."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def save_json(file_path, data):
    """Guarda datos en un archivo JSON."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_text(file_path):
    """Carga un archivo de texto y devuelve su contenido."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return ""

def save_text(file_path, content):
    """Guarda contenido en un archivo de texto."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

# Ejemplo de uso
if __name__ == "__main__":
    sample_data = {"prompt": "Hola, ¿cómo puedo ayudarte?"}
    json_file = "example.json"
    save_json(json_file, sample_data)
    loaded_data = load_json(json_file)
    print(f"Contenido JSON cargado: {loaded_data}")

    text_file = "example.txt"
    save_text(text_file, "Este es un ejemplo de texto almacenado.")
    loaded_text = load_text(text_file)
    print(f"Contenido del archivo de texto: {loaded_text}")