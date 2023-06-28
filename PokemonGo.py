import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
import time

import os
import random

def clear():
    os.system("cls")

#####################个人私货环节
def mryj():
    kst = random.randint(1,20)
    if kst == 1:
        asahi = "宇宙或许在膨胀，但我们正日渐接近。\n                 ——Stellaris"
    elif kst == 2:
        asahi = "我们走后，他们会给你们修建学校和医院；这不是因为他们良心发现，而是因为我们来过。\n                 ——古巴革命名言"
    elif kst == 3:
        asahi = "一切伟大都要以牺牲来铸就。愚昧者或许无法理解，但他们必将服从。\n                 ——Stellaris"
    elif kst == 4:
        asahi = "我们活着，就是对恶意最大的反抗。\n                 ——LGBT平权运动"
    elif kst == 5:
        asahi = "我不同意你说的每一个字，但我誓死捍卫你说话的权利。\n                 ——伏尔泰"
    elif kst == 6:
        asahi = "We shall go on to the end. We shall never surrender.\n                 ——温斯顿·丘吉尔，《We shall fight on the beaches》，1940"
    elif kst == 7:
        asahi = "这是我的一小步，但却是人类的一大步。\n                 ——尼尔·奥尔登·阿姆斯特朗,1966于月球表面"
    elif kst == 8:
        asahi = "Ни шагу назад!(No Step Back!)\n                 ——苏联第227号命令，1942"
    elif kst == 9:
        asahi = "你的名字无人知晓，你的功绩永世长存。\n                 ——无名英雄纪念碑（莫斯科）碑文"
    elif kst == 10:
        asahi = "今天是我们，明天就轮到你。\n                 ——海尔·塞拉西一世（谴责英国和法国的绥靖政策），1936"
    elif kst == 11:
        asahi = "穿越泥泞与鲜血到达绿野的彼端。\n                 ——加拿大皇家装甲部队座右铭"
    elif kst == 12:
        asahi = "挨饿和失业的人民是独裁的土壤。\n                 ——富兰克林 D. 罗斯福，1933"
    elif kst == 13:
        asahi = "他们将不能通过！\n                 ——罗贝尔·尼维尔，1916"
    elif kst == 14:
        asahi = "我能尽心奉献的别无他物，唯有热血、辛劳、眼泪和汗水。\n                 ——温斯顿·丘吉尔，《热血、辛劳、眼泪和汗水》，1940"
    elif kst == 15:
        asahi = "工事，火炮，外援都毫无意义。除非普通的士兵都清楚，他，正在保卫国家。\n                 ——卡尔·古斯塔夫·埃米尔·曼纳海姆，1940"
    elif kst == 16:
        asahi = "过路人啊，请给斯巴达人传个话，为了履行对他们的承诺，我们永远地留在了这里。\n                 ——温泉关，斯巴达勇士墓碑碑文"
    elif kst == 17:
        asahi = "我宽恕造成我死亡的人，我还要祈求上帝，在我鲜血抛洒之后，在法国的土地上再也不要流血了。\n                 ——路易十六，1793"
    elif kst == 18:
        asahi = "这个时代的重大的问题不是演说和决议所能解决的……这些问题只有铁和血才能解决。\n                 ——奥托·冯·俾斯麦，1862"
    elif kst == 19:
        asahi = "我的双手沾满了鲜血。\n                 ——罗伯特·奥本海默（听说原子弹在广岛和长崎爆炸后），1945"
    elif kst == 20:
        asahi = "总而言之，一方面是竞争和倾轧，另一方面是利害冲突，人人都时时隐藏着损人利己之心。这一切灾祸，都是私有财产的第一个后果，同时也是新产生的不平等的必然产物。\n                 ——让·雅克·卢梭，《论人类不平等的起源与基础》，1755"
    return asahi 

#####################

######

skp1 = ""
skp2 = ""
sp1 = ""
sp2 = ""
asahi1 = True
asahi2 = True

sb1 = False
sb2 = False

exp1 = 0.1
exp2 = 0.1
exr1 = 1.5
exr2 = 1.5
exf1 = ""
exf2 = ""

######

class Servant:
    def __init__(self,name,hp,atk,defe,spd,skill):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defe = defe
        self.spd = spd
        self.skill = skill
    
######

class Skill:
    def __init__(self,id,name,power):
        self.id = id
        self.name = name
        self.power = power

    def exe(self,m,n):

        global asahi1,asahi2,lphs1,lphs2,skp1,skp2,sp1,sp2,exp1,exp2,exr1,exr2,sb1,sb2

        lphs1 = P1.spd / P2.spd
        lphs2 = P2.spd / P1.spd  #あさひ
        
        if m == 0:
            if random.random() > lphs1 * 0.5 + 0.5:
                asahi1 = False
        elif m == 1:
            if random.random() > lphs2 * 0.5 + 0.5:
                asahi2 = False 

        listh = [asahi1,asahi2]

        damage = self.power/100 * (list[m].atk - list[n].defe)

        if self.id == 1:
            damage = damage + list[n].hp * 0.15
            if random.random() < 0.15:
                bufflist.append(Buff(B2.id,B2.name,n,B2.ef1,B2.ef2,B2.ef3,B2.ef4,2,0,0))
                txt.insert("1.0",f"{list0[n]}的{list[n].name}受到了眩晕效果。\n")
        elif self.id == 3:
            damage = damage + list[m].hp * 0.2
        elif self.id == 4:
            list[m].atk = list[m].atk * 1.1
            list[m].defe = list[m].defe * 1.05
            list[m].hp = list[m].hp + list[m].atk * 0.4 + 10
            list[m].atk = int(list[m].atk)
            list[m].defe = int(list[m].defe)
            list[m].hp = int(list[m].hp)
            if m == 0:
                skp1 = f"P1的{P1.name}使用{Sk4.name},攻击、防御提升一级。回复{int(P1.atk*0.4 + 10)}点HP。\n"
                asahi1 = True  #あさひ
            elif m == 1:
                skp2 = f"P2的{P2.name}使用{Sk4.name},攻击、防御提升一级。回复{int(P2.atk*0.4 + 10)}点HP。\n"
                asahi2 = True
        elif self.id == 5:
            if listh[m] == True:
                list[m].atk = list[m].atk * 1.1
                list[m].atk = int(list[m].atk)
                if damage > 1:
                    list[m].hp = list[m].hp - damage * 0.25
                    list[m].hp = int(list[m].hp)
                    if m == 0:
                        sp1 = f"P1的{P1.name}使用{Sk5.name},攻击提升一级，但是震伤了自己，失去{int(damage*0.25)}点HP。"
                    elif m == 1:
                        sp2 = f"P2的{P2.name}使用{Sk5.name},攻击提升一级，但是震伤了自己，失去{int(damage*0.25)}点HP。"
                elif damage <= 1:
                    list[m].hp = list[m].hp - 1
                    if m == 0:
                        sp1 = f"P1的{P2.name}使用{Sk5.name},攻击提升一级，但是震伤了自己，失去1点HP。"
                    elif m == 1:
                        sp2 = f"P2的{P2.name}使用{Sk5.name},攻击提升一级，但是震伤了自己，失去1点HP。"
                if random.random() < 0.07:
                    bufflist.append(Buff(B2.id,B2.name,n,B2.ef1,B2.ef2,B2.ef3,B2.ef4,2,0,0))
                    txt.insert("1.0",f"{list0[n]}的{list[n].name}受到了眩晕效果。\n")
        elif self.id == 6:
            list[m].defe = list[m].defe * 1.1
            list[m].defe = int(list[m].defe)
            if m == 0:
                skp1 = f"P1的{P1.name}使用{Sk6.name},防御提升两级。\n"
                asahi1 = True
            elif m == 1:
                skp2 = f"P2的{P2.name}使用{Sk6.name},防御提升两级。\n"
                asahi2 = True
        elif self.id == 7:
            if listh[m] == True:
                bufflist.append(Buff(B1.id,B1.name,n,B1.ef1,B1.ef2,B1.ef3,B1.ef4,3,0,0))        
        elif self.id == 8:
            damage = damage + (list1[n].hp - list[n].hp) * 0.4  #あさひ
        elif self.id == 9:
            list[m].atk = list[m].atk * 1.1
            list[m].atk = int(list[m].atk)
            list[n].atk = list[n].atk * 0.9
            list[n].atk = int(list[n].atk)
            if m == 0:
                skp1 = f"P1的{P1.name}使用{Sk9.name},自身攻击提升一级，对方攻击下降一级。\n"
                asahi1 = True
            elif m == 1:
                skp2 = f"P2的{P2.name}使用{Sk9.name},自身攻击提升一级，对方攻击下降一级。\n"
                asahi2 = True
        elif self.id == 10:
            if listh[m] == True:
                bufflist.append(Buff(B1.id,B1.name,n,B1.ef1,B1.ef2,B1.ef3,B1.ef4,3,0,0))
                if random.random() < 0.2:
                    bufflist.append(Buff(B1.id,B1.name,m,B1.ef1,B1.ef2,B1.ef3,B1.ef4,2,0,0))
        elif self.id == 12:
            if random.random() < 0.4:
                if m == 0:
                    asahi1 = True
                elif m == 1:
                    asahi2 = True
                trf = random.random()
                if trf <= 0.5:
                    bufflist.append(Buff(B4.id,B4.name,n,B4.ef1,B4.ef2,B4.ef3,B4.ef4,3,0,0))
                    txt.insert("1.0",f"{list0[n]}的{list[n].name}受到了困惑效果。\n")
                elif trf > 0.5 and trf < 0.9:
                    bufflist.append(Buff(B4.id,B4.name,n,B4.ef1,B4.ef2,B4.ef3,B4.ef4,4,0,0))
                    txt.insert("1.0",f"{list0[n]}的{list[n].name}受到了困惑效果。\n")
                else:
                    bufflist.append(Buff(B4.id,B4.name,n,B4.ef1,B4.ef2,B4.ef3,B4.ef4,2,0,0))
                    txt.insert("1.0",f"{list0[n]}的{list[n].name}受到了困惑效果。\n")
            else:
                if m == 0:
                    asahi1 = False
                elif m == 1:
                    asahi2 = False
        elif self.id == 13:
            list[m].spd = list[m].spd + 3
            if m == 0:
                asahi1 = True
                exp1 = exp1 + 0.05
                exr1 = exr1 + 0.15
                skp1 = f"P1的{P1.name}使用{Sk13.name},自身速度、暴击率、暴击伤害提升一级。\n"
            elif m == 1:
                asahi2 = True
                exp2 = exp2 + 0.05
                exr2 = exr2 + 0.15
                skp2 = f"P2的{P2.name}使用{Sk13.name},自身速度、暴击率、暴击伤害提升一级。\n"
        elif self.id == 14:
            if listh[m] == True:
                list[m].hp = int(list[m].hp + list[m].atk * 0.4 + 10)
                list[n].hp = int(list[n].hp - list[m].atk * 0.4 - 10)     #あさひ
                if m == 0:
                    skp1 = f"P1的{P1.name}使用{Sk14.name},窃取{int(list[m].atk*0.4+10)}点HP。\n"
                elif m == 1:
                    skp2 = f"P2的{P2.name}使用{Sk14.name},窃取{int(list[m].atk*0.4+10)}点HP。\n"
        elif self.id == 15:
            damage = damage + (listhp[m] - list[m].hp) / listhp[m] * listhp[n] * 0.5
        elif self.id == 17:
            if listh[m] == True:
                shp = list[m].hp
                list[m].hp = list[n].hp
                list[n].hp = shp
                if m == 0:
                    skp1 = f"P1的{P1.name}使用{Sk17.name},交换了双方HP值。\n"
                elif m == 1:
                    skp2 = f"P2的{P2.name}使用{Sk17.name},交换了双方HP值。\n"
        elif self.id == 18:
            if listh[m] == True:
                damage = damage * 0.5 + self.power/100 * (list[n].atk - list[n].defe) * 0.5
        elif self.id == 19:
            bufflist.append(Buff(B5.id,B5.name,n,B5.ef1,B5.ef2,B5.ef3,B5.ef4,2,0,0))
            if m == 0:
                P1.hp = int(P1.hp * 0.95)
                skp1 = f"P1的{P1.name}使用{Sk19.name},闪避下回合攻击，并失去{int(P1.hp*0.05)}点HP。\n"
            if m == 1:
                P2.hp = int(P2.hp * 0.95)
                skp2 = f"P2的{P2.name}使用{Sk19.name},闪避下回合攻击，并失去{int(P2.hp*0.05)}点HP。\n"
        elif self.id == 20:
            if listh[m] == True:
                bufflist.append(Buff(B3.id,B3.name,n,B3.ef1,B3.ef2,B3.ef3,B3.ef4,4,0,0))
        elif self.id == 21:
            if listh[m] == True:
                list[m].hp = int(list[m].hp * 0.5 + list[n].hp * 0.5)
                list[n].hp = list[m].hp
                if m == 0:
                    skp1 = f"P1的{P1.name}使用{Sk21.name},平均了双方HP值。\n"
                elif m == 1:
                    skp2 = f"P2的{P2.name}使用{Sk21.name},平均了双方HP值。\n"
        elif self.id == 22:
            list[m].hp = int(list[m].hp + (listhp[m] - list[m].hp) * 0.4)
            if m == 0:
                skp1 = f"P1的{P1.name}使用{Sk22.name},回复了{int((listhp[m]-list[m].hp)*0.4)}点HP。\n"
            if m == 1:
                skp2 = f"P2的{P2.name}使用{Sk22.name},回复了{int((listhp[m]-list[m].hp)*0.4)}点HP。\n"


        bar1['value'] = P1.hp/P1hp * 100
        bar2['value'] = P2.hp/P2hp * 100

        return int(damage)

######
class Buff:
    def __init__(self,id,name,player,ef1,ef2,ef3,ef4,time,satk,sdefe):
        self.id = id
        self.name = name
        self.player = player
        self.ef1 = ef1
        self.ef2 = ef2
        self.ef3 = ef3
        self.ef4 = ef4
        self.time = time
        self.satk = satk
        self.sdefe = sdefe     

######
def randomnum():
    a = 1
    while a*a > 0.01:
        a = random.gauss(0,0.04)
    return a
    
######
Sk0 = Skill(0,"",0)
Sk1 = Skill(1,"过肩摔",50)
Sk2 = Skill(2,"龙潜",120)
Sk3 = Skill(3,"传说力量",60)
Sk4 = Skill(4,"龙之力量",0)
Sk5 = Skill(5,"闪电旋风劈",150)
Sk6 = Skill(6,"强健体魄",0)
Sk7 = Skill(7,"追踪爆炸",120)
Sk8 = Skill(8,"焦比断头台",50)
Sk9 = Skill(9,"嘴遁",0)
Sk10 = Skill(10,"稀饭临头",40)
Sk11 = Skill(11,"盒武器",150)
Sk12 = Skill(12,"抽象艺术",10)
Sk13 = Skill(13,"卧薪尝胆",0)
Sk14 = Skill(14,"窃取",0)
Sk15 = Skill(15,"回光返照",50)
Sk16 = Skill(16,"倒打一耙",120)
Sk17 = Skill(17,"偷天换日",0)
Sk18 = Skill(18,"借刀杀人",120)
Sk19 = Skill(19,"折翼求生",0)
Sk20 = Skill(20,"绝命毒师",40)
Sk21 = Skill(21,"生命链接",0)
Sk22 = Skill(22,"秘密药剂",0)
Sk23 = Skill(23,"瞬间伤害II",140)


######
S99 = Servant("",330,150,45,35,[])
S0 = Servant("上古战龙",330,150,45,35,[Sk1,Sk2,Sk3,Sk4])
S1 = Servant("焦比",460,95,75,20,[Sk5,Sk6,Sk7,Sk8])
S2 = Servant("孙笑川",420,105,65,18,[Sk9,Sk10,Sk11,Sk12])
S3 = Servant("尹春红",260,175,15,40,[Sk13,Sk14,Sk15,Sk16])
S4 = Servant("溥仪",350,140,55,38,[Sk13,Sk17,Sk18,Sk19])
S5 = Servant("张勇",310,155,45,30,[Sk20,Sk21,Sk22,Sk23])
S6 = Servant("",330,150,45,35,[])


######

St = [S0,S1,S2,S3,S4,S5,S6]



#######
B1 = Buff(1,"烧伤",-1,0.08,False,1,0.75,0,0,0)
B2 = Buff(2,"眩晕",-1,0,True,1,1,0,0,0)
B3 = Buff(3,"中毒",-1,0.08,False,0.75,1,0,0,0)
B4 = Buff(4,"困惑",-1,0,True,1,0.8,0,0,0)
B5 = Buff(5,"无敌",-1,0,False,1,1,0,0,0)


########

rs1 = ""
rs2 = ""


#########

app = tk.Tk()
app.title("Pokemon Go!")
app.geometry("850x600+450+250")


#########
frame1 = tk.Frame(app)
frame2 = tk.Frame(app)

frame1.pack()
    
def clicked():

    global ps1,ps2,P1,P2,list,P1hp,P2hp,lbl3,lbl4,bar1,bar2,lbl1,lbl2,listhp

    ps1 = cbt1.get()
    ps2 = cbt2.get()

    for lks in St:
        if lks.name == ps1:
            pk1 = lks
        if lks.name == ps2:
            pk2 = lks

    P1 = Servant(pk1.name,pk1.hp,pk1.atk,pk1.defe,pk1.spd,pk1.skill)
    P2 = Servant(pk2.name,pk2.hp,pk2.atk,pk2.defe,pk2.spd,pk2.skill)

    P1hp = P1.hp
    P2hp = P2.hp

    listhp = [P1hp,P2hp]
    list = [P1,P2]

    bt11 = tk.Button(frame2,text = f"{P1.skill[0].name}", command = lambda: clicked11())
    bt11.grid(row=9, column=1)
    bt12 = tk.Button(frame2,text = f"{P1.skill[1].name}", command = lambda: clicked12())
    bt12.grid(row=9, column=2)
    bt13 = tk.Button(frame2,text = f"{P1.skill[2].name}", command = lambda: clicked13())
    bt13.grid(row=10, column=1)
    bt14 = tk.Button(frame2,text = f"{P1.skill[3].name}", command = lambda: clicked14())
    bt14.grid(row=10, column=2)
    bt21 = tk.Button(frame2,text = f"{P2.skill[0].name}", command = lambda: clicked21())
    bt21.grid(row=9, column=4)
    bt22 = tk.Button(frame2,text = f"{P2.skill[1].name}", command = lambda: clicked22())
    bt22.grid(row=9, column=5)
    bt23 = tk.Button(frame2,text = f"{P2.skill[2].name}", command = lambda: clicked23())
    bt23.grid(row=10, column=4)
    bt24 = tk.Button(frame2,text = f"{P2.skill[3].name}", command = lambda: clicked24())
    bt24.grid(row=10, column=5)

    lbl1 = tk.Label(frame2,text=f"P1  {P1.name}")
    lbl1.grid(row=6, column=1)
    lbl2 = tk.Label(frame2,text=f"P2  {P2.name}")
    lbl2.grid(row=6, column=4)
    lbl3 = tk.Label(frame2,text=f"{P1.hp}/{P1hp}")
    lbl3.grid(row=7, column=2)
    lbl4 = tk.Label(frame2,text=f"{P2.hp}/{P2hp}")
    lbl4.grid(row=7, column=5)

    bar1 = Progressbar(frame2, length=200)
    bar1.grid(row=6, column=2)
    bar2 = Progressbar(frame2, length=200)
    bar2.grid(row=6, column=5)

    bar1['value'] = 100
    bar2['value'] = 100
    style = ttk.Style()
    #style.theme_use('default')
    style.configure("yellow.Horizontal.TProgressbar", background='gold')
    style.configure("red.Horizontal.TProgressbar", background='red')

    lbg2 = tk.Label(frame2,text = "\n")
    lbg2.grid(row=12,column=3)

    bt00 = tk.Button(frame2,text = "回合结算", command = lambda: click00())
    bt00.grid(row=13, column=3)


    asahi = mryj()

    messagebox.showinfo("仆从选择", f"P1选择了{ps1}。\nP2选择了{ps2}。\n\n\n\n{asahi}")
    frame1.destroy()
    frame2.grid()

def clicked11():
    global rs1
    txt.insert('1.0', f'P1选择了技能{P1.skill[0].name}。\n')
    rs1 = P1.skill[0].name
    return rs1
def clicked12():
    global rs1
    txt.insert('1.0', f'P1选择了技能{P1.skill[1].name}。\n')
    rs1 = P1.skill[1].name
    return rs1
def clicked13():
    global rs1
    txt.insert('1.0', f'P1选择了技能{P1.skill[2].name}。\n')
    rs1 = P1.skill[2].name
    return rs1
def clicked14():
    global rs1
    txt.insert('1.0', f'P1选择了技能{P1.skill[3].name}。\n')
    rs1 = P1.skill[3].name
    return rs1

def clicked21():
    global rs2
    txt.insert('1.0', f'P2选择了技能{P2.skill[0].name}。\n')
    rs2 = P2.skill[0].name
    return rs2
def clicked22():
    global rs2
    txt.insert('1.0', f'P2选择了技能{P2.skill[1].name}。\n')
    rs2 = P2.skill[1].name
    return rs2
def clicked23():
    global rs2
    txt.insert('1.0', f'P2选择了技能{P2.skill[2].name}。\n')
    rs2 = P2.skill[2].name
    return rs2
def clicked24():
    global rs2
    txt.insert('1.0', f'P2选择了技能{P2.skill[3].name}。\n')
    rs2 = P2.skill[3].name
    return rs2


############




#######
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]   #あさひ

list0 = ["P1","P2"]

bufflist = []


damage = 0
flag = True

flag1 = True
flag2 = True



i = 1

#######
lb = tk.Label(frame1,text = "开始游戏！", font = (50))
lb.pack()


lb1 = tk.Label(frame1,text = "P1", font = (50))
lb1.pack()


cbt1 = ttk.Combobox(frame1)
cbt1["values"] = ("上古战龙","焦比","孙笑川","尹春红","溥仪","张勇")
cbt1.current(0)
cbt1.pack()

lb2 = tk.Label(frame1,text = "P2", font = (50))
lb2.pack()


cbt2 = ttk.Combobox(frame1)
cbt2["values"] = ("上古战龙","焦比","孙笑川","尹春红","溥仪","张勇")
cbt2.current(0)
cbt2.pack()

m2 = ""
n2 = ""

bt = tk.Button(frame1,text = "选择", command = lambda: clicked())
bt.pack()

for ptsr in range(1,10):
    lbgs2 = tk.Label(frame1,text = "\n")
    lbgs2.pack()
lbsg = tk.Label(frame1,text = "あさひ小姐为您恭敬奉上，请愉快体验")
lbsg.pack()

ps1 = cbt1.get()
ps2 = cbt2.get()

for lks in St:
    if lks.name == ps1:
        pk1 = lks
    if lks.name == ps2:
        pk2 = lks

P1 = Servant(pk1.name,pk1.hp,pk1.atk,pk1.defe,pk1.spd,pk1.skill)
P2 = Servant(pk2.name,pk2.hp,pk2.atk,pk2.defe,pk2.spd,pk2.skill)

###########

lb = tk.Label(frame2,text = "第1回合", font = (50))
lb.grid(row=1,column=3)

for pts in range(1,5):
    lbg2 = tk.Label(frame2,text = "\n")
    lbg2.grid(row=pts+13,column=3)

lbg = tk.Label(frame2,text = "あさひ小姐为您恭敬奉上，请愉快体验")
lbg.grid(row=18,column=3)


txt = scrolledtext.ScrolledText(frame2, width=40, height=10)    #あさひ

txt.grid(row=2,column=3)

list = [P1,P2]

list1 = [pk1,pk2]

effect1 = ""
effect2 = ""
effect3 = ""
effect4 = ""

P1atk = pk1.atk
P2atk = pk2.atk
P1defe = pk1.defe
P2defe = pk2.defe

t1 = 0
t2 = 0

#app.protocol("WM_DELETE_WINDOW", quit)
######

def click00():

    global t1,t2,flag1,flag2,i,bar1,bar2,lphs1,lphs2,asahi1,asahi2,effect1,effect2,exf1,exf2,exr1,exr2,exp1,exp2
    global skp1,skp2,sp1,sp2,p1atk,p2atk,p1defe,p2defe,P1atk,P2atk,P1defe,P2defe,sb1,sb2    #あさひ

    p1atk = 1
    p2atk = 1
    p1defe = 1
    p2defe = 1
    P1atk = P1.atk
    P2atk = P2.atk
    P1defe = P1.defe
    P2defe = P2.defe

    if sb1 == True:
        asahi1 = False
    if sb2 == True:
        asahi2 = False

    for buffse in bufflist:
        if buffse.ef2 == True:
            if buffse.player == 0:
                flag1 = False
                effect1 = buffse.name
            else:
                flag2 = False
                effect2 = buffse.name
        
        if buffse.ef3 != 1:
            if buffse.player == 0:
                if buffse.ef3 < p1atk:
                    p1atk = buffse.ef3
            else:
                if buffse.ef3 < p2atk:
                    p2atk = buffse.ef3

        if buffse.ef4 != 1:
            if buffse.player == 0:
                if buffse.ef4 < p1defe:
                    p1defe = buffse.ef3
            else:
                if buffse.ef4 < p2defe:
                    p2defe = buffse.ef3
        
        if buffse.id == 5:
            if buffse.player == 0:
                asahi1 = False
            else:
                asahi2 = False

    P1.atk = P1.atk * p1atk
    P2.atk = P2.atk * p2atk
    P1.defe = P1.defe * p1defe
    P2.defe = P2.defe * p2defe

    txt.insert("1.0","\n")
    txt.insert("1.0","\n")

    txt.insert("1.0",f"第{i}回合。\n")

    if exr1 > 4:
        exr1 = 4
    if exr2 > 4:
        exr2 = 4

    if flag1 == True:
        for sk1 in P1.skill:
            if sk1.name == rs1:
                t1 = sk1.exe(0,1)
    elif flag1 == False:
        t1 = 0

    if flag2 == True:
        for sk2 in P2.skill:
            if sk2.name == rs2:
                t2 = sk2.exe(1,0)
    if flag2 == False:
        t2 = 0

    if random.random() < exp1:
        t1 = int(t1*exr1)
        exf1 = "暴击了，"
    if random.random() < exp2:
        t2 = int(t2*exr2)
        exf2 = "暴击了，"
  
    if t1 < 0:
        t1 = 1
    if t2 < 0:
        t2 = 1
        
    if P1.hp > P1hp:
        P1.hp = P1hp
    if P2.hp > P2hp:
        P2.hp = P2hp

    if asahi1 == False:
        t1 = 0
    if asahi2 == False:
        t2 = 0

    tp2 = randomnum()
    t2 = int( t2 * ( 1 + tp2 )) 
    P1.hp = P1.hp - t2

    tp1 = randomnum()
    t1 = int( t1 * ( 1 + tp1 ))
    P2.hp = P2.hp - t1

    if P1.atk > 2.5 * pk1.atk:
        P1.atk = pk1.atk
    if P2.atk > 2.5 * pk2.atk:
        P2.atk = pk2.atk

    if P1.defe > 2 * pk1.defe:
        P1.defe = pk1.defe
    if P2.defe > 2 * pk2.defe:
        P2.defe = pk2.defe
    
    if P1.hp < 0:
        P1.hp = 0
    if P2.hp < 0:
        P2.hp = 0

    if flag1 == True:
        if asahi1 == True:
            if skp1 != "":
                txt.insert("1.0",f"{skp1}")
                skp1 = ""
            elif sp1 != "":
                txt.insert("1.0",f"{sp1}并对敌方造成了{t1}点伤害。\n")
                sp1 = ""
            else:
               txt.insert("1.0",f"P1的{P1.name}使用了技能{rs1},{exf1}造成了{t1}点伤害。\n")
        else:
            txt.insert("1.0",f"P1的{P1.name}的攻击被闪避了。\n")
    elif flag1 == False:
        txt.insert("1.0",f"P1本回合由于{effect1}效果无法行动。\n")

    if flag2 == True:
        if asahi2 == True:
            if skp2 != "":
                txt.insert("1.0",f"{skp2}")
                skp2 = ""
            elif sp2 != "":
                txt.insert("1.0",f"{sp2}并对敌方造成了{t2}点伤害。\n")
                sp2 = ""
            else:
               txt.insert("1.0",f"P2的{P2.name}使用了技能{rs2},{exf2}造成了{t2}点伤害。\n")
        else:
            txt.insert("1.0",f"P2的{P2.name}的攻击被闪避了。\n")
    elif flag2 == False:
        txt.insert("1.0",f"P2本回合由于{effect2}效果无法行动。\n")

    asahi1 = True
    asahi2 = True

    bar1['value'] = P1.hp/P1hp * 100
    bar2['value'] = P2.hp/P2hp * 100

    rfs = 0
    for bufx in bufflist:
        rft = 0
        for buft in bufflist:
            if buft.id == bufx.id and buft.player == bufx.player and buft != bufx:
                bufflist.pop(rfs)
                rfs = rfs - 1
                break
            rft = rft + 1
        rfs = rfs + 1
      
    for buffs in bufflist:
        buffs.time = buffs.time - 1
        if buffs.player == 0:
            if buffs.ef1 != 0:
                P1.hp = int(P1.hp * (1 - buffs.ef1))
                txt.insert("1.0",f"{buffs.name}效果造成P1的{P1.name}失去{int(P1.hp*buffs.ef1)}点HP。\n")
        elif buffs.player == 1:
            if buffs.ef1 != 0:
                P2.hp = int(P2.hp * (1 - buffs.ef1))
                txt.insert("1.0",f"{buffs.name}效果造成P2的{P2.name}失去{int(P2.hp*buffs.ef1)}点HP。\n")

    rfs = 0
    for bufe in bufflist:
        if bufe.time == 0:
            bufflist.pop(rfs)
            rfs = rfs - 1
        rfs = rfs + 1

    txt.insert("1.0",f"P1剩余{P1.hp}/{P1hp}点HP。\n")
    txt.insert("1.0",f"P2剩余{P2.hp}/{P2hp}点HP。\n")

    bar1['value'] = P1.hp/P1hp * 100
    bar2['value'] = P2.hp/P2hp * 100

    txt.insert("1.0","\n")
    txt.insert("1.0","\n")

    exf1 = ""
    exf2 = ""

    sb1 = False
    sb2 = False
#    frame2.update()
#    time.sleep(0.5)



#    if P1.hp/P1hp <= 0.4 and P1.hp/P1hp > 0.2:    
#        bar1 = Progressbar(frame2, length=200, style='yellow.Horizontal.TProgressbar') #あさひ
#    elif P1.hp/P1hp <= 0.2:        
#        bar1 = Progressbar(frame2, length=200, style='red.Horizontal.TProgressbar')
#        
#    if P2.hp/P2hp <= 0.4 and P2.hp/P2hp > 0.2:
#        bar2 = Progressbar(frame2, length=200, style='yellow.Horizontal.TProgressbar')
#    elif P2.hp/P2hp <= 0.2:
#        bar2 = Progressbar(frame2, length=200, style='red.Horizontal.TProgressbar')

    i = i + 1

    flag1 = True
    flag2 = True
    effect1 = ""
    effect2 = ""

    P1.atk = P1atk
    P2.atk = P2atk
    P1.defe = P1defe
    P2.defe = P2defe

    lb.configure(text=f"第{i}回合")
    lbl3.configure(text=f"{P1.hp}/{P1hp}")
    lbl4.configure(text=f"{P2.hp}/{P2hp}")

    if P1.hp * P2.hp == 0:

        if P1.hp > 0 and P2.hp <= 0:
            txt.insert("1.0","P1胜利。\n")
            messagebox.showinfo("游戏结束", f"P1胜利。\n")
        elif P1.hp <= 0 and P2.hp >0:
            txt.insert("1.0","P2胜利。\n")
            messagebox.showinfo("游戏结束", f"P2胜利。\n")
        else:
            txt.insert("1.0","平局。\n")
            messagebox.showinfo("游戏结束", f"平局。\n")    #あさひ



######



while P1.hp > 0 and P2.hp > 0 :

    rs1 = ""
    rs2 = ""

    tk.mainloop()
#    txt.delete(1.0, 'end')



