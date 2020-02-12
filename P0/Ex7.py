from Seq0 import *
print('-----| Exercise 7 |------')
folder = "../Session-04/"
filename = 'U5.txt'
sequence = seq_read_fasta(folder + filename)

print('Gene ' + filename + ':')
print('Frag ' + (sequence[:19])
print('Comp: ', seq_complement(sequence[:19]))