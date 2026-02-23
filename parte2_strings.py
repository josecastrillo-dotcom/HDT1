# ============================================================
#  HDT1 — Parte 2: Strings
#  DataFest 2026 — Sistema de Operaciones
# ============================================================

# ============================================================
#  Ejercicio 2.1 — Generador de Credenciales  (8 pts)
# ============================================================
# Formato: FD26-[ZONA3]-[INICIALES][NUMERO]
#
#   ZONA3     → primeras 3 letras de la zona en MAYÚSCULAS
#   INICIALES → primera letra del nombre + primera del apellido, MAYÚSCULAS
#   NUMERO    → registro con 4 dígitos y ceros a la izquierda
#
# Pistas:
#   - nombre.split()     → lista de palabras; el apellido es el ÚLTIMO elemento
#   - str(n).zfill(4)    → "47" → "0047"
#   - "campo"[:3].upper() → "CAM"
#
# Casos de prueba (NO modificar):
registros = [
    ("Carlos Mendoza",        "vip",         47),
    ("Ana García",            "campo",         5),
    ("José Luis Rodríguez",   "gradería",   1823),
    ("María López",           "preferencia", 312),
]

# --- Tu código aquí ---

for nombre, zona, numero in registros:
    # Extrae las 3 primeras letras de zona en mayúsculas
    zona3_letras = zona[:3].upper()

    # Extrae la inicial del nombre (primera palabra)
    partes = nombre.split()
    inicial_nombre = partes[0][0].upper()

    # Extrae la inicial del apellido (última palabra)
    inicial_apellido = partes[-1][0].upper()

    # Formatea el número con zfill(4)
    num4 = str(numero).zfill(4)

    # Construye y muestra la credencial
    credencial = f"FD26-{zona3_letras}-{inicial_nombre}{inicial_apellido}{num4}"
    print(credencial)
    

# Salida esperada:
# FD26-VIP-CM0047
# FD26-CAM-AG0005
# FD26-GRA-JR1823
# FD26-PRE-ML0312


# ============================================================
#  Ejercicio 2.2 — Limpieza de Datos de Asistentes  (6 pts)
# ============================================================
# Formato crudo: "  nombre  ,  email  ,  edad  "
#
# Procesamiento:
#   - Separar por coma y limpiar espacios con .strip()
#   - Nombre: .title() para capitalizar cada palabra
#   - Email:  .lower(); válido si contiene "@" y hay un "." DESPUÉS del "@"
#   - Edad:   int(); advertir si no está en [5, 100]

# --- Datos de prueba (NO modificar) ---
registros_crudos = [
    "  ana GARCIA    ,   ana.garcia@gmail.com  ,   22  ",
    "  JOSE LUIS perez  ,  jl_perez@outlook  ,  17  ",
    "  María Fernanda SOLIS  ,  mfernanda@ufm.edu  ,  150  ",
]

# --- Tu código aquí ---

for i, registro in enumerate(registros_crudos, start=1):
    print(f"--- Registro {i} ---")

    # Separa el registro en sus 3 campos usando split(",")
    campos = registro.split(",")

    # Aplica .strip() a cada campo
    nombre_leido = campos[0].strip()
    email_leido = campos[1].strip()
    edad_leido = campos[2].strip()

    # Procesa y valida nombre, email y edad
    nombre = nombre_leido.title()
    email = email_leido.lower()

    if "@" in email:
        pos_arroba = email.find("@")
        valido_email = ("." in email[pos_arroba + 1 :])
    else:
        valido_email = False       

    edad = int(edad_leido)
    en_rango = 5 <= edad <= 100

    # Imprime el resultado con el formato esperado
    print(f"Nombre : {nombre}")
    print(f"Email  : {email} | Válido: {'Sí' if valido_email else 'No'}")

    if en_rango:
        print(f"Edad   : {edad} | En rango: Sí")
    else:
        print(f"Edad   : {edad} | En rango: No — fuera del rango [5, 100]")

    print()


    

# Salida esperada:
# --- Registro 1 ---
# Nombre : Ana Garcia
# Email  : ana.garcia@gmail.com | Válido: Sí
# Edad   : 22 | En rango: Sí
#
# --- Registro 2 ---
# Nombre : Jose Luis Perez
# Email  : jl_perez@outlook | Válido: No
# Edad   : 17 | En rango: Sí
#
# --- Registro 3 ---
# Nombre : Maria Fernanda Solis
# Email  : mfernanda@ufm.edu | Válido: Sí
# Edad   : 150 | En rango: No — fuera del rango [5, 100]


# ============================================================
#  Ejercicio 2.3 — Análisis de Reseñas  (6 pts)
# ============================================================
# Para cada reseña calcula:
#   1. Total de palabras (.split())
#   2. Total de vocales (a e i o u á é í ó ú — mayúsculas y minúsculas)
#   3. Palabra más larga (primer empate gana)
#   4. Sentimiento:
#      - positiva   → solo tiene palabras positivas
#      - negativa   → solo tiene palabras negativas
#      - mixta      → tiene de ambas
#      - neutral    → no tiene ninguna
#
# Positivas: "increíble", "excelente", "genial", "espectacular",
#            "maravilloso", "fantástico"
# Negativas: "malo", "pésimo", "terrible", "aburrido",
#            "decepcionante", "horrible"

# --- Datos de prueba (NO modificar) ---
resenas = [
    "El festival fue espectacular los artistas son increíble el sonido la energía todo genial",
    "Lamentablemente el sonido fue terrible aunque los artistas estuvieron genial pero el acceso horrible",
]

# --- Tu código aquí ---

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
palabras_positivas = ["increíble", "excelente", "genial", "espectacular", "maravilloso", "fantástico"]
palabras_negativas = ["malo", "pésimo", "terrible", "aburrido", "decepcionante", "horrible"]

for i, resena in enumerate(resenas, start=1):
    print(f"--- Reseña {i} ---")

    palabras = resena.split()

    # TODO: Cuenta las palabras
    total_palabras = len(resena.split())

    # TODO: Cuenta las vocales (recorre cada carácter)
    total_vocales = 0
    for palabra in palabras:
        vocales_vistas = set()
        for caracter in palabra:
            if caracter in vocales and caracter not in vocales_vistas:
                total_vocales += 1  
                vocales_vistas.add(caracter)          

    # TODO: Encuentra la palabra más larga
    
    palabra_larga = palabras[0]
    for palabra in palabras:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra

    # TODO: Determina el sentimiento
    tiene_positivo = any(p in palabras_positivas for p in palabras)
    tiene_negativo = any(p in palabras_negativas for p in palabras)

    if tiene_positivo and not tiene_negativo:
        sentimiento = "positiva"
    elif tiene_negativo and not tiene_positivo:
        sentimiento = "negativa"
    elif tiene_positivo and tiene_negativo:
        sentimiento = "mixta"
    else:
        sentimiento = "neutral"

    # TODO: Imprime los resultados con el formato esperado
    print(f"Palabras      : {total_palabras}")
    print(f"Vocales       : {total_vocales}")
    print(f'Palabra larga : "{palabra_larga.lower()}"')
    print(f"Sentimiento   : {sentimiento}")
    print()
    

# Salida esperada:
# --- Reseña 1 ---
# Palabras      : 14
# Vocales       : 27
# Palabra larga : "espectacular"
# Sentimiento   : positiva
#
# --- Reseña 2 ---
# Palabras      : 12 
# Vocales       : 22
# Palabra larga : "decepcionante"
# Sentimiento   : mixta

