class lexicon(object):

    palabras = {'direction': ['north', 'south', 'east', 'west', 'down', 'up',
                             'left', 'right', 'back'],
               'verb': ['go', 'stop', 'kill', 'eat'],
               'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
               'noun': ['door', 'bear', 'princess', 'cabinet']}
            
    def __init__(self):
        pass
        #print 'Initialized'

    def in_lexicon(self, w):
        for k in self.palabras.keys():
            if w in self.palabras[k]:
                return k

        return -1

    def scan(self, usr_input):
        words = [s.lower() for s in usr_input.split()]
        res = []
        for w in words:
            key = self.in_lexicon(w)
            if key != -1:
                res.append((key, w))
            else:
                try:
                    res.append(('number', int(w)))
                except ValueError:
                    res.append(('error', w))

        return res

#a = lexicon()
#print a.scan(raw_input("> "))
