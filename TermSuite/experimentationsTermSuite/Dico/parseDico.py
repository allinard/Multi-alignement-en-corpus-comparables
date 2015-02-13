import sys


print("Processing FR-DE")
f = open('FR-DE/dicfrdeelda-utf8.txt', 'r')
g = open('FR-DE.txt','w')
h = open('DE-FR.txt','w')
for line in f:
	elementsLine = line.split(';')
	motFR = elementsLine[0]
	trad = elementsLine[3]
	g.write(motFR+'\t'+trad+'\n')
	h.write(trad+'\t'+motFR+'\n')
f.close()
g.close()
h.close()







print("Processing FR-ES")
f = open('FR-ES/dicfrspelda-utf8.txt', 'r')
g = open('FR-ES.txt','w')
h = open('ES-FR.txt','w')
for line in f:
	elementsLine = line.split(';')
	motFR = elementsLine[0]
	trad = elementsLine[3]
	g.write(motFR+'\t'+trad+'\n')
	h.write(trad+'\t'+motFR+'\n')
f.close()
g.close()
h.close()








print("Processing FR-EN")
f = open('FR-EN/dicfrenelda-utf8.txt', 'r')
g = open('FR-EN.txt','w')
h = open('EN-FR.txt','w')
for line in f:
	elementsLine = line.split(';')
	motFR = elementsLine[0]
	trad = elementsLine[3]
	g.write(motFR+'\t'+trad+'\n')
	h.write(trad+'\t'+motFR+'\n')
f.close()
g.close()
h.close()
