'''
Author: Jose Eduardo Soto JoeySo22

This program is written linearly without defining subroutines or functions.
It makes it much more easier to read and understand the program. First,
the input is checked. Next, parse through the file and count the words
line by line. Finally, write to the file in descending order which takes
n^2 time.
'''

import sys, re

l_args = len(sys.argv)

# Assert we have two plus one arguements
if (len(sys.argv) != 3):
    print('Error: Requires 1 input filename and 1 output filename')
else:
    input_file = ''
    output_file = ''
    try:
        input_file = open(sys.argv[1], 'r')
    except:
        print('Error: Cannot open input file %s' % sys.argv[1])
        sys.exit(-1)
    try: 
        output_file = open(sys.argv[2], 'w')
    except:
        print('Error: Cannot write to output file %s' % sys.argv[2])
        sys.exit(-1)
    print('> Files openned.')


    # Contain the word counting in a dictionary.
    word_dictionary = {}
    # Iterate through the input file until there are no more lines.
    print('> Reading and building dictionary...')
    while True:

        
        # Read each line to digest.
        line = input_file.readline()
        '''
        An empty string will tell us when readline() has reached the EOF.
        If the text document as a vertical spacing by paragraph seperation
        then there is a new-line character. Therefore, the empty string IS the 
        EOF.
        '''
        if (len(line) == 0):
            print('> Finished parsing input file.')
            break
        # Make line into all lowercase
        line = line.lower()
        # Substitute all non-alphabet characters into empty strings
        line = re.sub('[^ a-z]', '', line)
        # Seperate all strings by whitespace
        word_vector = line.split()

        
        '''
        Now all of our words are split into a list we can iterate them
        and begin counting.
        '''
        for word in word_vector:
            if word in word_dictionary:
                word_dictionary[word] += 1
                #print('>>Incrementing Dict %s \t %d' % (word, word_dictionary[word]))
            else:
                #print('>>Adding to Dict %s \t %d' % (word, 1))
                word_dictionary[word] = 1

                
# Write results into file in descending order (greatest to lowest)
print('> Adding max entries into output file...')
while True: # Done by 2830 
    if len(word_dictionary) > 0:
        max_key = ''
        max_value = 0
        for key in word_dictionary:
            if word_dictionary[key] > max_value:
                #print('>>Maxkey=%s\tMaxvalue=%d' % (key, word_dictionary[key]))
                max_key = key
                max_value = word_dictionary[key]
        output_file.write('%s\t\t%d\n' % (max_key, max_value))
        #print('>>inputting %s \t\t %d' % (max_key, max_value))
        word_dictionary.pop(max_key)
    else:
        print('> Finished dictionary.')
        break


# Close everything back up.
print('> Closing files...')
input_file.close()
output_file.close()
print('> DONE')
                
    
                
    
