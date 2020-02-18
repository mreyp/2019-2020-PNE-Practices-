import termcolor

class Seq:
    def __init__(self, strbases):
        bases = ["A", 'C', 'G', 'T']
        for i in strbases:
            if i not in bases:
                print("ERROR!")
                self.strbases = "INCORRECT sequence detected"
                return

        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]


def print_seqs(seq_list,termcolor):
    for seq in seq_list:
        termcolor.cprint("Sequence ", seq_list.index(seq), ":", "(Length: ", seq.len(),")", seq, 'green')

print_seqs(seq_list, termcolor)
