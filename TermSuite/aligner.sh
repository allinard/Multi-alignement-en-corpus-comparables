#!/bin/bash

#VARIABLES
JAVA_HOME=/home/dpt/E104799M/Documents/jdk1.7.0_80/bin/java
TS_JAR=/home/dpt/E104799M/Documents/LINAtermSuite/termSuite/trunk/ttc-term-suite/build/libs/ttc-term-suite-1.6-beta.jar
TT_HOME=/home/dpt/E104799M/Documents/treeTagger
CORPUS=$1
SWTMWT=$2


#Aligner EN-FR
$JAVA_HOME -Djava.awt.headless=true -Xms1g -Xmx2g -cp $TS_JAR eu.project.ttc.tools.cli.TermSuiteAlignerCLI \
--AlignerOutputDirectory /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/ResAligner$SWTMWT/NoPivotDict \
--DictionaryFile /home/dpt/E104799M/Documents/experimentationsTermSuite/Dico/EN-FR.txt \
--Directory /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/TradsRefs/EN-FR/$SWTMWT \
--SimilarityDistanceClassName eu.project.ttc.metrics.Cosine \
--SourceLanguage en \
--SourceTerminologyFile /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/English/en-terminology.xmi \
--TargetLanguage fr \
--TargetTerminologyFile /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/French/fr-terminology.xmi \
--MaxTranslationCandidates 20 \
--DistributionalMethod

#Aligner FR-EN
$JAVA_HOME -Djava.awt.headless=true -Xms1g -Xmx2g -cp $TS_JAR eu.project.ttc.tools.cli.TermSuiteAlignerCLI \
--AlignerOutputDirectory /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/ResAligner$SWTMWT/NoPivotDict \
--DictionaryFile /home/dpt/E104799M/Documents/experimentationsTermSuite/Dico/FR-EN.txt \
--Directory /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/TradsRefs/FR-EN/$SWTMWT \
--SimilarityDistanceClassName eu.project.ttc.metrics.Cosine \
--SourceLanguage fr \
--SourceTerminologyFile /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/French/fr-terminology.xmi \
--TargetLanguage en \
--TargetTerminologyFile /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/English/en-terminology.xmi \
--MaxTranslationCandidates 20 \
--DistributionalMethod

#EVAL PY
python evalAligner.py -eval /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/TradsRefs/EN-FR/$SWTMWT/ -align /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/ResAligner$SWTMWT/NoPivotDict/en-fr-alignment.tsv > /home/dpt/E104799M/Documents/resultatsTS/en-fr-$CORPUS-$SWTMWT.txt
echo $CORPUS $SWTMWT 'en-fr NO PIVOT DICT'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/en-fr-$CORPUS-$SWTMWT.txt

python evalAligner.py -eval /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/TradsRefs/FR-EN/$SWTMWT/ -align /home/dpt/E104799M/Documents/experimentationsTermSuite/$CORPUS/ResAligner$SWTMWT/NoPivotDict/fr-en-alignment.tsv > /home/dpt/E104799M/Documents/resultatsTS/fr-en-$CORPUS-$SWTMWT.txt
echo $CORPUS $SWTMWT 'fr-en NO PIVOT DICT'
tail -n 9 /home/dpt/E104799M/Documents/resultatsTS/fr-en-$CORPUS-$SWTMWT.txt


exit 0
