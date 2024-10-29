def main():
    print(DNA_strand('ATTGC'))

def DNA_strand(dna):
    dna_strand_list = []
    for i in dna:
        if i == 'A':
            i = 'T'
        elif i == 'T':
            i = 'A'
        elif i == 'G':
            i = 'C'
        elif i == 'C':
            i = 'G'

        dna_strand_list.append(i)
    return ''.join(dna_strand_list)


if __name__ == '__main__':
    main()