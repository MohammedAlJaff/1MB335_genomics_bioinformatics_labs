# Author: Mohammed Al-Jaff
# Genomics & Biofinormatics: 
# Lab 6

'''
Use pattern: 
>> python3 header_converter.py [your_fasta_seqs.fasta] [your_header_conversion_table.tsv] [1, 2 or 3 depending on what header type]

header type: 
    1: Shortest (max 8 charecter) id
    2: Human readable id
    3. Original ncbi sequence header

Use example

>> python3 header_converter.py all_cytb_seqs.fasta cytb_header_conversion_table.tsv 2

input: 
    1) A merged fasta file
    2) integer 1 2 or 3 representing which header style you want. 
'''


# modules 
import sys
import csv
import os
import time

def is_fasta_header(s):
    '''
    Checks if given line is a fasta headers
    '''
    if s[0] == '>':
        return True
    return False


def determine_current_header_type(current_header_string, header_type_lists):
    '''
    Determine curtent header type: I ether 1, 2 or 3
    Assuming  that the header type of the first encountered header 
    in the fasta file is representiative of all other headers in file 
    '''
    # Strip away '>' char and \n to get 'pure' header only.
    current_header_string = current_header_string[1:].strip()
    print(f"current header: {current_header_string}")
    t = 0

    # Check in which header type list current header belongs to. 
    for list in header_type_lists:
        
        if current_header_string in list:
            #print(f"Current header is type: {t+1}")
            return t+1
        else: 
            #print(f"Current header NOT type: {t+1}")
            t=t+1
    return -13


def construct_header_type_names_lists(csv_file_name):
    '''
    Techinical: Internal function used to check chich header type the given seq file has 
    and used to switch headers types. 
    '''
    type_1_names = []
    type_2_names = []
    type_3_names = []
    
    with open(csv_file_name, mode='r') as f:
        table = csv.reader(f, delimiter='\t')
        for row in table:
            type_1_names.append(row[1])
            type_2_names.append(row[2])
            type_3_names.append(row[3])

    type_1_names = type_1_names[1:]
    type_2_names = type_2_names[1:]
    type_3_names = type_3_names[1:]
    
    header_type_lists = [type_1_names, type_2_names, type_3_names]

    return header_type_lists


def get_new_header(current_header, current_header_type, desired_header_type, header_type_lists):
    '''
    Returms back desred header based on content and id of current header
    '''

    current_header = current_header[1:].strip()
    
    name_indx =header_type_lists[current_header_type-1].index(current_header) 

    new_header = header_type_lists[desired_header_type-1][name_indx]
    new_header = '>'+new_header+'\n'
    return new_header


#
if __name__=="__main__":

    # Sysarg stuff 
    fasta_file_name = sys.argv[1]
    converstion_table_file_name = sys.argv[2] 
    desired_header_type = int(sys.argv[3])

    # User specified header typ check:
    # to ensure valid conversion
    if desired_header_type not in [1,2,3]:
        print('oj!')
    else: print('header type checks out')

    # List of names of header/sequences for all 3 types.
    header_type_lists = construct_header_type_names_lists(converstion_table_file_name)


    abs_dir_path = os.path.abspath(os.path.dirname(fasta_file_name))
    base_file_name = os.path.basename(fasta_file_name)


    with open(fasta_file_name, mode='r') as f:

        temp_out_file_name = abs_dir_path + '/temp_output.fasta' # Write to temp file first.
        with open(temp_out_file_name, mode='w') as g:
            
            line=f.readline() 

            # Determine curtent header type: I ether 1, 2 or 3
            # Assuming  that the header type of the first encountered header 
            # in the fasta file is representiative of all other headers in file 
            current_header_type = determine_current_header_type(line, header_type_lists)

            #print(f"Current header type: {current_header_type}")

            while  line:
                # Check if we have a header line and 
                # transform accordingly if yes. 
                if is_fasta_header(line):
                    print('old head:\t', line.strip())
                    new_header = get_new_header(line, current_header_type, desired_header_type, header_type_lists)
                    print('new header:\t', new_header.strip())

                    g.write(new_header)
                else: 
                    g.write(line)

                line=f.readline() 


    # "replace" old file by removing original and replacing 
        # remove original file 
        remove_og_cmd = 'rm ' + fasta_file_name
        os.system(remove_og_cmd)
        
        # cp tmp file to new file with name of orignal 
        n = os.path.join(abs_dir_path, base_file_name)
        cp_temp_file_cmd = 'cp ' + temp_out_file_name + ' ' + n
        os.system(cp_temp_file_cmd)
        
        #remove temporaty file
        remove_temp_cmd = 'rm ' + temp_out_file_name
        os.system(remove_temp_cmd)
        
        