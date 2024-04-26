import streamlit as sl
from trie import *


def handleAdd(prefixTrie, suffixTrie, i):
    prefixTrie = insert(prefixTrie, i)
    suffixTrie = insert(suffixTrie, i[::-1])
    print(i)
    sl.success(f'Added {i} to the Database')

    return prefixTrie, suffixTrie

def showSearch(prefixTrie, suffixTrie):
    sl.header('Geno Search')
    sl.subheader('Manage Genome Structures Effectively')

    i = sl.text_input('Enter Genome to Search')

    if i:
        p = prefixWords(prefixTrie, i, trieType='prefix')
        s = prefixWords(suffixTrie, i, trieType='suffix')

        for word in p:
            sl.markdown(f':red[{i}]{word[len(i):]}')
        for word in s:
            sl.markdown(f'{word[:len(word)-len(i)]}:red[{i}]')
        
        if not p and not s:
            sl.warning('No Results Found')
            if sl.button('Add to Database'):
                print(isPresent(prefixTrie, i))
                prefixTree = insert(prefixTrie, i)
                suffixTrie = insert(suffixTrie, i[::-1])
                sl.success(f'Added {i} to the Database')
                print(isPresent(prefixTrie, i))

                # print(isPresent(prefixTrie, 'CCGAGATGTAGCATAC'))
                # t = insert(prefixTrie, 'CCGAGATGTAGCATAC')
                # print(isPresent(prefixTrie, 'CCGAGATGTAGCATAC'))

def add():
    # if sl.button('Add to Database'):
    pass
    #     insert(prefixTrie, i)
    #     insert(suffixTrie, i[::-1])
    #     sl.success(f'Added {i} to the Database')

    #     print(isPresent(prefixTrie, 'CCGAGATGTAGCATAC'))
    #     t = insert(prefixTrie, 'CCGAGATGTAGCATAC')
    #     print(isPresent(prefixTrie, 'CCGAGATGTAGCATAC'))

def main():
    prefixTrie = createTrie('genomes.txt', 'prefix')
    suffixTrie = createTrie('genomes.txt', 'suffix')
    showSearch(prefixTrie, suffixTrie)
    sl.markdown('---')
    add()


        
main()