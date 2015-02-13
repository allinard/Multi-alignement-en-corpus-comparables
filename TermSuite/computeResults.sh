#!/bin/bash

#STANDARD
#SingleWordTerms
./aligner.sh CorpusWindEnergy SWT
./aligner.sh CorpusMobileTechnology SWT

#MultiWordTerms
#./aligner.sh CorpusWindEnergy MWT
#./aligner.sh CorpusMobileTechnology MWT




#PIVOT DICT
#SingleWordTerms
./alignerPivotDict.sh CorpusWindEnergy SWT
./alignerPivotDict.sh CorpusMobileTechnology SWT

exit 0
