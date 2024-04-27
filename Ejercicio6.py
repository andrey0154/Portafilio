distancia_casa_universidad = float(input("¿Cuántos kilómetros separan su casa de la universidad?: "))
costo_por_km = float(input("costo por kilómetro de su viaje: "))
dias_por_semana = int(input("¿días a la semana viaja a la universidad?: "))

semanas_por_cuatrimestre = 15


costo_total = distancia_casa_universidad * costo_por_km * dias_por_semana * 2 * semanas_por_cuatrimestre  # Ida y vuelta


print(f"\nEl costo total de trasladarse a la universidad por cuatrimestre es: {costo_total:.2f} colones")
