sample = ["macao", "macaroni", "macaroon", "machinable", "machine", "macro", "macroscopic"]
trie = {
    'm': {
        'a': {
            'c': {
                'a': {
                    'o': {
                        'is_end': True
                    },
                    'r': {
                        'o': {
                            'n': {
                                'i': {
                                    'is_end': True
                                }
                            }
                        }
                    }
                },
                'h': {
                    'i': {
                        'n': {
                            'a': {
                                'b': {
                                    'l': {
                                        'e': {
                                            'is_end': True
                                        }
                                    }
                                },
                            },
                            'e': {
                                    'is_end': True
                                }
                        }
                    }
                },
                    'r': {
                        'o': {
                            'is_end': True,
                            's': {
                                'c': {
                                    'o': {
                                        'p': {
                                            'i': {
                                                'c': {
                                                    'is_end': True
                                                }
                                            }
                                        }
                                    }
                                }
                            
                            }
                        }
                    }
            }
        },
    }
}


def insert(trie, word):
    if not word:
        trie['is_end'] = True
        return trie
        
    if word[0] not in trie:
        trie[word[0]] = {}

    trie[word[0]] = insert(trie[word[0]], word[1:])
    return trie


def isPresent(trie, word):
    if not word:
        if 'is_end' in trie:
            return True
        else:
            return False

    if word[0] not in trie:
        return False

    return isPresent(trie[word[0]], word[1:])


def dfs(node, prefixes, words):
    if 'is_end' in node:
        words.append(prefixes)
        
    for char, child in node.items():
        if char != 'is_end':
            dfs(child, prefixes + char, words)


def findWordsWithPrefix(trie, prefix):
    node = trie
    for char in prefix:
        if char not in node:
            # Prefix not found in the trie, return an empty list
            return []
        node = node[char]

    words = []

    dfs(node, prefix, words)
    return words


def getAllWords(trie):
    words = []
    dfs(trie, "", words)
    return words


def countWords(trie):
    return len(getAllWords(trie))

def delete(trie, word):
    if not word:
        if 'is_end' in trie:
            del trie['is_end']
        return trie

    if word[0] not in trie:
        return trie

    trie[word[0]] = delete(trie.get(word[0], {}), word[1:])  # Use dict.get() to handle missing keys
    if not trie[word[0]]:
        del trie[word[0]]

    return trie