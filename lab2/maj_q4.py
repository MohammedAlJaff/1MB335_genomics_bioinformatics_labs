## Author: Mohammed Al-Jaff
## Cuourse: Genomics & Bioinformatics 
## Lab-2.


# Goal of this task 
'''
A script/program that reads a fasta-file and outputs: 
    1. The number of total sequences in the file.
    2. The names of all genes/features in the file.
    3. The name of each gene followed by its length.

HOW TO RUN THIS SCRIPT: 

>> python3 maj_q4.py your_fasta_file.txt
'''

# Relevant modules in use
import sys
import re

# FUNCTIONS created for task ###############################
def raw_seq_string_to_seq_object(raw_seq_string):
    '''
    Converts a chunch of string extracted from the raw fasta file corresponding to a header and all the lines of its sequence.

    intput: a "chunk" for lack of better word

    output: a so called 'sequence object' which basically is a dictionary with you elements a header and the whole sequence as a single long strings w/o a nextline charecter.
    '''

    # split string on \n charecter. 
    dummy_x = raw_seq_string.split(sep="\n")
    header = dummy_x[0]
    #print(f"header: {header}")

    the_rest = dummy_x[1:len(dummy_x)]
    #print(f"the  rest:\n {the_rest}")

    # Concatinate all the sequences into a single string....
    sequence_string = ""
    for element in the_rest:
        sequence_string = sequence_string + element

    seq_obj = {'header':header, 'sequence':sequence_string}
    return seq_obj


def extract_gene_from_header(seq_obj):
    '''
    Extracts and returns the name of the gene in the header from an inputed 'sequence object'

    input: sequence object
    output: gene name as a string
    '''

    header = seq_obj['header'] # extract string from object
    pattern = re.compile(r"gene=[a-zA-Z1-9]+") # define regex pattern for gene name
    pattern_instance = pattern.findall(header) # search for pattern in header.
    gene_name_raw = pattern_instance[0] #first occurance of pattern ('gene')
    gene_name = gene_name_raw[5:] # remove the 'gene=' part of the match
    return gene_name

## Workflow / script 
if __name__ == '__main__':

    print("\n\nNEW_RUN\n................")
    fasta_file_name = sys.argv[1] #2nd element in args! FIrst arg is the script itself
    
    # Open inputed fastafile and basically read whole damn thing at once. 
    with open(fasta_file_name, "r") as fasta_file:
        whole_raw_fasta_file_as_string = fasta_file.read()


    # The idea hear is to avoid going through the fasta file line by line, 
    # but instead realsie that we can split the whole content by the '>'
    # charecter to get each header+sequence-lines after the split.  

    # split on  '>' charcter
    x  = whole_raw_fasta_file_as_string.split(sep='>')
    x = x[1:] # removing first element becasue split assigns it as an empty string. 

    if len(x) == 0: # Incase we get inputed a bad fasta-file.
        print('ERROR: NO SEQUENCES FOUND IN FILE...')
        sys.exit()
    else: 

        # Each element of X will be a long string "paragraf" corresponing 
        # to a pair of (header_i, seq_of_header_i). 
        # We'lll now process each element transform them to dictionary object with 
        # the function make_into_equence_object [see begining of file for function internal algo]

        all_seq_objects = [] # list to store all formed sequence objects extracted from raw fasta file. 
        for elementi_i in x: 
            seq_obj_i = raw_seq_string_to_seq_object(elementi_i)
            all_seq_objects.append(seq_obj_i)

        # Printing Total number of sequences
        print('---------------------------------------------')
        print(f"Total number of genes in file: {len(all_seq_objects)}")
        print('---------------------------------------------')
        
        # Printing  names of all genes/features in the file
        print('---------------------------------------------')
        print('All gene/feature names found  with sequence length (nt):\n')
        for i, seq_obj_i in enumerate(all_seq_objects):
            print(i+1, '\t-\t', extract_gene_from_header(seq_obj_i), '\t-\t', len(seq_obj_i['sequence']), 'nt')
            print('---------------------------------------------')
            