import sys


print("Processing EN-(FR)-ES")
LS_LP = open('EN-FR.txt','r')
LP_LC = open('FR-ES.txt','r')
LS_LC = open('EN-ES.txt','w')
reverse = open('ES-EN.txt','w')

dicoLS_LP = {}
dicoLP_LC = {}
dicoLS_LC = {}

for line in LS_LP:
	elementsLine = line.split('\t')
	motS = elementsLine[0]
	motP = elementsLine[1].replace("\n","")
	try:
		dicoLS_LP[motS].append(motP)
	except KeyError:
		dicoLS_LP[motS] = []
		dicoLS_LP[motS].append(motP)

for line in LP_LC:
	elementsLine = line.split('\t')
	motP = elementsLine[0]
	motC = elementsLine[1].replace("\n","")
	try:
		dicoLP_LC[motP].append(motC)
	except KeyError:
		dicoLP_LC[motP] = []
		dicoLP_LC[motP].append(motC)

for source in dicoLS_LP:
	for pivot in dicoLS_LP[source]:
		try:
			cible = dicoLP_LC[pivot]
			try:
				dicoLS_LC[source].append(cible)
			except KeyError:
				dicoLS_LC[source] = []
				dicoLS_LC[source].append(cible)
		except KeyError:
			pass


print(len(dicoLS_LP))
print(len(dicoLP_LC))
print(len(dicoLS_LC))


for motSOURCE in dicoLS_LC:
	listTradsCandidates = []
	for trads in dicoLS_LC[motSOURCE]:
		for trad in trads:
			listTradsCandidates.append(trad)
	listTradsCandidates = list(set(listTradsCandidates))
	for tradCIBLE in listTradsCandidates:
		LS_LC.write(motSOURCE+"\t"+tradCIBLE+"\n")
		reverse.write(tradCIBLE+"\t"+motSOURCE+"\n")

LS_LP.close()
LP_LC.close()
LS_LC.close()
reverse.close()
