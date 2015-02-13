import sys, os


#Load existing dicts
FR_EN = {}
FR_ES = {}
FR_DE = {}
EN_FR = {}
ES_FR = {}
DE_FR = {}
for file in os.listdir(os.getcwd()+'/TradsRefs/FR-EN/'):
    if file.endswith(".txt"):
        fileEval = open(os.getcwd()+'/TradsRefs/FR-EN/'+file, 'r')
	for line in fileEval:
		elementsLine = line.split('\t')
		FR_EN[elementsLine[0].replace("\n","").rstrip()] = elementsLine[1].replace("\n","").rstrip()
	fileEval.close()
for file in os.listdir(os.getcwd()+'/TradsRefs/FR-ES/'):
    if file.endswith(".txt"):
        fileEval = open(os.getcwd()+'/TradsRefs/FR-ES/'+file, 'r')
	for line in fileEval:
		elementsLine = line.split('\t')
		FR_ES[elementsLine[0].replace("\n","").rstrip()] = elementsLine[1].replace("\n","").rstrip()
	fileEval.close()
for file in os.listdir(os.getcwd()+'/TradsRefs/FR-DE/'):
    if file.endswith(".txt"):
        fileEval = open(os.getcwd()+'/TradsRefs/FR-DE/'+file, 'r')
	for line in fileEval:
		elementsLine = line.split('\t')
		FR_DE[elementsLine[0].replace("\n","").rstrip()] = elementsLine[1].replace("\n","").rstrip()
	fileEval.close()
for file in os.listdir(os.getcwd()+'/TradsRefs/EN-FR/'):
    if file.endswith(".txt"):
        fileEval = open(os.getcwd()+'/TradsRefs/EN-FR/'+file, 'r')
	for line in fileEval:
		elementsLine = line.split('\t')
		EN_FR[elementsLine[0].replace("\n","").rstrip()] = elementsLine[1].replace("\n","").rstrip()
	fileEval.close()
for file in os.listdir(os.getcwd()+'/TradsRefs/DE-FR/'):
    if file.endswith(".txt"):
        fileEval = open(os.getcwd()+'/TradsRefs/DE-FR/'+file, 'r')
	for line in fileEval:
		elementsLine = line.split('\t')
		DE_FR[elementsLine[0].replace("\n","").rstrip()] = elementsLine[1].replace("\n","").rstrip()
	fileEval.close()
for file in os.listdir(os.getcwd()+'/TradsRefs/ES-FR/'):
    if file.endswith(".txt"):
        fileEval = open(os.getcwd()+'/TradsRefs/ES-FR/'+file, 'r')
	for line in fileEval:
		elementsLine = line.split('\t')
		try:
			ES_FR[elementsLine[0].replace("\n","").rstrip()] = elementsLine[1].replace("\n","").rstrip()
		except IndexError:
			pass
	fileEval.close()





#EN-ES
print("           EN - ES ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-EN.csv', 'r')
count = 0
for line in f:
	elementsLine = line.split('\t')
	ref = elementsLine[0].rstrip()
	if ref:
		try:	
			pivot=EN_FR[ref]
			trad=FR_ES[pivot]
			print('Translation ES for "'+ref+'" is '+trad)
			count += 1
			g = open('TradsRefs/EN-ES/'+str(count)+'.txt','w')
			g.write(ref+'\t'+trad)
			g.close()
		except KeyError:		
			print('Translation ES for "'+ref+'": ')
			user_input = sys.stdin.readline()
			if "NONE" not in user_input:
				count += 1
				g = open('TradsRefs/EN-ES/'+str(count)+'.txt','w')
				g.write(ref+'\t'+user_input)
				g.close()
f.close()



#EN-DE
print("           EN - DE ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-EN.csv', 'r')
count = 0
for line in f:
	elementsLine = line.split('\t')
	ref = elementsLine[0].rstrip()
	if ref:
		try:	
			pivot=EN_FR[ref]
			trad=FR_DE[pivot]
			print('Translation DE for "'+ref+'" is '+trad)
			count += 1
			g = open('TradsRefs/EN-DE/'+str(count)+'.txt','w')
			g.write(ref+'\t'+trad)
			g.close()
		except KeyError:		
			print('Translation DE for "'+ref+'": ')
			user_input = sys.stdin.readline()
			if "NONE" not in user_input:
				count += 1
				g = open('TradsRefs/EN-DE/'+str(count)+'.txt','w')
				g.write(ref+'\t'+user_input)
				g.close()
f.close()







#ES-EN
print("           ES - EN ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-ES.csv', 'r')
count = 0
for line in f:
	elementsLine = line.split('\t')
	ref = elementsLine[0].rstrip()
	if ref:
		try:	
			pivot=ES_FR[ref]
			trad=FR_EN[pivot]
			print('Translation EN for "'+ref+'" is '+trad)
			count += 1
			g = open('TradsRefs/ES-EN/'+str(count)+'.txt','w')
			g.write(ref+'\t'+trad)
			g.close()
		except KeyError:		
			print('Translation EN for "'+ref+'": ')
			user_input = sys.stdin.readline()
			if "NONE" not in user_input:
				count += 1
				g = open('TradsRefs/ES-EN/'+str(count)+'.txt','w')
				g.write(ref+'\t'+user_input)
				g.close()
f.close()






#ES-DE
print("           ES - DE ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-ES.csv', 'r')
count = 0
for line in f:
	elementsLine = line.split('\t')
	ref = elementsLine[0].rstrip()
	if ref:
		try:	
			pivot=ES_FR[ref]
			trad=FR_DE[pivot]
			print('Translation DE for "'+ref+'" is '+trad)
			count += 1
			g = open('TradsRefs/ES-DE/'+str(count)+'.txt','w')
			g.write(ref+'\t'+trad)
			g.close()
		except KeyError:		
			print('Translation DE for "'+ref+'": ')
			user_input = sys.stdin.readline()
			if "NONE" not in user_input:
				count += 1
				g = open('TradsRefs/ES-DE/'+str(count)+'.txt','w')
				g.write(ref+'\t'+user_input)
				g.close()
f.close()








#DE-EN
print("           DE - EN ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-DE.csv', 'r')
count = 0
for line in f:
	elementsLine = line.split('\t')
	ref = elementsLine[0].rstrip()
	if ref:
		try:	
			pivot=DE_FR[ref]
			trad=FR_EN[pivot]
			print('Translation EN for "'+ref+'" is '+trad)
			count += 1
			g = open('TradsRefs/DE-EN/'+str(count)+'.txt','w')
			g.write(ref+'\t'+trad)
			g.close()
		except KeyError:		
			print('Translation EN for "'+ref+'": ')
			user_input = sys.stdin.readline()
			if "NONE" not in user_input:
				count += 1
				g = open('TradsRefs/DE-EN/'+str(count)+'.txt','w')
				g.write(ref+'\t'+user_input)
				g.close()
f.close()






#DE-ES
print("           DE - ES ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-DE.csv', 'r')
count = 0
for line in f:
	elementsLine = line.split('\t')
	ref = elementsLine[0].rstrip()
	if ref:
		try:	
			pivot=DE_FR[ref]
			trad=FR_ES[pivot]
			print('Translation ES for "'+ref+'" is '+trad)
			count += 1
			g = open('TradsRefs/DE-ES/'+str(count)+'.txt','w')
			g.write(ref+'\t'+trad)
			g.close()
		except KeyError:		
			print('Translation ES for "'+ref+'": ')
			user_input = sys.stdin.readline()
			if "NONE" not in user_input:
				count += 1
				g = open('TradsRefs/DE-ES/'+str(count)+'.txt','w')
				g.write(ref+'\t'+user_input)
				g.close()
f.close()








