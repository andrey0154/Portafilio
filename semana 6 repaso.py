vueltas_totales = 0
tiempo_vuelta_acumulado = 0
pits_totales = 0
tiempo_pits_acumulado = 0

while True:
    tiempo_vuelta = input("Ingresa el tiempo de vuelta (en segundos) o ingresa 0 para terminar: ")
    if tiempo_vuelta == "0":
        break
    if tiempo_vuelta.isdigit():
        tiempo_vuelta_num = float(tiempo_vuelta)
        vueltas_totales += 1
        tiempo_vuelta_acumulado += tiempo_vuelta_num
    else:
        print("Por favor, ingresa un número válido (número entero o decimal).")

    tiempo_pits = input("Ingresa el tiempo en PITS (en segundos) o ingresa 0 para terminar: ")
    if tiempo_pits == "0":
        break
    if tiempo_pits.isdigit():
        tiempo_pits_num = float(tiempo_pits)
        pits_totales += 1
        tiempo_pits_acumulado += tiempo_pits_num
    else:
        print("Por favor, ingresa un número válido (número entero o decimal).")

tiempo_promedio_vuelta = tiempo_vuelta_acumulado / vueltas_totales if vueltas_totales > 0 else 0
tiempo_promedio_pits = tiempo_pits_acumulado / pits_totales if pits_totales > 0 else 0
porcentaje_tiempo_pits = (tiempo_pits_acumulado / (tiempo_vuelta_acumulado + tiempo_pits_acumulado)) * 100


print("\nEstadísticas de los tiempos de vuelta y PITS:")
print(f"Tiempo promedio por vuelta: {tiempo_promedio_vuelta:.2f} segundos")
print(f"Tiempo promedio en PITS: {tiempo_promedio_pits:.2f} segundos")
print(f"Porcentaje de tiempo en PITS: {porcentaje_tiempo_pits:.2f}%")





# Programa 2

menores_100 = 0
entre_100_y_120 = 0
entre_121_y_130 = 0
entre_131_y_140 = 0
mayores_140 = 0
total_estaturas = 0
estatura_acumulada = 0

while True:
    estatura = input("Ingresa la estatura del niño (en cm) o ingresa 0 para terminar: ")
    if estatura == "0":
        break
    if estatura.isdigit():
        estatura_num = float(estatura)
        if estatura_num < 100:
            menores_100 += 1
        elif 100 <= estatura_num < 120:
            entre_100_y_120 += 1
        elif 120 <= estatura_num < 130:
            entre_121_y_130 += 1
        elif 130 <= estatura_num < 140:
            entre_131_y_140 += 1
        elif estatura_num >= 140:
            mayores_140 += 1
        estatura_acumulada += estatura_num
        total_estaturas += 1
    else:
        print("Por favor, ingresa un número válido (número entero o decimal).")

promedio_estaturas = estatura_acumulada / total_estaturas if total_estaturas > 0 else 0


print("\nEstadísticas de las estaturas:")
print(f"Cantidad de niños que miden menos de 100 cm: {menores_100}")
print(f"Cantidad de niños que miden entre 100 y 120 cm: {entre_100_y_120}")
print(f"Cantidad de niños que miden entre 121 y 130 cm: {entre_121_y_130}")
print(f"Cantidad de niños que miden entre 131 y 140 cm: {entre_131_y_140}")
print(f"Cantidad de niños que miden más de 140 cm: {mayores_140}")
print(f"Promedio de estaturas: {promedio_estaturas:.2f} cm")




# Programa 3
valor = float(input("Ingresa un valor: "))


numeros_divisibles = []
i = 1
while len(numeros_divisibles) < 10:
    if i % valor == 0:
        numeros_divisibles.append(i)
    i += 1


print("\nLos primeros 10 números divisibles entre el valor ingresado son:")
for i, numero in enumerate(numeros_divisibles, start=1):
    print(f"{i}. {numero}")



# Programa 4

salarios = []
for i in range(15):
    salario = float(input(f"Ingresa el salario {i + 1}: "))
    salarios.append(salario)


dinero_necesario = 0
for salario in salarios:
    if salario < 500:
        dinero_necesario += 500 - salario


print("\nPara que a menos todos ganen $500, se necesita:")
print(f"{dinero_necesario:.2f} dólares")