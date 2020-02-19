from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")

s1 = Seq()
s1.read_fasta(FILENAME)

print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print('\tBases: ',s1.count())
print("\tRev: ", s1.reverse())
print("\tComp:", s1.complement())