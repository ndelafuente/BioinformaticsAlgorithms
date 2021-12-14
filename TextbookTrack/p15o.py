"""
Author: Huang Wenrui
https://github.com/wh2353/Rosalind_Solutions_in_Python
"""

list_of_seqs=open("rosalind_ba3c.txt","r").read().rstrip().split("\n")

'''
sorting is necessary to reduce 
time complexity of each search to O(log(N))
'''
list_of_seqs.sort()

alphabeta = 'ACGT'

#write output to file
with open("ouput.txt", "w") as out:
    
    for seq in list_of_seqs:
        '''
        try each of four bases, 
        to see attaching which one in the end 
        will generate a sequence in the list
        '''
        for letter in alphabeta:
            if seq[1:] + letter in list_of_seqs:
                out.writelines(seq + " -> " + seq[1:] + letter + "\n")
                break
out.close()
print "FINISHED"


list_of_seqs.sort() # sort the list

for seq in list_of_seqs: # for every sequence
    for letter in 'ACGT': # and for every possible base
        # If the generated suffix exists in the sequence list
        if seq[1:] + letter in list_of_seqs:
            print(seq + " -> " + seq[1:] + letter)
            break # continue to the next sequence
print "FINISHED"