from Seq0 import *

print('------| Exercise 6 |------')
folder = "../Session-04/"
filename = 'U5.txt'
sequence = seq_read_fasta(folder + filename)

print('Gene ' + filename + ':')
print('Frag: ' + (sequence[:20]))
print('Rev: ', seq_reverse(sequence[:20]))