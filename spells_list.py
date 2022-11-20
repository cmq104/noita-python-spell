#该文件用于存放具体各项法术
import noita_spells

#投射物类
spark_bolt = noita_spells.projectile(5,3,0.05,'火花弹')
magic_bolt = noita_spells.projectile(30,12,0.12,'魔法弹')
bouncing_burst = noita_spells.projectile(5,3,-0.03,'弹跳爆发')

#投射物修正类
speed_up = noita_spells.projectile_modifier(3,0,0,'加速')#功能是给子弹加速

#多重施法类
double_spell = noita_spells.multicast(0,1,'二重施法')