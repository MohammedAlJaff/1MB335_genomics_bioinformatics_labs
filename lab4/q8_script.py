# Genomics & Bioinformatics 
# Lab 4: Python script. 
# Author: Mohammed Al-Jaff 


'''
A python script that out puts a fasta file with a suer specified header tag containing the user-specified name, and interval of an inputed interval. 
'''


## Modules 
import sys

## Functons 



def extract_sequence_from_file(file_name, start_pos, stop_pos): 
    '''
    High level function that extracts and returns a region of intereest from a given fasta sequence from a user inpputed fasta file and the start and stop endpoint positions of the sequence

    Assumes that sqeuence is already sequentialized, ie in in one line. Can be modified as in lab 2 to account for un-sequentialized fasta files. 

    Input: Filename (string), start_pos (int), stop_pos(int)
    Return: subsequence (string)
    '''
    
    with open(file_name, 'r') as f: 
        whole_damn_thing = f.read()

    dummy = whole_damn_thing.split(sep='\n')

    header = dummy[0]
    seq = dummy[1]

    subseq = seq[start_pos-1:stop_pos]
    return subseq




def construct_valid_header_string(feature_id, start_pos, stop_pos, extra_annotation_info=''):
    '''
    A Function thats constructs and returns a valid fasta header. 
    Input: Header specific input: feature_id, start and stop pos (integers) and optional extra feature annotation info

    returns: header (string)
    '''
    header = '>' + feature_id + ':' + str(start_pos) + '-' + str(stop_pos) + ' ' + extra_annotation_info
    return header


# input_mitocondria.fasta TGH_4 5001 5100 This is a cool gene
# Assumption is that inputted file is a whoel genome with only one seq.

if __name__=='__main__':
    'Assign input information to variables'
    read_file_name = sys.argv[1]
    feature_id = sys.argv[2]
    start_pos = int(sys.argv[3])
    stop_pos = int(sys.argv[4])

    # Output file header code
    if (len(sys.argv)>5):
        extra_annotation_info = " ".join(sys.argv[5:])
        print('possible extra shit added')
        
        header = construct_valid_header_string(feature_id, start_pos, stop_pos, extra_annotation_info)
    else:
        header = construct_valid_header_string(feature_id, start_pos, stop_pos)

    
    subseq = extract_sequence_from_file(read_file_name, start_pos, stop_pos)

    print(header)
    print(subseq)

    # write to file
    with open(feature_id+'.fasta', 'w') as f_out:
        f_out.write(header+'\n')
        f_out.write(subseq)







