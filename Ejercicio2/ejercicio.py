
class Texto:
    def __init__(self, texto):
        self.texto = texto
    
    def separador_frases(self):
        l = len(self.texto)
        lists = []
        for i in range(l):

            print(self.texto[i])
            char = self.texto[i]
            if char == "#":
                lists.append(i)
            
            lists.append(l)

            start = 0
            end = 0
            phrases = []

            for list in lists:
                end = list
                txt = self.texto[start:end]
                start = end + 1
                t = txt.capitalize()
                phrases.append(t)
            print()
            for c in phrases:
                print(c)