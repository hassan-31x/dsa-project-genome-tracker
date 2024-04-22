from trie import *

def main():
    print('Genome structures loaded into trie:')
    prefixTrie = createTrie('genomes.txt', 'prefix')
    suffixTrie = createTrie('genomes.txt', 'suffix')

    print('Genome structures with prefix "AA":')
    print(prefixWords(prefixTrie, 'AA', trieType='prefix'))
    print(prefixWords(suffixTrie, 'AA', trieType='suffix'))

    print('Is "CCGAGATGTAGCATAC" present in the trie?', isPresent(prefixTrie, 'CCGAGATGTAGCATAC'))
    insert(prefixTrie, 'CCGAGATGTAGCATAC')
    print('Is "CCGAGATGTAGCATAC" present in the trie after Inserting?', isPresent(prefixTrie, 'CCGAGATGTAGCATAC'))

    if isPresent(prefixTrie, 'CCGAGATGTAGCATAC'):
        print('Removing "CCGAGATGTAGCATAC" from the trie')
        delete(prefixTrie, 'CCGAGATGTAGCATAC')
        print('Is "CCGAGATGTAGCATAC" present in the trie after deleting?', isPresent(prefixTrie, 'CCGAGATGTAGCATAC'))
    
main()