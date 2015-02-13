import sys


"""
#FR-EN
print("           FR - EN ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-FR.csv', 'r')

count = 0
for line in f:
	
	elementsLine = line.split('\t')
	ref = elementsLine[0]

	if ref:
		print('Translation EN for "'+ref+'": ')
		user_input = sys.stdin.readline()

		if "NONE" not in user_input:
			count += 1
			g = open('TradsRefs/FR-EN/'+str(count)+'.txt','w')
			g.write(ref+'\t'+user_input)
			g.close()






#FR-ES
print("\n\n\n\n\n           FR - ES ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-FR.csv', 'r')

count = 0
for line in f:
	
	elementsLine = line.split('\t')
	ref = elementsLine[0]

	if ref:
		print('Translation ES for "'+ref+'": ')
		user_input = sys.stdin.readline()

		if user_input != "NONE":
			count += 1
			g = open('TradsRefs/FR-ES/'+str(count)+'.txt','w')
			g.write(ref+'\t'+user_input)
			g.close()








"""



#FR-DE
print("\n\n\n\n\n           FR - DE ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-FR.csv', 'r')

count = 0
for line in f:
	
	elementsLine = line.split('\t')
	ref = elementsLine[0]

	if ref:
		print('Translation DE for "'+ref+'": ')
		user_input = sys.stdin.readline()

		if user_input != "NONE":
			count += 1
			g = open('TradsRefs/FR-DE/'+str(count)+'.txt','w')
			g.write(ref+'\t'+user_input)
			g.close()








#EN-FR
print("           EN - FR ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-EN.csv', 'r')

count = 0
for line in f:
	
	elementsLine = line.split('\t')
	ref = elementsLine[0]

	if ref:
		print('Translation FR for "'+ref+'": ')
		user_input = sys.stdin.readline()

		if "NONE" not in user_input:
			count += 1
			g = open('TradsRefs/EN-FR/'+str(count)+'.txt','w')
			g.write(ref+'\t'+user_input)
			g.close()











#ES-FR
print("           ES - FR ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-ES.csv', 'r')

count = 0
for line in f:
	
	elementsLine = line.split('\t')
	ref = elementsLine[0]

	if ref:
		print('Translation FR for "'+ref+'": ')
		user_input = sys.stdin.readline()

		if "NONE" not in user_input:
			count += 1
			g = open('TradsRefs/ES-FR/'+str(count)+'.txt','w')
			g.write(ref+'\t'+user_input)
			g.close()










#DE-FR
print("           DE - FR ")
f = open('TTC-RTL-windenergy-lemmatisation-tt-DE.csv', 'r')

count = 0
for line in f:
	
	elementsLine = line.split('\t')
	ref = elementsLine[0]

	if ref:
		print('Translation FR for "'+ref+'": ')
		user_input = sys.stdin.readline()

		if "NONE" not in user_input:
			count += 1
			g = open('TradsRefs/DE-FR/'+str(count)+'.txt','w')
			g.write(ref+'\t'+user_input)
			g.close()




