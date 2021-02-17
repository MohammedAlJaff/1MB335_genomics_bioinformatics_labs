import sys



def raw_seq_string_to_seq_object(raw_seq_string):
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
    # Creating a nucleotide translation map'
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



if __name__ == '__main__':
    print("\n\nNEW_RUN\n................")
    with open('q3.fasta', "r") as fasta_file:
        whole_raw_fasta_file_as_string = fasta_file.read()

    # split on  '>' charcter
    x  = whole_raw_fasta_file_as_string.split(sep='>')
    x = x[1:] # removing first element becasue split assigns it as an empty string. 

    if len(x) == 0:
        print('ERROR: NO SEQUENCES FOUND IN FILE...')
        sys.exit()
    else: 
        # Number of headers in fasta file 0 
        nr_headers = len(x)

        raw_seq_string_to_seq_object(x[0])

        # Each element of X will be a long string "paragraf" corresponing 
        # to a pair of (header_i, seq_of_header_i). 
        # We'lll now process each element transform them to dictionary object with 
        # the function make_into_equence_object [see begining of file for function internal algo]
        all_seq_objects = []

        for elementi_i in x: 
            seq_obj_i = raw_seq_string_to_seq_object(elementi_i)
            all_seq_objects.append(seq_obj_i)


        
        with open('new_new_reversed.fasta', "w") as new_fasta_file:
            
            for seq_obj_i in all_seq_objects:

                new_header = ">" + seq_obj_i['header'] + " Reversed" + "\n"
                new_fasta_file.write(new_header)

                reversed_sequence_i = reverse_compliment_of_sequence(seq_obj_i['sequence']) + "\n"
                new_fasta_file.write(reversed_sequence_i)

        '''
        dummy_seq_obj = all_seq_objects[3]
        s = dummy_seq_obj['sequence']

        print('first elemenet below')
       
        rev_s = reverse_compliment_of_sequence(s)
        print(f"sequence: \n{s}")
        print(f"rev sequence: \n{rev_s}")
        '''