def insert(trie, word):
    if word == '':
        trie['is_end'] = True
        return trie
        
    if word[0] not in trie:
        trie[word[0]] = {}

    trie[word[0]] = insert(trie[word[0]], word[1:])
    return trie


def createTrie(filename, trieType='prefix'):
    trie = {}

    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            if trieType == 'prefix':
                trie = insert(trie, word)
            elif trieType == 'suffix':
                trie = insert(trie, word[::-1])

    return trie


def isPresent(trie, word):
    if word == '':
        if 'is_end' in trie:
            return True
        else:
            return False

    if word[0] not in trie:
        return False

    return isPresent(trie[word[0]], word[1:])


def helperPrefix(node, prefixes, words, trieType='prefix'):
    if 'is_end' in node:
        if trieType == 'prefix':
            words.append(prefixes)
        else:
            words.append(prefixes[::-1])
        
    for childKey, childDictionary in node.items():
        if childKey != 'is_end':
            helperPrefix(childDictionary, prefixes + childKey, words, trieType)


def prefixWords(trie, prefix, trieType='prefix'):
    trieCopy = trie
    for char in prefix:
        if char not in trieCopy:
            return []
        trieCopy = trieCopy[char]

    words = []
    helperPrefix(trieCopy, prefix, words, trieType)
    return words


def getAllWords(trie):
    return prefixWords(trie, "")


def countWords(trie):
    return len(getAllWords(trie))


def delete(trie, word):
    if word == '':
        if 'is_end' in trie:
            del trie['is_end']
        return trie

    if word[0] not in trie:
        return trie

    trie[word[0]] = delete(trie.get(word[0], {}), word[1:])

    return trie