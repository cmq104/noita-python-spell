class spell(object):
    draw = -1


class wand(spell):
    def __init__(self,asd):
        self.asd = asd


wand1 =wand(2)
print(wand1.draw)