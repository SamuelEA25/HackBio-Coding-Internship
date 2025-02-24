"""
This script is composed of four functions:
Function 1: dna_to_protein: Translates a DNA sequence into a protein sequence.
Function 2: generate_logistic_growth_curves: Generates multiple logistic growth curves.
Function 3: time_to_80_percent_growth: Determines the time to reach 80% of the carrying capacity.
Function 4: hamming_distance: Calculates the Hamming distance between two sets of strings (usernames).
"""

# Function 1: Translate DNA to Protein
# Create a dictionary (codon_table) mapping RNA codons to corresponding amino acids (or 'Stop' for termination)
codon_table = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',

    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',

    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',

    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}

# Define a function (dna_to_protein), which accepts a string (dna_sequence), and translates a given DNA sequence into a protein sequence.
def dna_to_protein(dna_sequence):
    mRNA = dna_sequence.replace('T', 'U')  # Transcribe DNA sequence into mRNA by replacing T with U
    protein = ""  # Initialise an empty string to store the protein sequence after translation
    
    # Use a for loop to iterate through mRNA sequence in steps of 3 codons until the entire length of the mRNA sequence is covered
    for i in range(0, len(mRNA), 3):  
        codon = mRNA[i:i+3]  # Extract a three-base long codon
        
        if codon in codon_table:  # Check if codon exists in the codon_table
            amino_acid = codon_table[codon]  # Get the amino acid that corresponds to the current codon in the codon_table
            
            if amino_acid == 'Stop':  # Stop codon encountered
                break  # Stop the loop and terminate translation
            
            protein += amino_acid  # Add the translatded amino acid to protein string as the loop progresses
    
    return protein # Returns the final protein sequence upon loop completion (or stop codon interruption)


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
        raise InvalidValueError("Strings must be of equal length to compute hamming distance.") # Verify that the two usernames are of equal length
    distance = 0  # Ensures that the distance counter begins from zero
    # Create a loop to compare characters (c) at the same position (index) between both usernames 
    for c in range(len(username1)):
        if username1[c] != username2[c]:
            distance += 1  # Increase the distance variable count by 1 for every difference found

    return distance
