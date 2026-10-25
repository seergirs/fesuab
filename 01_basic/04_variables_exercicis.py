###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador= "router4304243"
ubicacio_encaminador="Barcelona"
nombre_ports=67
ences= True

print(f"Encaminador: {nom_encaminador} Ubicació: {ubicacio_encaminador} Ports:{nombre_ports} Ences: {ences}" )



# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gbpla=30
gbconsumits=12
gbrestants=gbpla-gbconsumits
print(f"Et queden {gbrestants}GB, {gbconsumits}/{gbpla}GB")
gbconsumits=17
gbrestants=gbpla-gbconsumits
print(f"Et queden {gbrestants}GB, {gbconsumits}/{gbpla}GB")
