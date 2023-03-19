class NFA:
    def __init__(self, delta, q0, final,drumuri):
        self.delta = delta #tranzitii
        self.q0 = q0 #stare initiala
        self.final = final
        self.drumuri = drumuri

    def run(self, word,p,lista):
        if p != self.q0:
            q = p
        else:
            q = self.q0
        lista2 = lista.copy()
        lista2.append(p)
        if word != "":
            if (q, word[0]) in self.delta:
                for i in range(len(self.delta[(q, word[0])])):
                    a = self.delta[(q, word[0])][i]
                    self.run(word[1:],a,lista2)
            else:
                return False
        else:
            if q in self.final:
                self.drumuri.append(lista2)

    def dr(self):
        return self.drumuri

    def reset(self):
        self.drumuri = []

'''
format automata.in
stare initiala
stari finale
nod litera nod (de n ori)
'''
f = open("automata.in", 'r')
'''
format words
word
word
word...
'''
g = open("words.in", 'r')
q0 = f.readline().strip()
final = [x.strip() for x in f.readline().split()]
delta = {}

for linie in f:
    linie = linie.split()
    if (linie[0], linie[1]) in delta:
        delta[(linie[0], linie[1])].append(linie[2])
    else:
        delta[(linie[0], linie[1])] = [linie[2]]


auto = NFA(delta,q0,final,[])


for word in g:
    auto.reset()
    word = word.strip()
    '''q0 stare initiala
    lista goala pentru retinerea drumului'''
    auto.run(word,q0,[])
    drum = auto.dr()

    if len(drum) == 0:
        print(f"\nThe word {word} has been rejected.")
    else:
        print(f"\nThe word {word} has been accepted.")
        for d in drum:
            print(*d,sep="-")

f.close()
g.close()