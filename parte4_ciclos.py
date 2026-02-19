# ============================================================
#  HDT1 — Parte 4: Ciclos
#  DataFest 2026 — Sistema de Operaciones
# ============================================================

# ============================================================
#  Ejercicio 4.1 — Reporte Visual de Afluencia por Hora  (8 pts)
# ============================================================
# ⚠ PROHIBIDO usar max() para encontrar la hora pico.
#
# Muestra solo las horas con afluencia > 0.
# Cada █ representa 30 asistentes (usa //).
# Agrega [PICO] a las horas con afluencia >= 300.
# Al final: total del día y hora pico.
#
# Formato de cada línea:
#   "Hora XX | " + "█" * barras + f" {afluencia} asistentes"
#   Si hay 0 barras, omite los █ pero sí muestra el número.

# --- Datos de prueba (NO modificar) ---
afluencia_por_hora = [
    0,  0,  0,  0,  0,  0,  0,  0,   # 00 – 07
   45, 120, 230, 310, 280,             # 08 – 12
   190, 260, 310, 420, 390,            # 13 – 17
   280, 150,  80,  30,  10,  0        # 18 – 23
]

# --- Tu código aquí ---

print("=== AFLUENCIA POR HORA ===")

# TODO: Usa for con enumerate para recorrer afluencia_por_hora
# TODO: Muestra solo las horas con afluencia > 0
# TODO: Calcula el número de bloques: bloques = afluencia // 30
# TODO: Construye la barra con "█" * bloques
# TODO: Agrega [PICO] si afluencia >= 300
# TODO: Lleva la cuenta del total y encuentra la hora pico (sin max())

total_dia = 0
hora_pico = 0
afluencia_pico = 0

for hora, afluencia in enumerate(afluencia_por_hora):
    pass  # reemplaza este pass con tu lógica

# TODO: Imprime el resumen final
# Salida esperada (fragmento):
# === AFLUENCIA POR HORA ===
# Hora 08 | █ 45 asistentes
# Hora 09 | ████ 120 asistentes
# Hora 10 | ███████ 230 asistentes
# Hora 11 | ██████████ 310 asistentes [PICO]
# Hora 12 | █████████ 280 asistentes
# Hora 13 | ██████ 190 asistentes
# Hora 14 | ████████ 260 asistentes
# Hora 15 | ██████████ 310 asistentes [PICO]
# Hora 16 | ██████████████ 420 asistentes [PICO]
# Hora 17 | █████████████ 390 asistentes [PICO]
# Hora 18 | █████████ 280 asistentes
# Hora 19 | █████ 150 asistentes
# Hora 20 | ██ 80 asistentes
# Hora 21 | █ 30 asistentes
# Hora 22 | 10 asistentes
#
# Total del día : 3,122 asistentes
# Hora pico     : Hora 16 con 420 asistentes


# ============================================================
#  Ejercicio 4.2 — Simulador de Plan de Pagos  (8 pts)
# ============================================================
# Precio de la entrada VIP: Q1,200
# El cliente ingresa su cuota mensual.
#
# Validación (con while):
#   - Mínimo Q100, máximo Q600
#   - Debe ser múltiplo de 50 (cuota % 50 == 0)
#   - Si no cumple, muestra el error específico y pide de nuevo
#
# Simulación del plan:
#   - Mostrar cada cuota con número y saldo restante
#   - La última cuota puede ser menor (no cobrar de más)
#   - Al final: total de cuotas y total pagado

precio_vip = 1200

# --- Tu código aquí ---

# TODO: Usa while para pedir y validar la cuota
print("=== SIMULADOR DE PAGOS — ENTRADA VIP ===")

cuota = 0  # se sobreescribirá con input()
# Pistas para la validación:
#   cuota < 100   → "La cuota mínima es Q100"
#   cuota > 600   → "La cuota máxima es Q600"
#   cuota % 50 != 0 → "La cuota debe ser múltiplo de 50"

# TODO: Simula el plan de pagos con while
# TODO: Lleva la cuenta del número de cuota y el saldo restante

# Salida esperada (si el usuario ingresa 250):
# Cuota ingresada válida: Q250.00
#
# === PLAN DE PAGOS ===
# Cuota #1 : Q250.00 | Saldo restante: Q950.00
# Cuota #2 : Q250.00 | Saldo restante: Q700.00
# Cuota #3 : Q250.00 | Saldo restante: Q450.00
# Cuota #4 : Q250.00 | Saldo restante: Q200.00
# Cuota #5 : Q200.00 | Saldo restante: Q0.00
#
# Total de cuotas : 5
# Total pagado    : Q1200.00


# ============================================================
#  Ejercicio 4.3 — Ranking de Géneros Musicales  (9 pts)
# ============================================================
# ⚠ PROHIBIDO usar diccionarios.
#
# 1. Usa for para contar artistas por género con dos listas paralelas:
#    generos = []  y  conteos = []
#    - Si el género ya está en generos → incrementa su conteo
#    - Si no está → agrégalo con conteo 1
#
# 2. Ordena el ranking de MAYOR a MENOR.
#    Pista para el intercambio:
#       generos[i], generos[j] = generos[j], generos[i]
#       conteos[i], conteos[j] = conteos[j], conteos[i]
#
# 3. Muestra el ranking: cada █ = 1 artista.

# --- Datos de prueba (NO modificar) ---
artistas = [
    ("Resonancia",   "Rock"),        ("Pixel Dreams",  "Electrónica"),
    ("La Guardia",   "Reggaeton"),   ("Voz del Sur",   "Folk"),
    ("Bass Station", "Electrónica"), ("Los Caminos",   "Rock"),
    ("Noche Caribe", "Reggaeton"),   ("Eco Urbano",    "Hip-Hop"),
    ("Marimba 2.0",  "Folk"),        ("Circuito",      "Electrónica"),
    ("Tierra Roja",  "Rock"),        ("Bit a Bit",     "Hip-Hop"),
    ("Cumbia Tech",  "Cumbia"),      ("Guitarra 404",  "Rock"),
]

# --- Tu código aquí ---

generos  = []
conteos  = []

# TODO: Itera sobre artistas y llena generos/conteos
for nombre, genero in artistas:
    pass  # reemplaza con tu lógica

# TODO: Ordena generos y conteos de mayor a menor conteo
#       (ordena las dos listas al mismo tiempo manteniendo correspondencia)

# TODO: Imprime el ranking
print("\n=== RANKING DE GÉNEROS DATAFEST 2026 ===")

# Salida esperada:
# === RANKING DE GÉNEROS DATAFEST 2026 ===
# #1  Rock         ████ 4 artistas
# #2  Electrónica  ███  3 artistas
# #3  Reggaeton    ██   2 artistas
# #4  Folk         ██   2 artistas
# #5  Hip-Hop      ██   2 artistas
# #6  Cumbia       █    1 artistas
