import os

def convertir_a_binario(numero):
    return bin(numero)[2:]

def convertir_a_octal(numero):
    return oct(numero)[2:]

def convertir_a_hexadecimal(numero):
    return hex(numero)[2:]

def mostrar_numero_en_base(numero, base):
    if base == 2:
        print(f"El número {numero} en base {base} es {convertir_a_binario(numero)}")
    elif base == 8:
        print(f"El número {numero} en base {base} es {convertir_a_octal(numero)}")
    elif base == 16:
        print(f"El número {numero} en base {base} es {convertir_a_hexadecimal(numero)}")
    else:
        print("La base proporcionada no es válida. Debe ser 2, 8 o 16.")

def main():
    numero = int(input("Ingrese un número: "))
    print(f"El número {numero} en binario es {convertir_a_binario(numero)}")
    print(f"El número {numero} en octal es {convertir_a_octal(numero)}")
    print(f"El número {numero} en hexadecimal es {convertir_a_hexadecimal(numero)}")

    base = int(input("Ingrese una base (2, 8, 16): "))
    mostrar_numero_en_base(numero, base)

if __name__ == "__main__":
    main()


