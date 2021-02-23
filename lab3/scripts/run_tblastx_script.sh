#!/bin/bash
# do not run now!

# Template from instructions 
#gzip -dc path_to_the_assembly/assembly.fna.gz | tblastx -query - -db #path_to_the_protein_set/protein_set.fasta -outfmt 6 -out outfile_name.blast

gzip -dc assembly_set_folder/GCF_000149515.1_ASM14951v1_genomic.fna.gz | tblastx -query - -db protein_set/protein_set/C_elegans_NC_001328.1_mt_codingsequences.fna -outfmt 6 -out tblastx_blast_outfile_for_C_elegans.blast