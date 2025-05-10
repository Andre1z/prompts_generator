import re

def clean_text(text):
    """Limpia el texto eliminando espacios extra y caracteres innecesarios."""
    return re.sub(r"\s+", " ", text.strip())

def format_prompt(prompt, max_length=500):
    """Formatea un prompt asegurándose de que no exceda el límite de caracteres."""
    cleaned_prompt = clean_text(prompt)
    return cleaned_prompt[:max_length]

def validate_prompt(prompt):
    """Valida el prompt para detectar contenido vacío o caracteres inválidos."""
    if not prompt or not isinstance(prompt, str):
        return False
    return len(clean_text(prompt)) > 0

# Ejemplo de uso
if __name__ == "__main__":
    test_prompt = "   Hola, ¿puedes ayudarme con    esto?   "
    formatted = format_prompt(test_prompt)
    valid = validate_prompt(formatted)
    print(f"Prompt formateado: {formatted}")
    print(f"Es válido: {valid}")