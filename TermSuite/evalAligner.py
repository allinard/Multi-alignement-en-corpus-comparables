import sys
import argparse
import os



def printResults(results):
	for wordSRC in results:
		listTrads = results[wordSRC]
		for trad in listTrads:
			for wordTARGET in trad:
				print(wordSRC+" "+wordTARGET+" "+trad[wordTARGET])



#-eval EVALDIR -align ALIGNMENT
parser = argparse.ArgumentParser()
parser.add_argument("-eval", "--evalDirectory", dest = "eval", help="Evaluation Directory path containing all terms to evaluate")
parser.add_argument("-align", "--alignement", dest = "align", help="Alignment tsv file")
args = parser.parse_args()


#Parse eval dir
nbTotalMots = 0
dictionary = {}
for file in os.listdir(args.eval):
    if file.endswith(".txt"):
        fileEval = open(args.eval+file, 'r')
	for line in fileEval:
		elementsLine = line.split('\t')
		dictionary[elementsLine[0].replace("\n","").rstrip()] = elementsLine[1].replace("\n","").rstrip()
		nbTotalMots += 1
	fileEval.close()




#Parse alignment
results = {}
fileAlignment = open(args.align, 'r')
for line in fileAlignment:
	elementsLine = line.split('\t')
	keySRC = elementsLine[0]
	wordSRC = elementsLine[1]
	rank = elementsLine[2]
	wordTARGET =elementsLine[3].replace("\n","")
	try:
		tradRank = {}
		tradRank[wordTARGET] = rank
		results[wordSRC].append(tradRank)
	except Exception:	
		results[wordSRC]=[]
		tradRank = {}
		tradRank[wordTARGET] = rank
		results[wordSRC].append(tradRank)
fileAlignment.close()




top1 = 0
top2 = 0
top3 = 0
top5 = 0
top10 = 0
top20 = 0

print(args.align)

#Find correct translations
for word in dictionary:
	translation = dictionary[word]
	try:
		foundTranslationsList = results[word]
		for indice in range(0,len(foundTranslationsList)):
			try:
				foundTranslations = foundTranslationsList[indice]
				if int(foundTranslations[translation]) < 2:
					top1 += 1
					top2 += 1
					top3 += 1
					top5 += 1
					top10 += 1
					top20 += 1
					print(word+" > "+translation+" (rank "+foundTranslations[translation]+")")
					break
				elif int(foundTranslations[translation]) < 3:
					top2 += 1
					top3 += 1
					top5 += 1
					top10 += 1
					top20 += 1
					print(word+" > "+translation+" (rank "+foundTranslations[translation]+")")
					break
				elif int(foundTranslations[translation]) < 4:
					top3 += 1
					top5 += 1
					top10 += 1
					top20 += 1
					print(word+" > "+translation+" (rank "+foundTranslations[translation]+")")
					break
				elif int(foundTranslations[translation]) < 6:
					top5 += 1
					top10 += 1
					top20 += 1
					print(word+" > "+translation+" (rank "+foundTranslations[translation]+")")
					break
				elif int(foundTranslations[translation]) < 11:
					top10 += 1
					top20 += 1
					print(word+" > "+translation+" (rank "+foundTranslations[translation]+")")
					break
				elif int(foundTranslations[translation]) < 21:
					top20 += 1
					print(word+" > "+translation+" (rank "+foundTranslations[translation]+")")
					break
				
			except Exception:
				pass
	except KeyError:
		print(word+" not found")


print("TOP1 : "+str(top1))
print("TOP2 : "+str(top2))
print("TOP3 : "+str(top3))
print("TOP5 : "+str(top5))
print("TOP10 : "+str(top10))
print("TOP20 : "+str(top20))
print("Total mots : "+str(nbTotalMots))
print("\n")

