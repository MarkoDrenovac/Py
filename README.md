# Zadatak 1

sloziti python skriptu koja u standard output (shell) outputa (prvi dio skripte):
 
•	usage memorija (RAM + SWAP) – prikazati vrijednosti I postotak usage-a
•	load sustava – 1min, 5min, 15min
•	prikazati podatke o procesoru: tip procesora, brzina I broj core-a
•	prikazati usage iNodeova za / particiju (vrijednosti – current I max + postotak usagea)
•	prikazati sve trenutne otvorene portove na hostu
•	prikazati sve established konekcije na tom hostu


#Zadatak 2

sloziti python kod koji ce sve gore navedene stavke (drugi dio skripte) izloziti kroz WEB servis

Requirement: sav output bi trebao biti u JSON formatu 
 
 
Sample:
ako u browser upisem: http://ip_adresa_servera:port/procesor
 
browser prikaze (primjer u clear textu, a ne u JSON-u):
cpu core: 4
tip procesora: Intel xeon
speed: 2.5GHz
