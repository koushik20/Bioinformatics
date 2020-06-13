#Counting Nucleotide frequency of given DNA sample

def validateSeq(dna_seq, Nucleotides):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return True


def main():
    print("Enter the DNA sequence in fasta format: ")
    Nucleotides = ['A', 'C', 'T', 'G', '\n']
    lines = []
    while True:
        line = input()
        if line:

            lines.append(line)
        else:
            break
    DNA = '\n'.join(lines)

    result = validateSeq(DNA, Nucleotides)

    if result is True:

        A = DNA.count("A")
        C = DNA.count("C")
        T = DNA.count("T")
        G = DNA.count("G")

        print("\nThe number of A in your DNA sequence is: ", A)
        print("The number of C in your DNA sequence is: ", C)
        print("The number of T in your DNA sequence is: ", T)
        print("The number of G in your DNA sequence is: ", G)

        print("The GC ratio of your DNA sequence is: ", (G + C) / (A + C + T + G))
    else:
        print("invalid sequence")

if __name__ == '__main__':
    main()