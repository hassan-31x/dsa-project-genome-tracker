from trie import *

def main():
    print('Genome structures loaded into trie:')
    file = 'genome_structures.txt'
    trie = createTrie(file)

    print('Genome structures with prefix "AA":', prefixWords(trie, 'AA'))
    print('Genome structures with prefix "AC":', prefixWords(trie, 'AC'))

    print('Is "ACGGTA" present in the trie?', isPresent(trie, 'ACGGTA'))
    insert(trie, 'ACGGTA')
    print('Is "ACGGTA" present in the trie after Inserting?', isPresent(trie, 'ACGGTA'))

    print('Total number of genome structures:', countWords(trie))

    if 'ATTGACTCGC' in trie:
        print('Removing "ATTGACTCGC" from the trie')
        delete(trie, 'ATTGACTCGC')
        print('Is "ATTGACTCGC" present in the trie after deleting?', isPresent(trie, 'ATTGACTCGC'))


main()