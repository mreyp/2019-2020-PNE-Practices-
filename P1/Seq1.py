import self as self


class Seq:
    """A class for representing sequence objects"""

    def __init__(self, strbases="NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object

        if strbases == "NULL":
            print("NULL Seq created!")
            self.strbases = "NULL"

        elif strbases == "Invalid sequence":
            print("INVALID Seq!")
            self.strbases = "ERROR"

        else:
            self.strbases = strbases
            print("New sequence created!")

        return

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):

            return len(self.strbases)

    pass

    def count_base(self, base):
        return self.strbases.count(base)

    def count(seq):
        bases = ['A', 'C', 'T', 'G']
        count_bases = []
        for base in bases:
            count_bases.append(seq.count_base(seq, base))
        dicti = dict(zip(bases, count_bases))
        return dicti

    def reverse(seq):
        return seq[::-1]

    def complement(seq):
        bases = ['A', 'C', 'T', 'G']
        compl_bases = ['T', 'G', 'A', 'C']
        dict_bases_compl = dict(zip(bases, compl_bases))
        complementary = ''
        for i in seq:
            for base, c_base in dict_bases_compl.items():
                if i == base:
                    complementary += c_base
        return (complementary)