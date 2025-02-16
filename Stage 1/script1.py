"""
This script contains four functions:
1. dna_to_protein: Translates a DNA sequence into a protein sequence.
2. generate_logistic_growth_curves: Generates multiple logistic growth curves.
3. time_to_80_percent_growth: Determines the time to reach 80% of the carrying capacity.
4. hamming_distance: Computes the Hamming distance between two strings.
"""

# Function 1: Translate DNA to Protein
codon_table = {
    'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine',
    'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGA': 'STOP', 'UGG': 'Tryptophan', 'CUU': 'Leucine', 'CUC': 'Leucine',
    'CUA': 'Leucine', 'CUG': 'Leucine', 'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline',
    'CAU': 'Histidine', 'CAC': 'Histidine', 'CAA': 'Glutamine', 'CAG': 'Glutamine', 'CGU': 'Arginine',
    'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine', 'AUU': 'Isoleucine', 'AUC': 'Isoleucine',
    'AUA': 'Isoleucine', 'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine',
    'AAU': 'Asparagine', 'AAC': 'Asparagine', 'AAA': 'Lysine', 'AAG': 'Lysine', 'AGU': 'Serine', 'AGC': 'Serine',
    'AGA': 'Arginine', 'AGG': 'Arginine', 'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine',
    'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine', 'GAU': 'Aspartic Acid', 
    'GAC': 'Aspartic Acid', 'GAA': 'Glutamic Acid', 'GAG': 'Glutamic Acid', 'GGU': 'Glycine', 'GGC': 'Glycine',
    'GGA': 'Glycine', 'GGG': 'Glycine'
}

def dna_to_protein(dna_sequence):
    mRNA = dna_sequence.replace('T', 'U')
    codons = [mRNA[i:i+3] for i in range(0, len(mRNA), 3)]
    protein = []
    for codon in codons:
        if codon in codon_table:
            amino_acid = codon_table[codon]
            if amino_acid == 'STOP':
                break
            protein.append(amino_acid)
    return protein

# Function 2: Generate Logistic Growth Curves
def generate_logistic_growth_curves(num_curves=100, K=1000, P0=10, E=2.71828, max_time=100):
    growth_curves = []
    for curve_index in range(num_curves):
        lag_variation = (curve_index % 16) + 5  
        growth_rate = 0.12 + ((curve_index % 14) + 2) / 100
        curve_data = {"Time": [], "Population": [], "Curve": curve_index + 1}
        for time_step in range(max_time):
            if time_step < lag_variation:
                population_size = P0
            else:
                population_size = (K / (1 + ((K - P0) / P0) * (E ** (-growth_rate * (time_step - lag_variation)))))
            curve_data["Time"].append(time_step)
            curve_data["Population"].append(population_size)
        growth_curves.append(curve_data)
    return growth_curves

# Function 3: Time to Reach 80% of Carrying Capacity
def time_to_80_percent_growth(K, P, r, dt=0.01):
    t = 0
    P_target = 0.8 * K
    while P < P_target:
        P += r * P * (1 - P / K) * dt
        t += dt
    return t

# Function 4: Hamming Distance
def hamming_distance(username1, username2):
    if len(username1) != len(username2):
        raise ValueError("Strings must be of equal length to compute Hamming distance.")
    return sum(c1 != c2 for c1, c2 in zip(username1, username2))

# Example Usage
dna = "ATGGCCATTGTAATGGGCCGAGGAG"
print("Protein sequence:", dna_to_protein(dna))

growth_curves = generate_logistic_growth_curves(num_curves=10, max_time=20)
print("Generated logistic growth curves:", growth_curves[:2])  # Displaying first two

K, P, r = 1000, 10, 0.1
time_to_80 = time_to_80_percent_growth(K, P, r)
print("Time to reach 80% of carrying capacity:", time_to_80)

print("Hamming distance:", hamming_distance("AmakaMadubuike", "AmakaMadubuike"))
