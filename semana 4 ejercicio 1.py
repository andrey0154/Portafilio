
salario = input("ingrese su salario")
salario = int (salario)

categoria = input ("su categoria es 1 , 2 , 3 ,4")
categoria= int (categoria)

if categoria ==1:
    porcentaje = salario *0.10
   
elif categoria == 2:
   categoria =salario * 0.20 
       
elif categoria ==3:
    categoria=salario * 0.30 
     
elif categoria == 4:
    categoria= salario * 0.40 

print ("su aumento de salario es ")
