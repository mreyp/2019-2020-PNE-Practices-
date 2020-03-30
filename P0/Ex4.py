from Seq0 import *

print('-----| Exercise 4 |------')

folder = "../Session-04/"
bases = ['A', 'C', 'T', 'G']
genes = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']

for gene in genes:
    sequence = seq_read_fasta(folder + gene + '.txt')
    print('Gene ' + gene + ':')

    for base in bases:
        print(base + ': ', seq_count_base(sequence, base))
