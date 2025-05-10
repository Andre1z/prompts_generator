import json
import os
from config import PROMPT_DIR

class FileHandler:
    """Clase para gestionar la lectura y escritura de archivos JSON."""

    @staticmethod
    def load_json(file_name):
        """Carga un archivo JSON desde el directorio de prompts."""
        file_path = os.path.join(PROMPT_DIR, file_name)
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}

    @staticmethod
    def save_json(file_name, data):
        """Guarda datos en un archivo JSON dentro del directorio de prompts."""
        os.makedirs(PROMPT_DIR, exist_ok=True)
        file_path = os.path.join(PROMPT_DIR, file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

# Ejemplo de uso
if __name__ == "__main__":
    sample_data = {"prompt": "Hola, ¿cómo puedo ayudarte?"}
    FileHandler.save_json("example.json", sample_data)
    loaded_data = FileHandler.load_json("example.json")
    print(loaded_data)