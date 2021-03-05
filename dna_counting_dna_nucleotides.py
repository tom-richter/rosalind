def count_nucleotides(dna: str) -> str:
    result = ''

    for nucleotide in ['A', 'C', 'G', 'T']:
        result += str(dna.count(nucleotide)) + ' '

    return result.strip()


dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

print(count_nucleotides(dna))
