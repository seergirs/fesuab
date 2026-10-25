###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
a=int(input("Introdueix el primer nombre:"))
b=int(input("Introdueix el segon primer nombre: "))

if a>b:
    print(f"El nombre {a} és mes gran que el nombre {b}")
elif a<b:
    print(f"El nombre {b} és mes gran que el nombre {a}")
else:
    print(f"El nombres son iguals")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

a=int(input("Introdueix el primer nombre:"))
b=int(input("Introdueix el segon primer nombre: "))
operacio = input("Introdueix l'operació (+, -, *, /): ").strip()

if operacio == "/" and b == 0:
    print("Error: no es pot dividir per zero.")
elif operacio == "+":
    resultat = a + b
    print(f"El resultat és: {resultat}")
elif operacio == "-":
    resultat = a - b
    print(f"El resultat és: {resultat}")
elif operacio == "*":
    resultat = a* b
    print(f"El resultat és: {resultat}")
elif operacio == "/":
    resultat = a / b
    print(f"El resultat és: {resultat}")
else:
    print("Operació no vàlida.")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.
any=int(input=("Introdueix un any: "))

if any%4==0 and any%100!=0 and any%400==0:
    print("És un any de traspás")
else:
    print("No és un any de traspás")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
edad=int(input=("Introdueix una edad: ") )

if 0<=edad<=2:
    print("Nadó")
elif 3<=edad<=12:
    print("Infant")
elif 13<=edad<=17:
    print("Adolescent")
elif 18<=edad<=64:
    print("Adult")
elif edad>=65:
    print("Persona gran")
else:
    print("Edad no vàlida")
# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

rssi=int(floate("Introdueix un nivell de senyal rebut (RSSI): "))
if rssi >= -50:
    print("Cobertura excel·lent.")
elif rssi >= -67:
    print("Cobertura bona.")
elif rssi >= -75:
    print("Cobertura feble.")
else:
    print("Cobertura molt feble.")

# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potencia=float(input=("Introdueix una potència òptica: "))
if potencia < -27:
    print("El nivell és massa baix.")
elif potencia <= -8:
    print("El nivell és acceptable.")
else:
    print("El nivell és massa alt.")

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum=float(input("Introdueix el consum de dades en GB d'una línea mòbil: "))
if consum<20:
    print(f"Consum dins del límit {consum}/20GB")
else:
    consumadicional=consum-20
    print(f"Consum fora del límit {consum}/20GB, consum adicional de {consumadicional}")

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
indicadorlos=input("L'indicador LOS del terminal òptic esta encès?(s/n):").strip.lower
indicadorinternet=input("L'indicador d'Internet del router esta encès?(s/n").strip.lower

if indicadorlos=="s":
    print("Cal revisar el cable de fibra")
elif indicadorinternet!="s":
    print("Cal comprovar el servei del proveïdor")
else:
    print("La connexió funciona correctament")


# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

percentatgebateria=int(input="Introdueix el percentatge de bateria disponible al SAI:")

if percentatgebateria<20:
    print("El nivell de bateria és crític")
elif 0<percentatgebateria or percentatgebateria>100:
    print("El nivell de bateria esta fora del rang")
elif percentatgebateria<50 :
    print("El nivell de bateria és baix")
else:
    print("El nivell de bateria es suficient")

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
latencia=float(input=("Introdueix la latencia de la connexió(ms)="))
percentatgepaquets=float(input=("Introdueix el porcentatge de paquets perduts="))

if latencia<0:
    print("La latencia és negativa")
elif 0>percentatgepaquets or percentatgepaquets>100:
    print("La latencia o el porcentatge esta fora de rang")
elif latencia<=30 and percentatgebateria<=1:
    print("La connexió es excel·lent")
elif latencia<=80 and percentatgebateria<=3:
    print("La connexió es bona")
elif latencia<=150 and percentatgebateria<=5:
    print("La connexió es acceptable")
else:
    print("La connexió és deficient")


# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
pla=input("Introdueix el teu tipus de pla (basic/plus): ").strip().lower()
consum=int(input=("Introdueix el teu consum mensual (GB): "))

if consum<0:
    print("El consum no pot ser negatiu")
elif pla=="basic":
    preu=10
    if consum>10:
        preu+=(consum-10)*1,5
    print(f"El cost total es de {preu}€ ")

elif pla=="plus":
    preu=20
    if consum>30:
        preu+=(consum-10)*0,75
    print(f"El cost total es de {preu}€ ")
else:
    print("Pla desconegut")

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
activitat=input("El compte està actiu? (s/n):").strip().lower()
contraseña=input("La contraseña és correcta? (s/n):").strip().lower()

if activitat=="s" and contraseña=="s":
    codiverificacio=int(input("Introdueix el codi de verificació: "))
elif activitat=="n" or contraseña=="n":
    print("Accés denegat")
else:
    verificacio=input("El codi de verificació es correcte? (s/n)").strip().lower()
    if verificacio=="s":
        print("Accés permés")
    else:
        print("Accés denegat")

# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
router=input("El router esta encès?(s/n): ").strip().lower()
los=input("L'indicador LOS del terminal òptic està encès? (s/n)").strip().lower()
internet=input("L'indicador d'Internet del router està encès? (s/n)").strip().lower()

if router=="n":
    print("Cal encendre el router")
else:
    if los=="s":
        print("Cal revisar el cable de fibra")
    elif internet=="n":
        print("Cal contactar amb el proveïdor")
    else:
        print("La conexió funciona correctament")

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
print("\nExercici 14:")
servei_critic = input("La incidència afecta un servei crític? (s/n): ").strip().lower()
usuaris = int(input("Quants usuaris estan afectats? "))

if usuaris < 0:
    print("El nombre d'usuaris no pot ser negatiu.")
else:
    alternativa = input("Hi ha una alternativa de connexió? (s/n): ").strip().lower()

    if (servei_critic == "s" and alternativa != "s") or (usuaris >= 50 and alternativa != "s"):
        print("Prioritat crítica.")
    elif usuaris >= 10 or servei_critic == "s":
        print("Prioritat alta.")
    else:
        print("Prioritat baixa.")

