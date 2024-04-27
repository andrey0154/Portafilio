
horas_semanales_trabajadas = float(input("Ingrese las horas semanales trabajadas: "))
pago_por_hora = float(input("Ingrese el pago por hora: "))


salario_bruto = horas_semanales_trabajadas * pago_por_hora * 4.2 * 4  # Considerando 4.2 semanas por mes
deducciones = salario_bruto * (0.105 + 0.05)  # Deducciones por cargas sociales (10.5%) y asociación solidarista (5%)
salario_neto = salario_bruto - deducciones


print(f"El salario mensual después de deducciones es: {salario_neto:.2f} colones")

