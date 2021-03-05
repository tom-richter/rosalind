def to_rna(dna: str) -> str:
    return dna.replace('T', 'U')


dna = 'GATGGAACTTGACTACGTAAATT'

print(to_rna(dna))
