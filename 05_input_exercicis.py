###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
tecnic= input("Introdueix el nom del técnic: ")
xarxa = input("Introdueix el nom de la xarxa: ")
print(tecnic, "està instal·lant la xarxa" , xarxa)

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres _solucions.pyi la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitudfibra=float(input("Introdueix la longitud de la fibra en km:  "))

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores=float(input("Introdueix el nombre d'hores de feina:  "))
preuhora=float(input("Introdueix el preu per hora:  "))
preumaterial=float(input("Introdueix el preu del material:  "))

costtotal= (hores*preuhora)+preumaterial
print("El cost total de la instal·lació és: ", costtotal, "€")
