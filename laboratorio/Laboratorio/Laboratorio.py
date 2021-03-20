import os
import itertools
while True:
    e = 2.718
    print("************Laboratorio************")
    print("	1 => Poisson	")     
    print("	2 => Binomial	")
    print("        3 => Normal     ")
    print("	4 => salir	    ")
    
    opcion=input()
    if opcion== '1':
       
        print("*Elegido Poison*")
        pp =int(input("Ingrese miu: "))
        kk =int(input("Ingrese k: "))
        
        
        fact = 1
        for n in range(1, (kk + 1)):
            fact = fact* n
        prob = (  (pp**kk)*(e**(-pp))  )  /  fact
        prob2 = prob * 100
        print("\PROBABILIDAD DE:", prob2)

    elif opcion== '2':

        print("**Elegido Bionomial**")
        n =int(input("Ingrese número de ensayos: "))
        k =int(input("Ingrese número de éxitos: "))
        p =float(input("Ingrese probabilidad de éxitos: "))
        q =float(input("Ingrese probabilidad de fracasos: "))

        # Factorial
        factorial = 1
        for n in range(1, (k + 1)):
            factorial = factorial * n

        probabilidad = ((n/k) * ((p ** k)*(q ** (n-k))))
        probabilidad2 = probabilidad * 100
        print("\nLa probabilidad es :", probabilidad2)

    elif opcion == '3':
        break

    elif opcion == '4':
        break
    input()