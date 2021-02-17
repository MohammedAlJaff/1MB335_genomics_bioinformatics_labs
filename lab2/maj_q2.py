## Author: Mohammed Al-Jaff
## Cuourse: Genomics & Bioinformatics 
## Lab-2 - task 3.


# Goal of this task 
'''
A program that takes a nucleotide fasta file as input and returns a new reverse complemented fasta file as output. It should be able to handle fasta files with more than one entry.

HOW TO RUN THIS SCRIPT: 

>> python3 maj_q2.py your_fasta_file.txt

This program will craeate and store a fasta file named wimillar to the inputed file but with the text '_reversed' attached at the end. 
'''

# Relevant modules
import sys

# Functions created for this task.....


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



def reverse_compliment_of_sequence(seq_string):
    '''
    Converts a nucleotide sequence in string form to its reverse compliment.

    input: sequnce (string)
    output: reverse compliment (string)
    '''
    # Creating a nucleotide translation map
    # To get back the complement of the base / nt you plug in.. 
    complement_map = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}

    # reverse string step
    reverse_seq = seq_string[::-1]

    # complement step 
    dummy_s = ''
    for nt in reverse_seq:
        dummy_s = dummy_s + complement_map[nt]

    reverse_complement_string = dummy_s
    return reverse_complement_string


## Workflow / script - The logic that runs when calling the script.
if __name__ == '__main__':
    print("\n\nNEW_RUN\n................")

    file_name = sys.argv[1] # get name of inputed file from input arguments list.

    # Open file and load/read whole damn file and store in a single string for now.
    with open(file_name, "r") as fasta_file:
        whole_raw_fasta_file_as_string = fasta_file.read()

    # The idea hear is to avoid going through the fasta file line by line, 
    # but instead realsie that we can split the whole content by the '>'
    # charecter to get each header+sequence-lines after the split.  Each one of these "chunks" is stores as a string element in the dummy variable x below. 

    # split on  '>' charcter
    x  = whole_raw_fasta_file_as_string.split(sep='>')
    x = x[1:] # removing first element becasue split assigns it as an empty string. 

    if len(x) == 0: # Incase we get inputed a bad fasta-file.
        print('ERROR: NO SEQUENCES FOUND IN FILE...')
        sys.exit()
    else: 
        # Each element of x will be a long string "paragraf" corresponing 
        # to a pair of (header_i, seq_of_header_i). 
        # We'lll now process each element transform them to dictionary object
        # and store this in a list of sequence objects.....

        all_seq_objects = []

        for elementi_i in x: 
            seq_obj_i = raw_seq_string_to_seq_object(elementi_i)
            all_seq_objects.append(seq_obj_i)

        ## Going through each object one by one and writing the header with its reversed complimented sequence to new file 

        # create new file name from orginal inputed file...
        file_name_split = file_name.split(sep='.')
        write_file_name = file_name_split[0] + "_reversed." + file_name_split[1]
        
        with open(write_file_name, "w") as new_fasta_file:
            
            for seq_obj_i in all_seq_objects:

                # Modify original header by adding 'reversed' at the end and and writing to file 
                new_header = ">" + seq_obj_i['header'] + " Reversed" + "\n"
                new_fasta_file.write(new_header)

                # reverse complimenting original string and writing to new file
                reversed_sequence_i = reverse_compliment_of_sequence(seq_obj_i['sequence']) + "\n"
                new_fasta_file.write(reversed_sequence_i)
