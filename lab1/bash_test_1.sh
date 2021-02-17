#!/bin/bash

#SGDPDai1.dedup.realn.3mask_recal.chr2.135787850-135887184.bam


samtools view /proj/g2021007/private/DATA/BAM/SGDPDai1.dedup.realn.3mask_recal.chr2.135787850-135887184.sam | head -25

echo "..............."
echo "..............."

samtools view /proj/g2021007/private/DATA/BAM/SGDPDai1.dedup.realn.3mask_recal.chr2.135787850-135887184.sam | head -25 | cut -f1,3,5

