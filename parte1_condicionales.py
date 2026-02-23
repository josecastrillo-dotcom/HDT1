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
cantidad      = 4

# --- Tu código aquí ---

precio_final = 0   # reemplaza con tu lógica

# 1: Determina el precio base según zona
#         (campo, gradería, preferencia, vip o zona inválida)
if zona == "campo":
    precio_base = 200
elif zona == "gradería" or zona == "graderia":
    precio_base = 350
elif zona == "preferencia":
    precio_base = 600
elif zona == "vip":
    precio_base = 1200
else:
    precio_base = 0

# 2: Calcula el porcentaje de descuento más alto que aplica
descuento = 0
razon_descuento = "sin descuento"

if es_ufm and carnet_valido:
    descuento = 0.25
    razon_descuento = "estudiante UFM"
elif dias_anticipacion <= 30:
    descuento = 0.15
    razon_descuento = "compra anticipada"
elif edad < 12 or edad > 64:
    descuento = 0.50
    razon_descuento = "edad"

# 3: Aplica el descuento al precio base
precio_base_descuento = precio_base * (1 - descuento)

# 4: Si cantidad > 4, aplica 10% adicional sobre el precio descontado
total_sin_volumen = precio_base_descuento * cantidad
total_descuento_volumen = 0.0
precio_final = total_sin_volumen

if cantidad > 4:
    total_descuento_volumen = total_sin_volumen * 0.10
    precio_final = total_sin_volumen - total_descuento_volumen


# 5: Imprime el resumen con el formato esperado:
# === ENTRADA DATAFEST 2026 ===
# Zona       : vip
# Precio base: Q1200.00
# Descuento  : 25.0% (estudiante UFM)
# Precio/entrada: Q900.00
# Descuento volumen (5 entradas): -Q450.00
# TOTAL A PAGAR: Q4050.00

print("=== ENTRADA DATAFEST 2026 ===")
print(f"Zona       : {zona}")
print(f"Precio base: Q{precio_base:.2f}")
print(f"Descuento  : {descuento*100:.1f}% ({razon_descuento})")
print(f"Precio/entrada: Q{precio_base_descuento:.2f}")
if cantidad > 4:
    print(f"Descuento volumen ({cantidad} entradas): -Q{total_descuento_volumen:.2f}")
print(f"TOTAL A PAGAR: Q{precio_final:.2f}")

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
    if not entrada:
        estado = "DENEGADO"
        mensaje = "Sin entrada valida"
    elif zona_c in ["vip", "backstage"] and not pulsera:
        estado = "DENEGADO"
        mensaje = "Zona VIP requiere pulsera especial"
    elif edad_c < 18 and not acompanante:
        estado = "DENEGADO"
        mensaje = "Menor de edad requiere acompañante"
    elif prohibicion:
        estado = "DENEGADO"
        mensaje = "Acceso prohibido por restricciones"
    else:
        estado = "PERMITIDO"
        mensaje = f"Bienvenido/a a zona: {zona_c}"
    # TODO: Imprime "Caso N: [PERMITIDO] ..." o "Caso N: [DENEGADO] ..."
    print(f"Caso {i}: [{estado}] {mensaje}")

# Salida esperada:
# Caso 1: [DENEGADO] Sin entrada válida
# Caso 2: [DENEGADO] Zona VIP requiere pulsera especial
# Caso 3: [DENEGADO] Menor de edad requiere acompañante
# Caso 4: [PERMITIDO] Bienvenido/a a zona: preferencia
