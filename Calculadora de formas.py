import math

def calcular_area(figura, medidas):
    if figura == "C":
        return medidas[0] ** 2
    elif figura == "T":
        return (medidas[0] * medidas[1]) / 2
    elif figura == "R":
        return medidas[0] * medidas[1]
    elif figura == "CI":
        return math.pi * medidas[0] ** 2
    else:
        return None

def calcular_perimetro(figura, medidas):
    if figura == "C":
        return 4 * medidas[0]
    elif figura == "T":
        return 3 * medidas[0]
    elif figura == "R":
        return 2 * (medidas[0] + medidas[1])
    elif figura == "CI":
        return 2 * math.pi * medidas[0]
    else:
        return None

def main():
    figura = input("Ingrese el tipo de figura a calcular (C para cuadrado, T para triángulo, R para rectángulo, CI para círculo): ").upper()

    if figura in ["C", "T", "R", "CI"]:
        medidas = [float(input(f"Ingrese la medida {(i+1)}: ")) for i in range(2 if figura == "T" else 1)]
        area = calcular_area(figura, medidas)
        perimetro = calcular_perimetro(figura, medidas)
        if area is not None and perimetro is not None:
            print("El área es:", area)
            print("El perímetro es:", perimetro)
        else:
            print("Error al calcular. Verifique los datos ingresados.")
    else:
        print("Figura no válida. Por favor, ingrese 'C' para cuadrado, 'T' para triángulo, 'R' para rectángulo o 'CI' para círculo.")

if __name__ == "__main__":
    main()
