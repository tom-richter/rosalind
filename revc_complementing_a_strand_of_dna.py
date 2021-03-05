def reverse_complement(dna: str) -> str:
    complements = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    reversed_complemented_dna = ''

    for base in dna[::-1]:
        reversed_complemented_dna += complements[base]

    return reversed_complemented_dna


dna = 'AAAACCCGGT'

print(reverse_complement(dna))
