
ingresos_mensuales = float(input("Por favor, ingresa tus ingresos mensuales: "))
gastos_alimentacion = float(input("Ahora, ingresa tus gastos mensuales en alimentación: "))

# Calcular porcentajes
porcentaje_gasto_alimentacion = (gastos_alimentacion / ingresos_mensuales) * 100
porcentaje_disponible_otros_rubros = 100 - porcentaje_gasto_alimentacion

# Resultados
print("\nResumen de tus Finanzas:")
print(f"  - Porcentaje de ingresos destinado a alimentación: {porcentaje_gasto_alimentacion:.2f}%")
print(f"  - Porcentaje disponible para otros rubros: {porcentaje_disponible_otros_rubros:.2f}%")
