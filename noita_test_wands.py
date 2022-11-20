# 该文件用于创建法术装填并且具体释放法术测试

import noita_wands
import spells_list

wand1 = noita_wands.wand(False, 1, 500, 500, 0.5, 0.3, 20)

wand1.wand_spell = [spells_list.magic_bolt, spells_list.spark_bolt,\
                    spells_list.bouncing_burst, spells_list.double_spell, spells_list.speed_up, spells_list.magic_bolt]
# 总体需要先判断法力值是否足够才能进行法术，释放法术顺序根据list来读取
# 设定施法块，当记录抽取数为0的时候将保存施法块并执行下一个施法块，初始为1抽取数

present_draw = 0
block_amount = 1


def casting_block():  # 判定施法块施法块
    global present_draw
    global block_amount
    left_draw = 1  # 剩余抽数
    print('第', block_amount, '施法块:')
    while left_draw > 0:
        left_draw = left_draw + wand1.wand_spell[present_draw].draw  # 加上法术的抽取数，为0是变成一个
        print(wand1.wand_spell[present_draw].name)
        present_draw += 1
    block_amount += 1


def test_wands():  # 打印所有施法块
    global present_draw
    while present_draw < len(wand1.wand_spell):
        casting_block()


test_wands()
