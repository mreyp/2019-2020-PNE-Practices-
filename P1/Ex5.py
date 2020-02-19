from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

bases = [ 'A', 'C', 'T', 'G']
for base in bases:

    print(f"Sequence 1: (Length: {s1.len()}) {s1} {count_base(s1, base)}")
    print(f"Sequence 2: (Length: {s2.len()}) {s2}")
    print(f"Sequence 3: (Length: {s3.len()}) {s3}")

