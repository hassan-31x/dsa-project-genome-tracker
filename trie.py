words = ["ant", "alligator", "almond", "bear", "bee", "butterfly", "ball", "bat", "cat", "dog", "duck", "elephant", "egg", "fish", "frog", "giraffe", "gorilla", "hippo", "horse", "iguana", "jellyfish", "kangaroo", "lion", "monkey", "mouse", "owl", "penguin", "quail", "rabbit", "snake", "tiger", "turtle", "unicorn", "vulture", "walrus", "zebra"]


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
                                'e': {
                                    'is_end': True
                                }
                            }
                        }
                    }
                },
                'c': {
                    'r': {
                        'o': {
                            'is_end': True
                        }
                    }
                }
            }
        },
    }
}