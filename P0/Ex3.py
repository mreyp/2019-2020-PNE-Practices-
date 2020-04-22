from Seq0 import *

FOLDER = "../Session-04/"
genes = ['U5', 'ADA', 'FRAT1', 'FXN']

for gene in genes:
    sequence = seq_read_fasta(FOLDER + gene + '.txt')

    print("Gene " + gene + "---> Length:", seq_len(sequence))