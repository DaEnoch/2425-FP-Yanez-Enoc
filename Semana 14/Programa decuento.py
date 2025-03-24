# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):

    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

monto_compra1 = 1000
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

# Asigno el monto total de la compra y el porcentaje de descuento
monto_compra2 = 2000
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2

# Imprimo los resultados

print(f"Compra 1 - Monto total: ${monto_compra1:.2f} USD, Descuento: ${descuento1:.2f} USD, Monto final: ${monto_final1:.2f} USD")
print(f"Compra 2 - Monto total: ${monto_compra2:.2f} USD, Descuento: ${descuento2:.2f} USD, Monto final: ${monto_final2:.2f} USD")