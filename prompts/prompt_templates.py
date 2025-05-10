# Definición de plantillas de prompts para distintas situaciones

PROMPT_TEMPLATES = {
    "saludo": "Hola, soy un modelo de IA. ¿Cómo puedo ayudarte?",
    "pregunta_abierta": "¿Qué te gustaría saber sobre {tema}?",
    "tarea_específica": "Por favor, proporciona detalles específicos sobre la tarea que necesitas realizar.",
    "análisis_datos": "Analiza los siguientes datos y proporciona un resumen claro:\n{datos}",
    "creatividad": "Genera una historia corta basada en el siguiente escenario: {escenario}",
    "traducción": "Traduce este texto al idioma {idioma}: {texto}",
    "asistencia_programación": "Ayúdame a solucionar este problema de código en {lenguaje}:\n{codigo}"
}

def get_prompt_template(tipo, **kwargs):
    """
    Devuelve una plantilla de prompt con los valores formateados.

    :param tipo: Clave de la plantilla a usar.
    :param kwargs: Valores a reemplazar en la plantilla.
    :return: Prompt estructurado.
    """
    template = PROMPT_TEMPLATES.get(tipo, "Tipo de prompt no encontrado.")
    return template.format(**kwargs)

# Ejemplo de uso
if __name__ == "__main__":
    ejemplo_prompt = get_prompt_template("pregunta_abierta", tema="inteligencia artificial")
    print(ejemplo_prompt)