#该文件用于定义法术类型
import noita_wands


class spell(object):
    draw = -1


class projectile(spell):#投射物，最基础的物品
    def __init__(self,mana_drain,damage,cast_delay,name):
        self.mana_drain = mana_drain
        self.damage = damage
        self.cast_delay = cast_delay
        self.name = name


class projectile_modifier(spell):#投射物修正
    def __init__(self,mana_drain,damage,cast_delay,name):
        self.mana_drain = mana_drain
        self.damage = damage
        self.cast_delay = cast_delay
        self.name = name
    draw = 0


class multicast(spell):
    def __init__(self,mana_drain,draw,name):
        self.draw = draw
        self.mana_drain =mana_drain
        self.name = name




