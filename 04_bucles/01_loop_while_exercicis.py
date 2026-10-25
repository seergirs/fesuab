###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
i=0
while i<10:
    i+=1
    print(i)
    
# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
i=1
suma=0
while i<=20:
    if i%2==0:
        suma+=i
    i+=1

print(f"La suma es: {suma}")


# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

numero=int(input("Introdueixi un numero enter positiu: "))
i=numero
factorial=1

while i!=1:
    factorial*=i
    i-=1

print(f"El factorial de {numero} és {factorial}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contrasena=""
while len(contrasena)<8:
    contrasena=input("Introdueix una contraseña (almenys 8 caràcters): ")
    if len(contrasena)<8:
        print("La contraseña ha de tener almenys 8 caràcters. Torna a introduir.")

print("Contraseña vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
numero=int(input("Introdueix un número: "))
i=1
print(f" | Taula de multiplicar del {numero} |")
while i<=10:
    print(f"{i}x{numero}={i*numero}")
    i+=1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.


print("\nExercici 6:")
n = int(input("Introdueix un número enter positiu N: "))

numero = 2
while numero <= n:
  es_primer = True  
  divisor = 2
  while divisor * divisor <= numero: 
    if numero % divisor == 0:
      es_primer = False  
      break
    divisor += 1
  if es_primer:
    print(numero)

  numero += 1


# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
suma=0

numero=int(input("Introdueix un numero enter: "))
while numero!=0:
   suma+=numero
   numero=int(input("Introdueix un numero enter: "))
   

print(f"La suma es {suma}")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
numero=int(input("Introdueix un numero enter positiu: "))
i=0

while numero>0:
   numero//=10
   xifres+=1
print(f"El numero te {xifres} xifres")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

termes = int(input("Quants termes de Fibonacci vols veure? "))
anterior = 0
actual = 1
comptador = 0

while comptador < termes:
  print(anterior)
  seguent = anterior + actual
  anterior = actual
  actual = seguent
  comptador += 1
   
# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

numero_secret = 3
intent = int(input("Endevina el número secret: "))

while intent != numero_secret:
  if intent < numero_secret:
    print("El número secret és més gran.")
  else:
    print("El número secret és més petit.")
  intent = int(input("Torna-ho a provar: "))

print("Correcte! Has endevinat el número.")

