from pprint import pprint

words = []
with open('words.txt') as f:
    for word in f:
        word = word.strip()
        words.append(word)

def is_amagram(word1, word2):
    return sorted(word1) == sorted(word2)

def anagrams():
    result = {}

    longest_sig = None
    longest_len = -1

    for w in words:
        signature = "".join(sorted(w))

        if signature not in result:
            result[signature] = []

        result[signature].append(w)

        if len(result[signature]) >= longest_len:
            longest_len = len(result[signature])
            longest_sig = signature

    return result[longest_sig]

pprint(anagrams())
