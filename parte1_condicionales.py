# ============================================================
#  HDT1 — Parte 1: Condicionales
#  DataFest 2026 — Sistema de Operaciones
# ============================================================

# ============================================================
#  Ejercicio 1.1 — Precios Dinámicos de Entradas  (10 pts)
# ============================================================
# Precios base: campo=Q200, gradería=Q350, preferencia=Q600, vip=Q1200
#
# Descuento mayor aplica (NO acumulables entre sí):
#   - Estudiante UFM con carnet válido    → 25%
#   - Compra en los primeros 30 días  → 15%
#   - Menor de 12 O mayor de 64 años      → 50%
#
# Regla adicional (sí aplica SOBRE el precio ya descontado):
#   - Más de 4 entradas de la misma zona  → 10% extra



# --- Datos de prueba (NO modificar) ---
zona          = "vip"
edad          = 30
es_ufm        = True
carnet_valido = True
dias_anticipacion = 35
cantidad      = 5

# --- Tu código aquí ---

precio_final = 0   # reemplaza con tu lógica

# TODO 1: Determina el precio base según zona
#         (campo, gradería, preferencia, vip o zona inválida)

# TODO 2: Calcula el porcentaje de descuento más alto que aplica

# TODO 3: Aplica el descuento al precio base

# TODO 4: Si cantidad > 4, aplica 10% adicional sobre el precio descontado

# TODO 5: Imprime el resumen con el formato esperado:
# === ENTRADA DATAFEST 2026 ===
# Zona       : vip
# Precio base: Q1200.00
# Descuento  : 25.0% (estudiante UFM)
# Precio/entrada: Q900.00
# Descuento volumen (5 entradas): -Q450.00
# TOTAL A PAGAR: Q4050.00


# ============================================================
#  Ejercicio 1.2 — Control de Acceso al Festival  (10 pts)
# ============================================================
# Evalúa TODAS las reglas en orden:
#   1. Sin entrada válida             → denegado
#   2. Zona vip/backstage sin pulsera → denegado
#   3. Menor de 18 sin acompañante    → denegado
#   4. prohibicion = True             → denegado (siempre)
#   5. Si pasa todo lo anterior       → permitido
#
# Formato: "Caso N: [PERMITIDO/DENEGADO] mensaje"

# --- Datos de prueba (NO modificar) ---
casos_acceso = [
    # (zona,         edad, tiene_entrada, pulsera_especial, con_acompanante, prohibicion)
    ("vip",          25,   False,         True,             True,            False),  # sin entrada
    ("vip",          22,   True,          False,            True,            False),  # sin pulsera
    ("campo",        16,   True,          False,            False,           False),  # menor sin acomp.
    ("preferencia",  30,   True,          False,            True,            False),  # todos ok
]

# --- Tu código aquí ---

for i, caso in enumerate(casos_acceso, start=1):
    zona_c, edad_c, entrada, pulsera, acompanante, prohibicion = caso

    # TODO: Evalúa las reglas en orden y construye el mensaje
    # TODO: Imprime "Caso N: [PERMITIDO] ..." o "Caso N: [DENEGADO] ..."
    pass

# Salida esperada:
# Caso 1: [DENEGADO] Sin entrada válida
# Caso 2: [DENEGADO] Zona VIP requiere pulsera especial
# Caso 3: [DENEGADO] Menor de edad requiere acompañante
# Caso 4: [PERMITIDO] Bienvenido/a a zona: preferencia
