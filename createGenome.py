import random

def generateGenomes(mini=16, maxi=24, total=1000):
    genomes = []
    nucleotides = ['A', 'C', 'G', 'T']

    for i in range(total):
        length = random.randint(mini, maxi)
        genome = ''
        for j in range(length):
            genome += nucleotides[random.randint(0, 3)]

        genomes.append(genome)

    return genomes
    

def writeGenomeToFile(filename, genomes):
    with open(filename, 'w') as file:
        for genome in genomes:
            file.write(genome + '\n')


genomes = generateGenomes()
writeGenomeToFile('genomes.txt', genomes)
