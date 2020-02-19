from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
bases = [ 'A', 'C', 'T', 'G']


print(f"Sequence 1: (Length: {s1.len()}) {s1}")

for b in bases:
    print( b + ':' , s1.count_base(b) , end =" ")

print(f"\nSequence 2: (Length: {s2.len()}) {s2}")

for b in bases:

    print(b + ':', s2.count_base(b), end=" ")

print(f"\nSequence 3: (Length: {s3.len()}) {s3}")

for b in bases:
    print(b + ':', s3.count_base(b), end=" ")



