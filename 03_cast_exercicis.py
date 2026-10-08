###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquets=int(input("Introdueix el nombre de paquets que ha rebut l'encaminador: "))
paquets+=1200
print(f"El nombre de paquets es {paquets}")

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat=float(input("Introdueix una velocitat en Mbps:"))
velocitatequivalent=velocitat/8
print(f"La velocitat equivalent: {velocitatequivalent} MB/s")