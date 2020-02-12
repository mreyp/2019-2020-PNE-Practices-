from Seq0 import *

print('------| Exercise 6 |------')
folder = "../Session-04/"
filename = 'U5.txt'
sequence = seq_read_fasta(folder + filename)

print('Gene ' + filename + ':')
print('Gene ' + (sequence[:19]))
print('Frag: ', seq_reverse(sequence[:19]))