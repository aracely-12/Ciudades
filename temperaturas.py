def calcular_temperatura_promedio(temperaturas, nombre_ciudad=None, semana=None):
    """
    Calcula la temperatura promedio de una ciudad durante un período de tiempo.

    Args:
        temperaturas (list): Lista de listas con datos de temperatura por ciudad y semana.
        nombre_ciudad (str, opcional): Nombre de la ciudad para calcular el promedio. Si es None, calcula el promedio general.
        semana (int, opcional): Número de semana para calcular el promedio. Si es None, calcula el promedio de todas las semanas.

    Returns:
        float: Temperatura promedio calculada.
    """

    nombres_ciudades = ["Ambato", "Quito", "Riobamba"]
    promedio_total = 0
    total_temperaturas = 0

    for i, ciudad_data in enumerate(temperaturas):
        nombre_ciudad_actual = nombres_ciudades[i]

        if nombre_ciudad is None or nombre_ciudad == nombre_ciudad_actual:
            for j, semana_data in enumerate(ciudad_data):
                if semana is None or semana == j + 1:
                    for dia_data in semana_data:
                        promedio_total += dia_data["temp"]
                        total_temperaturas += 1

    if total_temperaturas == 0:
        return 0  # Retorna 0 si no hay datos para calcular el promedio
    else:
        return promedio_total / total_temperaturas

# Datos de temperatura proporcionados
temperaturas = [
    [  # Ambato
        [  # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 25},
            {'day': 'Jueves', 'temp': 24},
            {'day': 'Viernes', 'temp': 28},
            {'day': 'Sábado', 'temp': 30},
            {'day': 'Domingo', 'temp': 32}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 33}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [  # Quito
        [  # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 25}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 24}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 25}
        ]
    ],
    [  # Riobamba
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 25}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 24}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 24},
        ],
        ]
        ]
