import json
import os
from config import PROMPT_DIR

CUSTOM_PROMPTS_FILE = os.path.join(PROMPT_DIR, "custom_prompts.json")

def load_custom_prompts():
    """Carga los prompts personalizados desde un archivo JSON."""
    if os.path.exists(CUSTOM_PROMPTS_FILE):
        with open(CUSTOM_PROMPTS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def save_custom_prompts(prompts):
    """Guarda los prompts personalizados en un archivo JSON."""
    os.makedirs(PROMPT_DIR, exist_ok=True)
    with open(CUSTOM_PROMPTS_FILE, "w", encoding="utf-8") as file:
        json.dump(prompts, file, indent=4, ensure_ascii=False)

def add_custom_prompt(name, content):
    """Añade un nuevo prompt personalizado."""
    prompts = load_custom_prompts()
    prompts[name] = content
    save_custom_prompts(prompts)

def get_custom_prompt(name):
    """Obtiene un prompt personalizado por su nombre."""
    prompts = load_custom_prompts()
    return prompts.get(name, "Prompt no encontrado.")

# Ejemplo de uso
if __name__ == "__main__":
    add_custom_prompt("motivación", "¡No te rindas! Cada esfuerzo te acerca a la meta.")
    print(get_custom_prompt("motivación"))