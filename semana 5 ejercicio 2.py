
nota_mayor = 0
nota_menor = 0
aprobados = 0
reprobados = 0

for alumno in range (10):
    nota = int (input ("ingerese nota que obtuvo"))
    if nota >70:
        nota_mayor =nota_menor+1

    elif nota <70:
         nota_menor =  nota_mayor+1

    if nota > nota_mayor:
        nota_mayor = nota
    
    if nota < nota_menor:
        nota_menor = nota

print("cual es la nota mayor",nota_mayor)
print("cual es la nota menor",nota_menor )

print ("la cantidad de alumnos aprobados es", nota_mayor)
print ("la cantidad de alumnos reprobados es", nota_menor)
        
