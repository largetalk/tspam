#coding:utf-8

import ahocorasick

class Inspector(object):
    def __init__(self, filename, delimiter):
        self._tree = ahocorasick.KeywordTree()

        with open(filename, 'rb') as fp:
            data = fp.read()
            #if not isinstance(data, unicode):
            #    data = data.decode('utf-8')

            words = data.split(delimiter)
            for word in words:
                if word:
                    self._tree.add(word)

        self._tree.make()

    def replace(self, text):
        if isinstance(text, unicode):
            text = text.encode('utf-8')
        last = 0
        result = []
        for match in self._tree.findall_long(text):
            result.append(text[last:match[0]])
            result.append('*' * (match[1] - match[0]))
            last = match[1]
        result.append(text[last:])
        return ''.join(result)

inspector = Inspector('banned.txt', '@')


