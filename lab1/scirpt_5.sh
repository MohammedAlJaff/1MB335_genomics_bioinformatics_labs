#!/bin/bash

#SGDPDai1.dedup.realn.3mask_recal.chr2.135787850-135887184.bam


echo ".............................."
echo ".......Head positions---------" 
samtools view  /proj/g2021007/private/DATA/BAM/SGDPDai1.dedup.realn.3mask_recal.chr2.135787850-135887184.sam | cut -f1,10 >> all_seqs_with_names.txt
