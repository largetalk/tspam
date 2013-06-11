#coding:utf-8

banned_text = 'banned.txt'
SPLIT = '@'
BANNED_T = None

from pytrie import SortedStringTrie as trie

def init_banned_tree():
    global BANNED_T
    if BANNED_T:
        return BANNED_T

    with open(banned_text, 'rb') as fp:
        data = fp.read()

        words = data.split(SPLIT)
        BANNED_T = trie.fromkeys(words, 1)
    return BANNED_T


def replace_banned(text):
    init_banned_tree()
    l = len(text)
    i = 0
    result = []
    while i < l:
        word = text[i]
        if BANNED_T.keys(prefix=word):
            check_word = text[i:i+50]
            try:
                pre = BANNED_T.longest_prefix(check_word)
                w_l = len(pre)
                result.append('*' * w_l )
                i += w_l
                continue
            except:
                pass
        result.append(word)
        i += 1

    return ''.join(result)

print replace_banned('强烈要求领导财产公示和收回钓鱼岛')
            


