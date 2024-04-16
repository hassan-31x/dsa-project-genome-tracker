import random

def generate_genome_structure(length_range=(4, 20), num_structures=100):
    genome_structures = []
    nucleotides = ['A', 'C', 'G', 'T']

    for _ in range(num_structures):
        length = random.randint(length_range[0], length_range[1])
        genome = ''.join(random.choices(nucleotides, k=length))
        genome_structures.append(genome)

    return genome_structures

def write_genome_structures_to_file(filename, genome_structures):
    with open(filename, 'w') as file:
        for genome in genome_structures:
            file.write(genome + '\n')

# Generate genome structures
genome_structures = generate_genome_structure()

# Write genome structures to a text file
write_genome_structures_to_file('genome_structures.txt', genome_structures)
