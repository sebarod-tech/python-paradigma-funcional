from functools import reduce

# Lista de ventas
ventas = [
    {"cliente": "Juan", "monto": 1500, "categoria": "A"},
    {"cliente": "Ana", "monto": 800, "categoria": "B"},
    {"cliente": "Luis", "monto": 2000, "categoria": "A"},
    {"cliente": "Sofia", "monto": 1200, "categoria": "C"},
    {"cliente": "Pedro", "monto": 500, "categoria": "B"},
    {"cliente": "Maria", "monto": 3000, "categoria": "A"}
]

# Función para aplicar descuento según categoría
def aplicar_descuento(venta):
    descuentos = {
        "A": 0.20,
        "B": 0.10,
        "C": 0.05
    }
    
    descuento = descuentos.get(venta["categoria"], 0)
    
    # Se devuelve una nueva venta (no se modifica la original)
    return {
        "cliente": venta["cliente"],
        "monto_original": venta["monto"],
        "categoria": venta["categoria"],
        "monto_final": venta["monto"] * (1 - descuento)
    }

# 1. Filtrar ventas mayores a 1000
ventas_filtradas = list(filter(lambda v: v["monto"] > 1000, ventas))

# 2. Aplicar descuentos
ventas_procesadas = list(map(aplicar_descuento, ventas_filtradas))

# 3. Calcular total
total = reduce(lambda acc, v: acc + v["monto_final"], ventas_procesadas, 0)

# 4. Calcular promedio
promedio = total / len(ventas_procesadas) if ventas_procesadas else 0

# Mostrar resultados
print("Ventas originales:")
for v in ventas:
    print(v)

print("\nVentas filtradas (>1000):")
for v in ventas_filtradas:
    print(v)

print("\nVentas con descuento aplicado:")
for v in ventas_procesadas:
    print(v)

print("\nTotal final:", total)
print("Promedio final:", promedio)
