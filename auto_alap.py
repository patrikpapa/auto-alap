class Híres_auto:
    def __init__(self, márka_név, henger_térfogat, nemzetiség):
        self.név = márka_név
        self. henger_térfogat = henger_térfogat
        self.nemzetiseg=nemzetiseg

    def elotag(self):
        if self.nemzetiseg == 'n':
            return 'német'
        else:
            return 'japán'

híres_auto=[]
for _ in range(3):
    marka_név=input('Addja meg a márka nevét')
    henger_térfogat=int(input('Addja meg a henger_térfogatát'))
    nemzetiseg=input('Addja meg a márkát gyártó nemzetiségét')
    hirs_auto=Híres_auto(marka_név, henger_térfogat, nemzetiseg)
    híres_autok.append(hires_auto)

for híres_auto in híres_auto:
    print(f' A {Híres_auto.elotag(), híres_auto.marka_név}, egy híres, {híres_auto.elotag()}, márka, {híres_auto.henger_térfogat}')
    
# nem jo az extensionom
    