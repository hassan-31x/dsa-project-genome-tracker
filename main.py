import streamlit as sl
from st_keyup import st_keyup
from trie import *

def validate(genome):
    for i in genome:
        if i not in ['A', 'C', 'G', 'T']:
            return False
    return True

def main():
    prefixTrie = createTrie('genomes.txt', 'prefix')
    suffixTrie = createTrie('genomes.txt', 'suffix')
    
    sl.header('Geno Search')
    sl.subheader('Manage Genome Structures Effectively')

    i = st_keyup('Enter Genome to Search', key='0')

    if i:
        p = prefixWords(prefixTrie, i, trieType='prefix')
        s = prefixWords(suffixTrie, i, trieType='suffix')

        for word in p:
            col1, col2 = sl.columns([6, 1])
            col1.markdown(f':red[{i}]{word[len(i):]}')
            if col2.button('Delete', key=word+str(len(i)), type='primary'):
                deletePermenant(word)
                sl.success(f'Deleted {word} from the Database')
                prefixTrie = createTrie('genomes.txt', 'prefix')
                suffixTrie = createTrie('genomes.txt', 'suffix')
        for word in s:
            if word in p:
                continue
            col1, col2 = sl.columns([6, 1])
            col1.markdown(f'{word[:len(word)-len(i)]}:red[{i}]')
            if col2.button('Delete', key=word+str(len(i)), type='primary'):
                deletePermenant(word)
                sl.success(f'Deleted {word} from the Database')
                prefixTrie = createTrie('genomes.txt', 'prefix')
                suffixTrie = createTrie('genomes.txt', 'suffix')
        
        if not p and not s:
            sl.warning('No Results Found')
            if sl.button('Add to Database'):
                if validate(i):
                    insertPermenant(i)
                    prefixTrie = createTrie('genomes.txt', 'prefix')
                    suffixTrie = createTrie('genomes.txt', 'suffix')

                    sl.success(f'Added {i} to the Database')
                else:
                    sl.error('Invalid Genome Structure')

main()