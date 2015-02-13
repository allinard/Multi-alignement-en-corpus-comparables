#!/bin/bash

#display all results
SWTMWT=SWT

CORPUS=CorpusWindEnergy

echo $CORPUS $SWTMWT 'en-fr NO PIVOT DICT'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/en-fr-$CORPUS-$SWTMWT.txt

echo $CORPUS $SWTMWT 'en-fr PIVOT DICT ES'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/en-es-fr-$CORPUS-$SWTMWT.txt

echo $CORPUS $SWTMWT 'en-fr PIVOT DICT DE'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/en-de-fr-$CORPUS-$SWTMWT.txt

echo $CORPUS $SWTMWT 'fr-en NO PIVOT DICT'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/fr-en-$CORPUS-$SWTMWT.txt

echo $CORPUS $SWTMWT 'fr-en PIVOT DICT ES'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/fr-es-en-$CORPUS-$SWTMWT.txt

echo $CORPUS $SWTMWT 'fr-en PIVOT DICT DE'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/fr-de-en-$CORPUS-$SWTMWT.txt




CORPUS=CorpusMobileTechnology

echo $CORPUS $SWTMWT 'en-fr NO PIVOT DICT'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/en-fr-$CORPUS-$SWTMWT.txt

echo $CORPUS $SWTMWT 'en-fr PIVOT DICT ES'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/en-es-fr-$CORPUS-$SWTMWT.txt

echo $CORPUS $SWTMWT 'en-fr PIVOT DICT DE'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/en-de-fr-$CORPUS-$SWTMWT.txt

echo $CORPUS $SWTMWT 'fr-en NO PIVOT DICT'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/fr-en-$CORPUS-$SWTMWT.txt

echo $CORPUS $SWTMWT 'fr-en PIVOT DICT ES'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/fr-es-en-$CORPUS-$SWTMWT.txt

echo $CORPUS $SWTMWT 'fr-en PIVOT DICT DE'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/fr-de-en-$CORPUS-$SWTMWT.txt





exit 0
