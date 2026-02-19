# Hoja de Trabajo 1 — Fundamentos de Programación
## DataFest 2026: Sistema de Operaciones del Festival

**Asignatura:** Fundamentos de Programación — Sección C
**Universidad:** Francisco Marroquín
**Valor:** 5 puntos sobre la nota final
**Entrega:** Martes 24 de febrero de 2026 antes de las 8:30 AM
**Modalidad:** Individual

---

## Contexto

Eres el/la nuevo/a desarrollador/a júnior de **DataFest 2026**, el festival de tecnología más
grande de Guatemala. El equipo organizador necesita urgentemente varios módulos del sistema
de operaciones del evento y tú eres el único disponible.

Tu misión: completar los archivos `.py` que dejó incompletos el desarrollador anterior,
quien misteriosamente desapareció después de tomar demasiado café.

> Cada archivo `.py` contiene variables ya definidas y comentarios `# TODO` que indican qué
> debes completar. **No cambies** los nombres de las variables ya definidas ni los valores
> de prueba — el calificador depende de ellos.

---

## Reglas

1. **Solo Python básico**: no importes librerías externas (`math`, `random`, `statistics`, etc.)
2. **Restricciones por ejercicio**: donde dice "SIN usar X", en serio no lo uses
3. **Sin funciones**: no definas funciones con `def` (se verán la próxima semana)
4. **El código debe ejecutarse sin errores**: archivo que no corre = 0 en ese archivo
5. **Verifica los casos de prueba**: cada ejercicio incluye el output esperado en comentarios

---

## Estructura y Puntos

| Archivo                    | Tema                  | Puntos |
|----------------------------|-----------------------|--------|
| `parte1_condicionales.py`  | Condicionales         | 20 pts |
| `parte2_strings.py`        | Strings               | 20 pts |
| `parte3_listas.py`         | Listas                | 20 pts |
| `parte4_ciclos.py`         | Ciclos (for y while)  | 25 pts |
| `parte5_integrador.py`     | Integrador            | 15 pts |
| **Total**                  |                       | **100 pts** |

---

## Parte 1: Condicionales (20 pts)

### Ejercicio 1.1 — Precios Dinámicos de Entradas (10 pts)

DataFest vende entradas en 4 zonas con precios base:

| Zona          | Precio base |
|---------------|-------------|
| `"campo"`     | Q200        |
| `"gradería"`  | Q350        |
| `"preferencia"` | Q600      |
| `"vip"`       | Q1200       |

**Reglas de descuento** — aplica el mayor, **NO son acumulables entre sí**:

| Condición                                          | Descuento |
|----------------------------------------------------|-----------|
| Estudiante UFM con `carnet_valido = True`          | 25%       |
| Compra con `dias_anticipacion > 30`                | 15%       |
| `edad < 12` o `edad >= 65`                         | 50%       |

**Regla adicional** (sí aplica sobre el precio ya descontado):
- Si `cantidad > 4` entradas de la misma zona: 10% adicional.

**Caso especial**: si la zona no existe → imprimir `"Error: zona '[zona]' no válida"` y
asignar `precio_final = -1`.

**Output esperado** (con los valores de prueba del archivo):
```
=== ENTRADA DATAFEST 2026 ===
Zona       : vip
Precio base: Q1200.00
Descuento  : 25.0% (estudiante UFM)
Precio/entrada: Q900.00
Descuento volumen (5 entradas): -Q450.00
TOTAL A PAGAR: Q4050.00
```

### Ejercicio 1.2 — Control de Acceso al Festival (10 pts)

El sistema verifica el acceso según estas reglas (evalúa **todas**, en orden):

1. Sin entrada válida → denegado
2. Zona `"vip"` o `"backstage"` sin `pulsera_especial` → denegado
3. Menor de 18 años sin `con_acompanante` → denegado
4. `prohibicion = True` → denegado (sin importar lo demás)
5. Si pasa todo lo anterior → permitido

**Output esperado** (para los 4 casos de prueba del archivo):
```
Caso 1: [DENEGADO] Sin entrada válida
Caso 2: [DENEGADO] Zona VIP requiere pulsera especial
Caso 3: [DENEGADO] Menor de edad requiere acompañante
Caso 4: [PERMITIDO] Bienvenido/a a zona: preferencia
```

---

## Parte 2: Strings (20 pts)

### Ejercicio 2.1 — Generador de Credenciales (8 pts)

Genera una credencial única con el formato: `FD26-[ZONA3]-[INICIALES][NUMERO]`

- `ZONA3`: primeras **3 letras de la zona** en MAYÚSCULAS (`"campo"` → `"CAM"`)
- `INICIALES`: primera letra del **nombre** + primera letra del **apellido**, ambas en MAYÚSCULAS
- `NUMERO`: número de registro con **4 dígitos** rellenado con ceros (`str(n).zfill(4)`)

**Output esperado:**
```
FD26-VIP-CM0047
FD26-CAM-AG0005
FD26-GRA-JR1823
FD26-PRE-ML0312
```

> Pista: para el apellido, `nombre.split()` separa las palabras del nombre completo.
> El apellido es el último elemento de esa lista.

### Ejercicio 2.2 — Limpieza de Datos de Asistentes (6 pts)

El sistema externo envía datos en formato crudo (un string con campos separados por coma):

```
"  ana GARCIA    ,   ana.garcia@gmail.com  ,   22  "
```

Procesa cada campo y:
- **Nombre**: `.strip()` + `.title()` para capitalizar correctamente
- **Email**: `.strip()` + `.lower()`; verificar que contenga `@` y que haya un `.` después del `@`
- **Edad**: `.strip()` + `int()`; validar que esté en el rango [5, 100]

**Output esperado** (para los 3 registros de prueba del archivo):
```
--- Registro 1 ---
Nombre : Ana Garcia
Email  : ana.garcia@gmail.com | Válido: Sí
Edad   : 22 | En rango: Sí

--- Registro 2 ---
Nombre : José Luis Pérez
Email  : jl_perez@outlook | Válido: No
Edad   : 17 | En rango: Sí

--- Registro 3 ---
Nombre : María Fernanda Solís
Email  : mfernanda@ufm.edu | Válido: Sí
Edad   : 150 | En rango: No — fuera del rango [5, 100]
```

### Ejercicio 2.3 — Análisis de Reseñas (6 pts)

Analiza las reseñas escritas por los asistentes al festival. Para cada reseña calcula:

1. **Total de palabras** (`.split()`)
2. **Total de vocales** — cuenta `a e i o u á é í ó ú` (mayúsculas y minúsculas)
3. **Palabra más larga** (en caso de empate, la primera que aparezca)
4. **Sentimiento**:
   - Positivas: `"increíble"`, `"excelente"`, `"genial"`, `"espectacular"`, `"maravilloso"`, `"fantástico"`
   - Negativas: `"malo"`, `"pésimo"`, `"terrible"`, `"aburrido"`, `"decepcionante"`, `"horrible"`
   - Ambas → `"mixta"` / Solo positivas → `"positiva"` / Solo negativas → `"negativa"` / Ninguna → `"neutral"`

**Output esperado** (para las 2 reseñas de prueba del archivo):
```
--- Reseña 1 ---
Palabras      : 14
Vocales       : 27
Palabra larga : "espectacular"
Sentimiento   : positiva

--- Reseña 2 ---
Palabras      : 12
Vocales       : 22
Palabra larga : "decepcionante"
Sentimiento   : mixta
```

---

## Parte 3: Listas (20 pts)

### Ejercicio 3.1 — Gestión de Zona VIP (10 pts)

Partiendo de:
```python
lista_espera = ["Valentina", "Diego", "Alejandra", "Kim", "Lu", "Marcelo", "Nati"]
capacidad_vip = 5
zona_vip = []
```

Realiza las operaciones **en este orden exacto**:

1. Agregar `"Óscar"` y `"Paula"` al **final** de `lista_espera`
2. `"Diego"` cancela — **removerlo** de `lista_espera`
3. **Mover** las primeras `capacidad_vip` personas de `lista_espera` a `zona_vip`
   (elimínalas de `lista_espera` al moverlas)
4. En `zona_vip`, a todo nombre con **más de 5 caracteres** agrégarle `" ★"` al final
5. Imprimir el estado final

**Output esperado:**
```
ZONA VIP (5/5)  : ['Valentina ★', 'Alejandra ★', 'Kim', 'Lu', 'Marcelo ★']
EN ESPERA (3)   : ['Nati', 'Óscar', 'Paula']
```

### Ejercicio 3.2 — Ajuste de Precios con IVA (10 pts)

```python
precios_con_iva = [224.00, 392.00, 672.00, 1344.00, 56.00, 448.00]
# IVA Guatemala = 12%  →  precio_sin_iva = precio_con_iva / 1.12
```

Crea las siguientes listas usando ciclos `for`:

a) `precios_sin_iva` — todos los precios sin IVA (usa `round(x, 2)`)
b) `precios_accesibles` — solo los precios sin IVA que sean **menores a Q400**
c) `precios_formateados` — lista de strings con formato `"Q{precio:.2f}"` de **todos** los precios sin IVA

**Output esperado:**
```
Sin IVA        : [200.0, 350.0, 600.0, 1200.0, 50.0, 400.0]
Accesibles     : [200.0, 350.0, 50.0]
Formateados    : ['Q200.00', 'Q350.00', 'Q600.00', 'Q1200.00', 'Q50.00', 'Q400.00']
```

---

## Parte 4: Ciclos (25 pts)

### Ejercicio 4.1 — Reporte Visual de Afluencia por Hora (8 pts)

> **Prohibido usar `max()`** para encontrar la hora pico.

Con la lista `afluencia_por_hora` (índice = hora del día, 0–23), genera un reporte de barras
donde cada `█` representa **30 asistentes** (usar `//`). Mostrar solo horas con afluencia > 0.
Agregar `[PICO]` a las horas con afluencia >= 300.

**Output esperado (fragmento):**
```
=== AFLUENCIA POR HORA ===
Hora 08 | █ 45 asistentes
Hora 09 | ████ 120 asistentes
Hora 10 | ███████ 230 asistentes
Hora 11 | ██████████ 310 asistentes [PICO]
...
Hora 22 | 10 asistentes

Total del día     : 3,122 asistentes
Hora pico         : Hora 16 con 420 asistentes
```

> Nota: si `afluencia // 30 == 0`, la barra queda vacía — está bien, igual muestra el número.

### Ejercicio 4.2 — Simulador de Plan de Pagos (8 pts)

Un asistente quiere pagar su entrada VIP (Q1,200) en cuotas mensuales.

**Validación con `while`** (pedir al usuario la cuota):
- Mínimo: Q100 — Máximo: Q600 — Debe ser **múltiplo de 50** (`cuota % 50 == 0`)
- Si no cumple, mostrar el error específico y pedir de nuevo

**Una vez validada**, simular el plan:
- Mostrar cada cuota, su número y el saldo pendiente
- La **última cuota** puede ser menor que la cuota acordada (no cobrar de más)

**Output esperado** (si el usuario ingresa cuota = Q250):
```
Cuota ingresada válida: Q250.00

=== PLAN DE PAGOS ===
Cuota #1 : Q250.00 | Saldo restante: Q950.00
Cuota #2 : Q250.00 | Saldo restante: Q700.00
Cuota #3 : Q250.00 | Saldo restante: Q450.00
Cuota #4 : Q250.00 | Saldo restante: Q200.00
Cuota #5 : Q200.00 | Saldo restante: Q0.00

Total de cuotas : 5
Total pagado    : Q1200.00
```

### Ejercicio 4.3 — Ranking de Géneros Musicales (9 pts)

> **Prohibido usar diccionarios** — solo listas (aún no las hemos visto).

Dado el cartel de artistas (lista de tuplas `(nombre, genero)`):

1. Usa `for` para contar artistas por género, almacenando los resultados en dos listas
   paralelas: `generos` y `conteos`
   - Si el género ya existe en `generos`, incrementa su conteo
   - Si no existe, agrégalo junto con conteo `1`

2. Ordena el ranking de **mayor a menor** usando un ordenamiento básico
   *(tip: intercambia elementos usando `generos[i], generos[j] = generos[j], generos[i]`
   y lo mismo para `conteos`)*

3. Muestra el ranking con barra visual (cada `█` = 1 artista):

**Output esperado:**
```
=== RANKING DE GÉNEROS DATAFEST 2026 ===
#1  Rock         ████ 4 artistas
#2  Electrónica  ███  3 artistas
#3  Reggaeton    ██   2 artistas
#4  Folk         ██   2 artistas
#5  Hip-Hop      ██   2 artistas
#6  Cumbia       █    1 artistas
```

---

## Parte 5: Integrador (15 pts)

### Sistema de Taquilla Virtual

Construye un sistema interactivo de taquilla para DataFest 2026 usando un ciclo `while`.

**Menú principal:**
```
========================================
       TAQUILLA DATAFEST 2026
========================================
1. Ver cartel de artistas
2. Comprar entrada
3. Ver mis compras
4. Resumen de gastos
5. Salir
```

**Requerimientos por opción:**

**Opción 1 — Ver cartel:**
- Mostrar todos los artistas con `enumerate()`, su turno y género
- Formato: `[N] Nombre (Género) — Turno: X`

**Opción 2 — Comprar entrada:**
- Pedir zona y cantidad
- Aplicar precios base (sin descuentos, para simplificar):
  `campo=Q200, gradería=Q350, preferencia=Q600, vip=Q1200`
- Validar zona con `while` — si no existe, pedir de nuevo
- Agregar la compra a la lista `mis_compras` como `[zona, cantidad, total]`
- Mostrar confirmación con el total

**Opción 3 — Ver mis compras:**
- Si no hay compras: `"Aún no has comprado entradas."`
- Si hay: mostrar tabla con zona, cantidad y monto de cada compra

**Opción 4 — Resumen:**
- Total gastado (implementado con `for`, sin `sum()`)
- Total de entradas compradas
- Zona con más compras (la que aparece más veces)

**Opción 5 — Salir:**
- Imprimir mensaje de despedida y salir del ciclo

**Manejo de opción inválida:**
- Si el usuario ingresa una opción que no existe: `"Opción no válida. Intenta de nuevo."`

---

## Rúbrica de Calificación

| Criterio        | Descripción                                               |
|-----------------|-----------------------------------------------------------|
| Correctitud     | El código produce los outputs esperados                   |
| Lógica          | La implementación es coherente con los conceptos vistos   |
| Sin errores     | El archivo corre sin excepciones                          |
| Restricciones   | Se respetan los `SIN usar X` de cada ejercicio            |

**Penalizaciones:**
- Archivo que no corre: −5 pts sobre ese archivo
- Usar función prohibida: −2 pts por instancia
- Modificar variables de prueba ya definidas: −3 pts por instancia

---

## Cómo Entregar

1. Haz **fork** de este repositorio en tu cuenta de GitHub
2. Trabaja en los archivos `.py` y guarda tus cambios localmente
3. Antes de entregar, verifica que cada archivo corra sin errores:
   ```bash
   python parte1_condicionales.py
   python parte2_strings.py
   python parte3_listas.py
   python parte4_ciclos.py
   python parte5_integrador.py
   ```
4. En tu fork en GitHub, usa **Add file → Upload files** y sube los archivos `.py` actualizados
5. Verifica **dos veces** que estás subiendo a **tu fork** (tu usuario) y no al repositorio original

---

*DataFest 2026 — Fundamentos de Programación, Sección C — UFM*
# HDT1
