#该文件用于定义法杖基础属性
class wand:#法杖类
    def __init__(self,shuffle,spell_cast,mana,mana_recharge,reload,delay,slots):#构造函数
        self.shuffle = shuffle
        self.spell_cast = spell_cast
        self.mana = mana
        self.mana_recharge = mana_recharge
        self.reload = reload
        self.delay = delay
        self.slots = slots
# shuffle:乱序,spell_cast:抽取数,mana:法力,mana_recharge:法力回复,reload:充能时间,delay:施法延迟,slots:容量,multicast:多重施法
    wand_spell = [1,2,3]

    def input_spells(self,wand_spell1):
        global wand_spell
        wand_spell = input(wand_spell1)



