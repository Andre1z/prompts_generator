import os

# Configuración de la aplicación
APP_NAME = "Generador de Prompts IA"
VERSION = "1.0.0"
AUTHOR = "Andrei"

# Directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_DIR = os.path.join(BASE_DIR, "prompts")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Parámetros predeterminados
DEFAULT_PROMPT_TEMPLATE = "Hola, soy un modelo de IA. ¿Cómo puedo ayudarte?"
MAX_PROMPT_LENGTH = 500

# Opciones de interfaz
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
THEME_COLOR = "#3498db"
FONT_FAMILY = "Arial"
FONT_SIZE = 12