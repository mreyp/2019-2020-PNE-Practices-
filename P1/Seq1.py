import self as self


class Seq:
    """A class for representing sequence objects"""

    def __init__(self, strbases="NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object

        if strbases == "NULL":
            print("NULL Seq created")
            self.strbases = "NULL"

        elif strbases == "Invalid sequence":
            print("INVALID Seq!")
            self.strbases = "Invalid sequence"

            return

        else:
            self.strbases = strbases
            print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

    pass
