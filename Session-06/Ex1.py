class Seq:
    """A class for representing sequence objects"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        bases = ['A', 'C', 'T', 'G']

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")


    print(f"Sequence 1: {s1}")
    print(f"Sequence 2: {s2}")