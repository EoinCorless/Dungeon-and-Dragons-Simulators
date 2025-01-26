#TO DO/FUTURE FEATURES
#LIGHT DEBUGGING
#UPDATE ADVANTAGE/DISADVANTAGE, THANKS FOR THE REMINDER TYMEK
#IMPLEMENT UPCASTING SPELLS, THANKS FOR THE IDEA TY
#IMPLEMENT THE REST OF THE DISADVANTAGES FOR RECKLESS ATTACK
#PERCENT COMPLETE METER FOR WHEN YOU SIMULATE A LARGE AMOUNT OF COMBAT
#TIDY UP SPELL SYSTEM (Eg list by spell name, no by spell caster)
#TIDY UP STAT STORAGE (Eg NOT ARRAYS)
#Ability to preview character abilities? (plus description)

import math
import random
import time
#CLASSES
#Barbarian,Bard,Cleric,Druid,Fighter,Monk,Paladin,Ranger,Rogue,Sorcerer,Warlock,Wizard,Artificer,Other (Such as Beasts) -->14 Classes
#       Ba,B,C,D,F,M,P,R,Ro,S,Wa,Wi,A,B
ClassID=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
LV1ClassHitDice=[12,8,8,8,10,8,10,10,8,6,8,6,8,0]
AVGClassHitDice=[7,5,5,5,6,5,6,6,5,4,5,4,5,0]
#Define Character Stats
#Array Order: Grugg,Clugg,Alice,Alice2,Petrov,Valdos,Bark
NameValues=["Grugg","Clugg","Alice (BH)","Alice (MM)","Petrov","Valdos","Bark (IK)","Bark (TW)","Tortimer","Tyrannosaurus Rex"]
NumberOfChar=len(NameValues)
HPValues=[22,22,10,10,14,15,28,28,42,136]
PrimaryClassValues=[0,0,11,11,11,5,3,3,4,13]
LevelValues=[2,2,2,2,2,2,2,2,4,8]
ACValues=[16,16,12,12,16,15,15,15,19,13]
InitValues=[2,2,2,2,2,3,2,2,4,0]
StrengthValues=[4,4,0,0,-1,0,1,1,0,7]
DexValues=[2,2,2,2,2,3,2,2,4,0]
ConstValues=[4,4,0,0,0,1,3,3,3,4]
SpellSlot1Values=[0,0,3,3,3,0,3,3,0,0]
KiValues=[0,0,0,0,0,2,0,0,0,0]
RageValues=[0,0,0,0,0,0,0,0,0,0]
RecklessValues=[1,1,0,0,0,0,0,0,0,0]
Name_char1 = "PLACEHOLDER1"
Name_char2 = "PLACEHOLDER2"
HP_char1 = int(0)
HP_char2 = int(0)
AC_char1 = int(0)
AC_char2 = int(0)
Init_char1 = int(0)
Init_char2 = int(0)
TurnOrder = int(0)
Player1Skip = int(0)
Attack_char1 = int(0)
Attack_char2 = int(0)
SpellSlot1_char1 = int(0)
SpellSlot1_char2 = int(0)
HitChance = int(0)
HitDamage = int(0)
Wins_char1 = int(0)
Wins_char2 = int(0)
InitWins_char1 = int(0)
InitWins_char2 = int(0)
TotalGames = int(0)
#These are the BONUS TO ROLLS not full stat
Strength_char1 = int(0)
Strength_char2 = int(0)
Dex_char1 = int(0)
Dex_char2 = int(0)
Const_char1 = int(0)
Const_char2 = int(0)
TurnTaken1 = False
TurnTaken2 = False

#Sets Character ID
CharExit1 = False
i=int(1)
while(CharExit1 == False):
    print("Please select character 1!")
    while(i<=NumberOfChar):
        j=str(i)
        NamePrint=NameValues[i-1]
        print(j+": "+NamePrint)
        i=i+1
    try:
        Character1ID=int(input(":"))
        if (Character1ID <= NumberOfChar and Character1ID > 0):
            Character1ID = int(Character1ID) - 1
            CharExit1 = True
        else:
            print("Invalid Value!")
    except ValueError:(
        print("Invalid! (Input was not an Integer)"))


CharExit2 = False
i=int(1)
while(CharExit2 == False):
    print("Please select character 2!")
    while(i<=NumberOfChar):
        j=str(i)
        NamePrint=NameValues[i-1]
        print(j+": "+NamePrint)
        i=i+1
    try:
        Character2ID=int(input(":"))
        if (Character2ID <= NumberOfChar and Character2ID > 0):
            Character2ID = int(Character2ID) - 1
            CharExit2 = True
        else:
            print("Invalid Value!")
    except ValueError:(
        print("Invalid! (Input was not an Integer)"))


#Sets Character Stats
Name_char1 = NameValues[Character1ID]
Name_char2 = NameValues[Character2ID]
Level_char1 = LevelValues[Character1ID]
Level_char2 = LevelValues[Character2ID]
PrimClass_char1 = PrimaryClassValues[Character1ID]
PrimClass_char2 = PrimaryClassValues[Character2ID]
HP_char1 = HPValues[Character1ID]
HP_char2 = HPValues[Character2ID]
HPreset_char1 = HP_char1
HPreset_char2 = HP_char2
AC_char1 = ACValues[Character1ID]
AC_char2 = ACValues[Character2ID]
Init_char1 = InitValues[Character1ID]
Init_char2 = InitValues[Character2ID]
Strength_char1 = StrengthValues[Character1ID]
Strength_char2 = StrengthValues[Character2ID]
Dex_char1 = DexValues[Character1ID]
Dex_char2 = DexValues[Character2ID]
Const_char1 = ConstValues[Character1ID]
Const_char2 = ConstValues[Character2ID]
SpellSlot1_char1 = SpellSlot1Values[Character1ID]
SpellSlot1_char2 = SpellSlot1Values[Character2ID]
Ki_char1 = KiValues[Character1ID]
Ki_char2 = KiValues[Character2ID]
Rage_char1 = RageValues[Character1ID]
Rage_char2 = RageValues[Character2ID]
Reckless_char1 = RecklessValues[Character1ID]
Reckless_char2 = RecklessValues[Character2ID]

AutoLVRule=input("Do you want to Auto Level your characters? (Y/N)")
if(AutoLVRule=="Y" or AutoLVRule=="y"):
    print(Name_char1,"is level",Level_char1,"\n"+Name_char2+" is level",Level_char2)
    if(Level_char1 == Level_char2):
        print("There are no chages to be made!")
    elif(Level_char1 > Level_char2):
        LevelGap=Level_char1-Level_char2
        print("LevelGap =",LevelGap)
        HPpre_char2 = HPreset_char2
        HPreset_char2=HPreset_char2+((AVGClassHitDice[PrimClass_char2]+Const_char2)*LevelGap)
        HP_char2=HPreset_char2
        LevelPre_char2=Level_char2
        Level_char2 = Level_char2 + LevelGap
        print(Name_char2+"'s HP raised from",HPpre_char2,"to their new HP of",HPreset_char2)
        print(Name_char2 + "'s Level raised from", LevelPre_char2, "to their new Level of", Level_char2)

    elif (Level_char2 > Level_char1):
        LevelGap = Level_char2 - Level_char1
        print("LevelGap =", LevelGap)
        HPpre_char1 = HPreset_char1
        HPreset_char1 = HPreset_char1 + ((AVGClassHitDice[PrimClass_char1] + Const_char1) * LevelGap)
        HP_char1 = HPreset_char1
        LevelPre_char1 = Level_char1
        Level_char1 = Level_char1 + LevelGap
        print(Name_char1 + "'s HP raised from", HPpre_char1, "to their new HP of", HPreset_char1)
        print(Name_char1 + "'s Level raised from", LevelPre_char1, "to their new Level of", Level_char1)


#Sets Print Rules
PrintExit=False
while(PrintExit==False):
    PrintInput = input("Do you want battle updates? Y/N:")
    if(PrintInput == "Y" or PrintInput == "y"):
        PrintRule = True
        PrintExit = True
    elif (PrintInput == "N" or PrintInput == "n"):
        PrintRule = False
        PrintExit = True
    else:
        print("Error! Please only use Y/N")

SimAmountExit = False
while(SimAmountExit == False):
    try:
        SimGames=int(input("How many games do you want to simulate?:"))
        print("Input Accepted!")
        SimAmountExit = True
    except ValueError:(
        print("Invalid! (Input was not an Integer)"))

#ATTACKS-->

def ACModifiers(DefID,OppAC):
    #DefensiveDuelist
    if(DefID == 8):
        OppAC = OppAC+2
        if (PrintRule == True):
            print(NameValues[DefID],"defensively duels! Their AC is now",OppAC)
        return (OppAC);
    else:
        return (OppAC);

def HitChanceRoller(AtkID,ATKReck):
    if (ATKReck == 1):
        HitChanceRoll1 = random.randint(1, 20)
        HitChanceRoll2 = random.randint(1, 20)
        if (PrintRule == True):
            print(NameValues[AtkID], "attacks with Advantage!")
            print("D20 ROLL 1", HitChanceRoll1, "\nD20 ROLL 2", HitChanceRoll2)
        if (HitChanceRoll1 >= HitChanceRoll2):
            HitChanceRoll = HitChanceRoll1
        elif (HitChanceRoll1 < HitChanceRoll2):
            HitChanceRoll = HitChanceRoll2
    elif (DEFReck == 1):
        if (TurnTaken == True):
            HitChanceRoll1 = random.randint(1, 20)
            HitChanceRoll2 = random.randint(1, 20)
            if (PrintRule == True):
                print(NameValues[DefID], "is hit with Disdvantage!")
                print("D20 ROLL 1", HitChanceRoll1, "\nD20 ROLL 2", HitChanceRoll2)
            if (HitChanceRoll1 >= HitChanceRoll2):
                HitChanceRoll = HitChanceRoll1
            elif (HitChanceRoll1 < HitChanceRoll2):
                HitChanceRoll = HitChanceRoll2


    return(HitChanceRoll);


#ATTACKS-->

def TRexBite(Strength,AttackerName,OppAC,AtkRage,DefRage,DefID,TurnTaken,ATKReck,DEFReck):
    OppAC=ACModifiers(DefID,OppAC)

    if(ATKReck == 1):
        HitChanceRoll1 = random.randint(1, 20)
        HitChanceRoll2 = random.randint(1, 20)
        if(PrintRule == True):
            print(AttackerName,"attacks with Advantage!")
            print("D20 ROLL 1",HitChanceRoll1,"\nD20 ROLL 2",HitChanceRoll2)
        if(HitChanceRoll1>=HitChanceRoll2):
            HitChanceRoll=HitChanceRoll1
        elif(HitChanceRoll1<HitChanceRoll2):
            HitChanceRoll=HitChanceRoll2

    elif (DEFReck == 1):
        if(TurnTaken == True):
            HitChanceRoll1 = random.randint(1, 20)
            HitChanceRoll2 = random.randint(1, 20)
            if (PrintRule == True):
                print(NameValues[DefID], "is hit with Disdvantage!")
                print("D20 ROLL 1", HitChanceRoll1, "\nD20 ROLL 2", HitChanceRoll2)
            if (HitChanceRoll1 >= HitChanceRoll2):
                HitChanceRoll = HitChanceRoll1
            elif (HitChanceRoll1 < HitChanceRoll2):
                HitChanceRoll = HitChanceRoll2

        else:
            HitChanceRoll = random.randint(1, 20)

    else:
        HitChanceRoll=random.randint(1,20)

    if(PrintRule == True):
        print("Hit Chance Roll",HitChanceRoll)
    HitChance=HitChanceRoll+10
    if(PrintRule == True):
        print("Chance to hit for "+AttackerName+"'s attack was",HitChance)
    if (OppAC <= HitChance):
        if(HitChanceRoll == int(20)):
            Roll1 = random.randint(1, 12)
            Roll2 = random.randint(1, 12)
            Roll3 = random.randint(1, 12)
            Roll4 = random.randint(1, 12)
            Roll5 = random.randint(1, 12)
            Roll6 = random.randint(1, 12)
            Roll7 = random.randint(1, 12)
            Roll8 = random.randint(1, 12)
            if(AtkRage==int(1)):
                HitDamage = Roll1+Roll2+Roll3+Roll4+Roll5+Roll6+Roll7+Roll8+7
                if(DefRage==int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            else:
                HitDamage = Roll1+Roll2+Roll3+Roll4+Roll5+Roll6+Roll7+Roll8+Strength
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            if(PrintRule == True):
                print("Critical Hit! Dealing",HitDamage,"Damage! \nRoll1:",Roll1," \nRoll2:",Roll2," \nRoll3:", Roll3," \nRoll4:", Roll4,"\nRoll5:",Roll5," \nRoll6:",Roll6," \nRoll7:", Roll7," \nRoll8:", Roll8)
            return (HitDamage);
        else:
            Roll1=random.randint(1, 12)
            Roll2=random.randint(1, 12)
            Roll3 = random.randint(1, 12)
            Roll4 = random.randint(1, 12)
            if (AtkRage == int(1)):
                HitDamage = Roll1+Roll2+Roll3+Roll4+7
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            else:
                HitDamage = Roll1+Roll2+Roll3+Roll4+7
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            if(PrintRule == True):
                print("Attack Hit! Dealing",HitDamage,"Damage! \nRoll1:",Roll1," \nRoll2:",Roll2," \nRoll3:", Roll3," \nRoll4:", Roll4)
            return(HitDamage);
    elif(OppAC>HitChance):
        if (PrintRule == True):
            print("The Attack Missed.")
        HitDamage = int(0)
        return (HitDamage);
def Meele2D6(Strength,AttackerName,OppAC,AtkRage,DefRage,DefID,TurnTaken,ATKReck,DEFReck):
    if (DefID == 8):
        OppAC = OppAC + 2
        if (PrintRule == True):
            print(NameValues[DefID], "defensively duels! Their AC is now", OppAC)

    if (ATKReck == 1):
        HitChanceRoll1 = random.randint(1, 20)
        HitChanceRoll2 = random.randint(1, 20)
        if (PrintRule == True):
            print(AttackerName, "attacks with Advantage!")
            print("D20 ROLL 1", HitChanceRoll1, "\nD20 ROLL 2", HitChanceRoll2)
        if (HitChanceRoll1 >= HitChanceRoll2):
            HitChanceRoll = HitChanceRoll1
        elif (HitChanceRoll1 < HitChanceRoll2):
            HitChanceRoll = HitChanceRoll2

    elif (DEFReck == 1):
        if (TurnTaken == True):
            HitChanceRoll1 = random.randint(1, 20)
            HitChanceRoll2 = random.randint(1, 20)
            if (PrintRule == True):
                print(NameValues[DefID], "is hit with Disdvantage!")
                print("D20 ROLL 1", HitChanceRoll1, "\nD20 ROLL 2", HitChanceRoll2)
            if (HitChanceRoll1 >= HitChanceRoll2):
                HitChanceRoll = HitChanceRoll1
            elif (HitChanceRoll1 < HitChanceRoll2):
                HitChanceRoll = HitChanceRoll2

        else:
            HitChanceRoll = random.randint(1, 20)

    else:
        HitChanceRoll = random.randint(1, 20)

    if(PrintRule == True):
        print("Hit Chance Roll",HitChanceRoll)
    HitChance=HitChanceRoll+Strength+2
    if(PrintRule == True):
        print("Chance to hit for "+AttackerName+"'s attack was",HitChance)
    if (OppAC <= HitChance):
        if(HitChanceRoll == int(20)):
            Roll1 = random.randint(1, 6)
            Roll2 = random.randint(1, 6)
            Roll3 = random.randint(1, 6)
            Roll4 = random.randint(1, 6)
            if(AtkRage==int(1)):
                HitDamage = Roll1+Roll2+Roll3+Roll4+Strength+2
                if(DefRage==int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            else:
                HitDamage = Roll1+Roll2+Roll3+Roll4+Strength
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            if(PrintRule == True):
                print("Critical Hit! Dealing",HitDamage,"Damage! Roll1:",Roll1," Roll2:",Roll2," Roll3:", Roll3," Roll4:", Roll4)
            return (HitDamage);
        else:
            Roll1=random.randint(1, 6)
            Roll2=random.randint(1, 6)
            if (AtkRage == int(1)):
                HitDamage = Roll1+Roll2+Strength+2
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            else:
                HitDamage =Roll1+Roll2+Strength
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            if(PrintRule == True):
                print("Attack Hit! Dealing",HitDamage,"Damage! Roll1:",Roll1," Roll2:",Roll2)
            return(HitDamage);
    elif(OppAC>HitChance):
        if (PrintRule == True):
            print("The Attack Missed.")
        HitDamage = int(0)
        return (HitDamage);

def DexMeele1D8(Dexterity,AttackerName,OppAC,AtkRage,DefRage,DefID,TurnTaken,ATKReck,DEFReck):
    if (DefID == 8):
        OppAC = OppAC + 2
        if (PrintRule == True):
            print(NameValues[DefID], "defensively duels! Their AC is now", OppAC)

    if (ATKReck == 1):
        HitChanceRoll1 = random.randint(1, 20)
        HitChanceRoll2 = random.randint(1, 20)
        if (PrintRule == True):
            print(AttackerName, "attacks with Advantage!")
            print("D20 ROLL 1", HitChanceRoll1, "\nD20 ROLL 2", HitChanceRoll2)
        if (HitChanceRoll1 >= HitChanceRoll2):
            HitChanceRoll = HitChanceRoll1
        elif (HitChanceRoll1 < HitChanceRoll2):
            HitChanceRoll = HitChanceRoll2

    elif (DEFReck == 1):
        if (TurnTaken == True):
            HitChanceRoll1 = random.randint(1, 20)
            HitChanceRoll2 = random.randint(1, 20)
            if (PrintRule == True):
                print(NameValues[DefID], "is hit with Disdvantage!")
                print("D20 ROLL 1", HitChanceRoll1, "\nD20 ROLL 2", HitChanceRoll2)
            if (HitChanceRoll1 >= HitChanceRoll2):
                HitChanceRoll = HitChanceRoll1
            elif (HitChanceRoll1 < HitChanceRoll2):
                HitChanceRoll = HitChanceRoll2

        else:
            HitChanceRoll = random.randint(1, 20)

    else:
        HitChanceRoll = random.randint(1, 20)

    HitChance=HitChanceRoll+Dexterity+2
    if(PrintRule == True):
        print("Chance to hit for "+AttackerName+"'s attack was",HitChance)
    if (OppAC <= HitChance):
        if(HitChanceRoll == int(20)):
            Roll1 = random.randint(1, 8)
            Roll2 = random.randint(1, 8)
            if(AtkRage==int(1)):
                HitDamage = Roll1+Roll2+Dexterity+2
                if(DefRage==int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            else:
                HitDamage = Roll1+Roll2+Dexterity
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            if(PrintRule == True):
                print("Critical Hit! Dealing",HitDamage,"Damage! Roll1:",Roll1," Roll2:",Roll2)
            return (HitDamage);
        else:
            Roll1=random.randint(1, 8)
            if (AtkRage == int(1)):
                HitDamage = Roll1+Dexterity+2
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            else:
                HitDamage =Roll1+Dexterity
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            if(PrintRule == True):
                print("Attack Hit! Dealing",HitDamage,"Damage! Roll1:",Roll1)
            return(HitDamage);
    elif(OppAC>HitChance):
        if (PrintRule == True):
            print("The Attack Missed.")
        HitDamage = int(0)
        return (HitDamage);


#GREAT WEAPON MASTER NEEDS UPDATING
def GreatWeaponMaster(Strength,AttackerName,OppAC,AtkRage,DefRage):
    HitChanceRoll=random.randint(1,20)
    HitChance=HitChanceRoll+Strength+2-5
    if(PrintRule == True):
        print("Chance to hit for "+AttackerName+"'s attack was",HitChance)
    if (OppAC <= HitChance):
        if(HitChanceRoll == int(20)):
            Roll1 = random.randint(1, 6)
            Roll2 = random.randint(1, 6)
            Roll3 = random.randint(1, 6)
            Roll4 = random.randint(1, 6)
            if(AtkRage==int(1)):
                HitDamage = Roll1+Roll2+Roll3+Roll4+Strength+2+10
                if(DefRage==int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)+10
                    print("Damage Resisted")
            else:
                HitDamage = Roll1+Roll2+Roll3+Roll4+Strength+10
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)+10
                    print("Damage Resisted")
            if(PrintRule == True):
                print("Critical Hit! Dealing",HitDamage,"Damage! Roll1:",Roll1," Roll2:",Roll2," Roll3:", Roll3," Roll4:", Roll4)
            return (HitDamage);
        else:
            Roll1=random.randint(1, 6)
            Roll2=random.randint(1, 6)
            if (AtkRage == int(1)):
                HitDamage = Roll1+Roll2+Strength+2
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            else:
                HitDamage =Roll1+Roll2+Strength
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            if(PrintRule == True):
                print("Attack Hit! Dealing",HitDamage,"Damage! Roll1:",Roll1," Roll2:",Roll2)
            return(HitDamage);
    elif(OppAC>HitChance):
        if (PrintRule == True):
            print("The Attack Missed.")
        HitDamage = int(0)
        return (HitDamage);

def AliceSpellsLV1(DefenderName,OppDex,DefID):
    #Burning Hands
    if(DefID == 0 or DefID == 1):
        DexRoll1=random.randint(1, 20)
        DexRoll2 = random.randint(1, 20)
        if(PrintRule  == True):
            print(DefenderName, "senses danger!","\nDex Roll1:",DexRoll1,"\nDex Roll2:",DexRoll2)
        if(DexRoll1>=DexRoll2):
            DexSavingThrow= DexRoll1 + OppDex
        elif(DexRoll2>DexRoll1):
            DexSavingThrow = DexRoll1 + OppDex
    else:
        DexRoll = random.randint(1, 20)
        if (PrintRule == True):
            print("Dex Roll was",DexRoll)
        DexSavingThrow = DexRoll + OppDex

    if (PrintRule == True):
        print("Dex Saving Throw for "+DefenderName+" was",DexSavingThrow)
    if(DexSavingThrow<=15):
        Roll1 = random.randint(1, 6)
        Roll2 = random.randint(1, 6)
        Roll3 = random.randint(1, 6)
        HitDamage=Roll1+Roll2+Roll3
        if(PrintRule == True):
            print("Burning Hands Hit, and the target failed the DexSave! Dealing", HitDamage, "Damage! Roll1:", Roll1, "Roll2:", Roll2,"Roll3:", Roll3)
    if(DexSavingThrow>15):
        Roll1 = random.randint(1, 6)
        Roll2 = random.randint(1, 6)
        Roll3 = random.randint(1, 6)
        HitDamage = (Roll1 + Roll2 + Roll3)/2
        HitDamage = math.floor(HitDamage)
        if (PrintRule == True):
            print("Burning Hands Hit, but the target succeeded the DexSave! Dealing", HitDamage, " Damage! Roll1:", Roll1, "Roll2:", Roll2, "Roll3:",Roll3)
    return (HitDamage);

def AliceSpellsLV1ALT():
    #Magic Missile
    Roll1 = random.randint(1, 4)
    Roll2 = random.randint(1, 4)
    Roll3 = random.randint(1, 4)
    HitDamage=Roll1+Roll2+Roll3+3
    if(PrintRule == True):
        print("Magic Missile Hit! Dealing", HitDamage, "Damage! Roll1:", Roll1, "Roll2:", Roll2,"Roll3:", Roll3)
    return (HitDamage);

def ChillTouchCantrip(AttackerName,OppAC):
    #Chill Touch
    HitChanceRoll=random.randint(1,20)
    HitChance=HitChanceRoll+7
    if(PrintRule == True):
        print("Chance to hit for "+AttackerName+"'s attack was",HitChance)
    if (OppAC <= HitChance):
        Roll1=random.randint(1, 8)
        HitDamage =Roll1
        if(PrintRule == True):
            print("Chill Touch Hit! Dealing",HitDamage," Damage! Roll1:",Roll1)
        return(HitDamage);
    elif(OppAC>HitChance):
        if (PrintRule == True):
            print("Chill Touch Missed.")
        HitDamage = int(0)
        return (HitDamage);

def PetrovSpellsLV1(AttackerName,OppAC):
    #Inflict Wounds
    HitChanceRoll = random.randint(1, 20)
    HitChance = HitChanceRoll + 5
    if (PrintRule == True):
        print("Chance to hit for " + AttackerName + "'s attack was", HitChance)
    if (OppAC <= HitChance):
        Roll1 = random.randint(1, 10)
        Roll2 = random.randint(1, 10)
        Roll3 = random.randint(1, 10)
        HitDamage = Roll1 + Roll2 + Roll3
        if (PrintRule == True):
            print("Attack Hit! Dealing", HitDamage, "Damage! Roll1:",Roll1,"Roll2:",Roll2,"Roll3:",Roll3)
        return (HitDamage);
    elif (OppAC > HitChance):
        if (PrintRule == True):
            print("The Attack Missed.")
        HitDamage = int(0)
        return (HitDamage);

def PetrovSpellsCantrip(DefenderName,OppDex,DefID):
    #Sacred Flame
    if (DefID == 0 or DefID == 1):
        DexRoll1 = random.randint(1, 20)
        DexRoll2 = random.randint(1, 20)
        if (PrintRule == True):
            print(DefenderName, "senses danger!", "\nDex Roll1:", DexRoll1, "\nDex Roll2:", DexRoll2)
        if (DexRoll1 >= DexRoll2):
            DexSavingThrow = DexRoll1 + OppDex
        elif (DexRoll2 > DexRoll1):
            DexSavingThrow = DexRoll1 + OppDex
    else:
        DexRoll = random.randint(1, 20)
        if (PrintRule == True):
            print("Dex Roll was", DexRoll)
        DexSavingThrow = DexRoll + OppDex

    if (PrintRule == True):
        print("Dex Saving Throw for " + DefenderName + " was", DexSavingThrow)
    if (DexSavingThrow <= 13):
        Roll1 = random.randint(1, 8)
        HitDamage = Roll1
        if (PrintRule == True):
            print("Sacred Flame Hit, and the target failed the DexSave! Dealing", HitDamage, "Damage! Roll1:", Roll1)
    if (DexSavingThrow > 13):
        HitDamage = int(0)
        if (PrintRule == True):
            print("Sacred Flame missed, because the target succeeded the DexSave")
    return (HitDamage);

def ValdosPunch(Dexterity,AttackerName,OppAC,DefRage,DefID,TurnTaken,ATKReck,DEFReck):
    if (DefID == 8):
        OppAC = OppAC + 2
        if (PrintRule == True):
            print(NameValues[DefID], "defensively duels! Their AC is now", OppAC)

    if (ATKReck == 1):
        HitChanceRoll1 = random.randint(1, 20)
        HitChanceRoll2 = random.randint(1, 20)
        if (PrintRule == True):
            print(AttackerName, "attacks with Advantage!")
            print("D20 ROLL 1", HitChanceRoll1, "\nD20 ROLL 2", HitChanceRoll2)
        if (HitChanceRoll1 >= HitChanceRoll2):
            HitChanceRoll = HitChanceRoll1
        elif (HitChanceRoll1 < HitChanceRoll2):
            HitChanceRoll = HitChanceRoll2

    elif (DEFReck == 1):
        if (TurnTaken == True):
            HitChanceRoll1 = random.randint(1, 20)
            HitChanceRoll2 = random.randint(1, 20)
            if (PrintRule == True):
                print(NameValues[DefID], "is hit with Disdvantage!")
                print("D20 ROLL 1", HitChanceRoll1, "\nD20 ROLL 2", HitChanceRoll2)
            if (HitChanceRoll1 >= HitChanceRoll2):
                HitChanceRoll = HitChanceRoll1
            elif (HitChanceRoll1 < HitChanceRoll2):
                HitChanceRoll = HitChanceRoll2

        else:
            HitChanceRoll = random.randint(1, 20)

    else:
        HitChanceRoll = random.randint(1, 20)

    HitChance = HitChanceRoll + Dexterity + 2
    if(PrintRule == True):
        print("Chance to hit for the punch for "+AttackerName+"'s attack was",HitChance)
    if (OppAC <= HitChance):
        if(HitChanceRoll == int(20)):
            Roll1 = random.randint(1, 4)
            Roll2 = random.randint(1, 4)
            HitDamage = Roll1+Roll2+Dexterity+2
            if (DefRage == int(1)):
                HitDamage = HitDamage/2
                HitDamage = math.floor(HitDamage)
                print("Damage Resisted")
            if(PrintRule == True):
                print("Critical Hit! Dealing",HitDamage,"Damage! Roll1:",Roll1," Roll2:",Roll2)
            return (HitDamage);
        else:
            Roll1=random.randint(1, 4)
            HitDamage =Roll1+Dexterity+2
            if (DefRage == int(1)):
                HitDamage = HitDamage/2
                HitDamage = math.floor(HitDamage)
                print("Damage Resisted")
            if(PrintRule == True):
                print("Attack Hit! Dealing",HitDamage,"Damage! Roll1:",Roll1)
            return(HitDamage);
    elif(OppAC>HitChance):
        if (PrintRule == True):
            print("The Attack Missed.")
        HitDamage = int(0)
        return (HitDamage);

def BarkSpellsLV1(AttackerName,OppAC,DefRage,OppDex,DefenderName,DefID,TurnTaken):
    #Ice Knife
    #First Strike
    if (DefID == 0 or DefID == 1):
        if (TurnTaken == True):
            HitChanceRoll1 = random.randint(1, 20)
            HitChanceRoll2 = random.randint(1, 20)
            if (PrintRule == True):
                print(NameValues[DefID], "is hit with Disdvantage!")
                print("D20 ROLL 1", HitChanceRoll1, "\nD20 ROLL 2", HitChanceRoll2)
            if (HitChanceRoll1 >= HitChanceRoll2):
                HitChanceRoll = HitChanceRoll1
            elif (HitChanceRoll1 < HitChanceRoll2):
                HitChanceRoll = HitChanceRoll2
        else:
            HitChanceRoll = random.randint(1, 20)
    else:
        HitChanceRoll = random.randint(1, 20)

    HitChance=HitChanceRoll+5
    if (PrintRule == True):
        print("Chance to hit for " + AttackerName + "'s attack was", HitChance)
    if (OppAC <= HitChance):
        if (HitChanceRoll == int(20)):
            Roll1 = random.randint(1, 10)
            Roll2 = random.randint(1, 10)
            HitDamage = Roll1 + Roll2
            if (DefRage == int(1)):
                HitDamage = HitDamage / 2
                HitDamage = math.floor(HitDamage)
                print("Damage Resisted")
            if (PrintRule == True):
                print("Critical Hit! Dealing", HitDamage, "Damage! Roll1:", Roll1, " Roll2:", Roll2)

        else:
            Roll1=random.randint(1, 10)
            HitDamage=Roll1
            if (DefRage == int(1)):
                HitDamage = HitDamage/2
                HitDamage = math.floor(HitDamage)
                print("Damage Resisted")
            if(PrintRule == True):
                print("Attack Hit! Dealing",HitDamage,"Damage! Roll1:",Roll1)

    elif (OppAC > HitChance):
        if (PrintRule == True):
            print("The Ice Knife Missed.")
        HitDamage = int(0)

    #Ice Knife Burst
    if (DefID == 0 or DefID == 1):
        DexRoll1 = random.randint(1, 20)
        DexRoll2 = random.randint(1, 20)
        if (PrintRule == True):
            print(DefenderName, "senses danger!", "\nDex Roll1:", DexRoll1, "\nDex Roll2:", DexRoll2)
        if (DexRoll1 >= DexRoll2):
            DexSavingThrow = DexRoll1 + OppDex
        elif (DexRoll2 > DexRoll1):
            DexSavingThrow = DexRoll2 + OppDex
    else:
        DexRoll = random.randint(1, 20)
        if (PrintRule == True):
            print("Dex Roll was", DexRoll)
        DexSavingThrow = DexRoll + OppDex

    if (PrintRule == True):
        print("Dex Saving Throw for "+DefenderName+" was",DexSavingThrow)
    if(DexSavingThrow<=13):
        Roll1 = random.randint(1, 6)
        Roll2 = random.randint(1, 6)
        HitDamage=HitDamage+Roll1+Roll2
        ExplosionDamage=Roll1+Roll2
        if(PrintRule == True):
            print("The Ice Knife Explodes! And the target failed the DexSave! Dealing", ExplosionDamage, "Damage! Roll1:", Roll1, "Roll2:", Roll2)
        return (HitDamage);
    if(DexSavingThrow>13):
        HitDamage = HitDamage
        if (PrintRule == True):
            print("The Ice Knife Explodes, but the target succeeded the DexSave!")
        return (HitDamage);

def BarkSpellsLV1ALT(DefenderName,OppCon):
    #Thunderwave
        ConSavingThrow = random.randint(1, 20) + OppCon
        if (PrintRule == True):
            print("Const Saving Throw for "+DefenderName+" was",ConSavingThrow)
        if(ConSavingThrow<=13):
            Roll1 = random.randint(1, 8)
            Roll2 = random.randint(1, 8)
            HitDamage=Roll1+Roll2
            if(PrintRule == True):
                print("Thunderwave Hit, and the target failed the ConstSave! Dealing", HitDamage, "Damage! Roll1:", Roll1, "Roll2:", Roll2)
        if(ConSavingThrow>13):
            Roll1 = random.randint(1, 8)
            Roll2 = random.randint(1, 8)
            HitDamage = (Roll1 + Roll2)/2
            HitDamage = math.floor(HitDamage)
            if (PrintRule == True):
                print("Thunderwave Hit, but the target succeeded the ConstSave! Dealing", HitDamage, " Damage! Roll1:", Roll1, "Roll2:", Roll2)
        return (HitDamage);

#NEEDS UPDATING
def BarkStaff(AttackerName,OppAC,AtkRage,DefRage):
    HitChanceRoll=random.randint(1,20)
    HitChance=HitChanceRoll+3
    if(PrintRule == True):
        print("Chance to hit for "+AttackerName+"'s attack was",HitChance)
    if (OppAC <= HitChance):
        if(HitChanceRoll == int(20)):
            Roll1 = random.randint(1, 6)
            Roll2 = random.randint(1, 6)
            Roll3 = random.randint(1, 6)
            Roll4 = random.randint(1, 6)
            if(AtkRage==int(1)):
                HitDamage = Roll1+Roll2+Roll3+Roll4+Strength+2
                if(DefRage==int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            else:
                HitDamage = Roll1+Roll2+Roll3+Roll4+Strength
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            if(PrintRule == True):
                print("Critical Hit! Dealing",HitDamage,"Damage! Roll1:",Roll1," Roll2:",Roll2," Roll3:", Roll3," Roll4:", Roll4)
            return (HitDamage);
        else:
            Roll1=random.randint(1, 6)
            Roll2=random.randint(1, 6)
            if (AtkRage == int(1)):
                HitDamage = Roll1+Roll2+Strength+2
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            else:
                HitDamage =Roll1+Roll2+Strength
                if (DefRage == int(1)):
                    HitDamage = HitDamage/2
                    HitDamage = math.floor(HitDamage)
                    print("Damage Resisted")
            if(PrintRule == True):
                print("Attack Hit! Dealing",HitDamage,"Damage! Roll1:",Roll1," Roll2:",Roll2)
            return(HitDamage);
    elif(OppAC>HitChance):
        if (PrintRule == True):
            print("The Attack Missed.")
        HitDamage = int(0)
        return (HitDamage);

def SporeDamage(HP,NameDEF,NameATK):
    SporeDamage = random.randint(1, 4) + random.randint(1, 4)
    HPOLD = HP
    HP = HP - SporeDamage
    if (PrintRule == True):
        print(NameDEF, "is assaulted by " + NameATK + "'s spores! Taking", SporeDamage,
              "Damage!")
        print(NameDEF, "has", HP, "HP left! Down from", HPOLD, "HP")

def InitiativeRoll(Init_char1,Init_char2,InitWins_char1,InitWins_char2):
    # Rolls for initiative
    OrderChosen = False
    while (OrderChosen == False):
        InitRoll1 = random.randint(1, 20) + Init_char1
        InitRoll2 = random.randint(1, 20) + Init_char2
        if (PrintRule == True):
            print("--------------------------------------------------------------------\nInitiative Roll 1:", InitRoll1,"\nInitiative Roll 2:", InitRoll2)
        if (InitRoll1 > InitRoll2):
            Player1Skip = int(0)
            InitWins_char1 = InitWins_char1 + 1
            if (PrintRule == True):
                print(Name_char1, "goes first!")
            return (Player1Skip);
        elif (InitRoll1 < InitRoll2):
            Player1Skip = int(1)
            InitWins_char2 = InitWins_char2 + 1
            if (PrintRule == True):
                print(Name_char2, "goes first!")
            return (Player1Skip);
        else:
            if (PrintRule == True):
                print("Initiative Roll Tie!")

def StatReset():
    HP_char1 = HPreset_char1
    HP_char2 = HPreset_char2
    SpellSlot1_char1 = SpellSlot1Values[Character1ID]
    SpellSlot1_char2 = SpellSlot1Values[Character2ID]
    Ki_char1 = KiValues[Character1ID]
    Ki_char2 = KiValues[Character2ID]
    TurnTaken1 = False
    TurnTaken2 = False
    if (PrintRule == True):
        print(Name_char1, "HP has been reset to", HP_char1)
        print(Name_char2, "HP has been reset to", HP_char2)


#############################
while(TotalGames < SimGames):
    Player1Skip = InitiativeRoll(Init_char1,Init_char2,InitWins_char1,InitWins_char2)
    StatReset()

    while(HP_char1>0 and HP_char2>0):
        if (Player1Skip == int(0)):
            #PLAYER 1 TURN
            if (PrintRule == True):
                print("--->", Name_char1, "<---")
            match Character1ID:
                case 0: #Grugg
                    TurnTaken1 = True
                    if (PrintRule == True):
                        print(Name_char1, "attacks using " + Name_char1 + "'s Club!")
                    HitDamage = Meele2D6(Strength_char1, Name_char1, AC_char2, Rage_char1, Rage_char2,Character2ID,Character1ID,TurnTaken2,Reckless_char2)
                    if (Character2ID == int(6) or Character2ID == int(7)):
                        SporeDamage(HP_char1,Name_char1,Name_char2)

                case 1: #Clugg
                    TurnTaken1 = True
                    if (PrintRule == True):
                        print(Name_char1, "attacks using " + Name_char1 + "'s Club!")
                    HitDamage = Meele2D6(Strength_char1, Name_char1, AC_char2, Rage_char1, Rage_char2,Character2ID,Character1ID,TurnTaken2,Reckless_char2)
                    if (Character2ID == int(6) or Character2ID == int(7)):
                        SporeDamage(HP_char1,Name_char1,Name_char2)

                case 2: #Alice (Burning Hands)
                    if (SpellSlot1_char1 > 0):
                        SpellSlot1_char1 = SpellSlot1_char1 - 1
                        if (PrintRule == True):
                            print("Alice has", SpellSlot1_char1, "Lv1 Spell Slots left")
                            print(Name_char1, "attacks using Burning Hands!")
                        HitDamage = AliceSpellsLV1(Name_char2, Dex_char2,Character2ID)
                    else:
                        if (PrintRule == True):
                            print(Name_char1, "attacks using Chill Touch!")
                        HitDamage = ChillTouchCantrip(Name_char2, Dex_char2)
                    if (Character2ID == int(6) or Character2ID == int(7)):
                        SporeDamage(HP_char1,Name_char1,Name_char2)

                case 3: #Alice (Magic Missile)
                    if (SpellSlot1_char1 > 0):
                        SpellSlot1_char1 = SpellSlot1_char1 - 1
                        if (PrintRule == True):
                            print("Alice has", SpellSlot1_char1, "Lv1 Spell Slots left")
                            print(Name_char1, "attacks using Magic Missile!")
                        HitDamage = AliceSpellsLV1ALT()
                    else:
                        if (PrintRule == True):
                            print(Name_char1, "attacks using Chill Touch!")
                        HitDamage = ChillTouchCantrip(Name_char2, Dex_char2)
                    if (Character2ID == int(6) or Character2ID == int(7)):
                        SporeDamage(HP_char1,Name_char1,Name_char2)

                case 4: #Petrov
                    if (SpellSlot1_char1 > 0):
                        SpellSlot1_char1 = SpellSlot1_char1 - 1
                        if (PrintRule == True):
                            print("Petrov has", SpellSlot1_char1, "Lv1 Spell Slots left")
                            print(Name_char1, "attacks using Inflict Wounds!")
                        HitDamage = PetrovSpellsLV1(Name_char1, AC_char2)
                    else:
                        if (PrintRule == True):
                            print(Name_char1, "attacks using Sacred Flame!")
                        HitDamage = PetrovSpellsCantrip(Name_char2, Dex_char2,Character2ID)
                    if (Character2ID == int(6) or Character2ID == int(7)):
                        SporeDamage(HP_char1,Name_char1,Name_char2)

                case 5: #Valdos
                    if (PrintRule == True):
                        print(Name_char1, "attacks using his bare hands!")
                    HitDamage1 = ValdosPunch(Dex_char1,Name_char1, AC_char2, Rage_char2,Character2ID,Character1ID,TurnTaken2,Reckless_char2)
                    HitDamage2 = ValdosPunch(Dex_char1,Name_char1, AC_char2, Rage_char2,Character2ID,Character1ID,TurnTaken2,Reckless_char2)
                    HitDamage3 = int(0)
                    if (Ki_char1 > 0):
                        Ki_char1 = Ki_char1 - 1
                        HitDamage3 = ValdosPunch(Name_char1, AC_char2, Rage_char2,Character2ID,Character1ID,TurnTaken2,Reckless_char1,Reckless_char2)
                    HitDamage = HitDamage1 + HitDamage2 + HitDamage3
                    if (PrintRule == True):
                        print("Valdos has", Ki_char1, "Ki points left")
                    if (Character2ID == int(6) or Character2ID == int(7)):
                        SporeDamage(HP_char1,Name_char1,Name_char2)

                case 6: #Bark (Ice Knife)
                    if (SpellSlot1_char1 > 0):
                        SpellSlot1_char1 = SpellSlot1_char1 - 1
                        if (PrintRule == True):
                            print("Bark has", SpellSlot1_char1, "Lv1 Spell Slots left")
                            print(Name_char1, "attacks using Ice Knife!")
                        HitDamage = BarkSpellsLV1(Name_char1, AC_char2, Rage_char2, Dex_char2, Name_char2,Character2ID,TurnTaken2)
                    else:
                        if (PrintRule == True):
                            print(Name_char1, "attacks using Chill Touch!")
                        HitDamage = ChillTouchCantrip(Name_char2, Dex_char2)
                    if (Character2ID == int(6) or Character2ID == int(7)):
                        SporeDamage(HP_char1,Name_char1,Name_char2)

                case 7: #Bark (Thunderwave)
                    if (SpellSlot1_char1 > 0):
                        SpellSlot1_char1 = SpellSlot1_char1 - 1
                        print(Name_char1, "has", SpellSlot1_char1, "Lv1 Spell Slots left")
                        if (PrintRule == True):
                            print(Name_char1, "attacks using Thunderwave!")
                        HitDamage = BarkSpellsLV1ALT(Name_char2, Const_char2)
                    else:
                        if (PrintRule == True):
                            print(Name_char1, "attacks using Chill Touch!")
                        HitDamage = ChillTouchCantrip(Name_char2, Dex_char2)
                    if (Character2ID == int(6) or Character2ID == int(7)):
                        SporeDamage(HP_char1,Name_char1,Name_char2)

                case 8:  #Tortimer
                    if (PrintRule == True):
                        print(Name_char1, "attacks using " + Name_char1 + "'s Rapier!")
                    HitDamage = DexMeele1D8(Dex_char1, Name_char1, AC_char2, Rage_char1, Rage_char2,Character2ID,Character1ID,TurnTaken2,Reckless_char2)
                    if (Character2ID == int(6) or Character2ID == int(7)):
                        SporeDamage(HP_char1,Name_char1,Name_char2)

                case 9:
                    if (PrintRule == True):
                        print(Name_char1, "bites down on "+Name_char2+"!")
                    HitDamage = TRexBite(Strength_char1, Name_char1, AC_char2, Rage_char1, Rage_char2, Character2ID,Character1ID, TurnTaken2,Reckless_char2)
                    if (Character2ID == int(6) or Character2ID == int(7)):
                        SporeDamage(HP_char1,Name_char1,Name_char2)
                case _:
                    print("Invalid Number")

            # Damage Calculation
            HPOLD_char2 = HP_char2
            HP_char2 = HP_char2 - HitDamage

            if (PrintRule == True):
                print(Name_char1, "dealt", HitDamage, "Damage")
                print(Name_char2, "has", HP_char2, "HP left! (Down from", HPOLD_char2, "HP)")
            if (HP_char2 <= 0):
                if (PrintRule == True):
                    print(Name_char2, "has died!")
                Wins_char1 = Wins_char1 + 1
                TotalGames = TotalGames + 1
                break

        # PLAYER 2 TURN
        if (Player1Skip == int(1)):
            Player1Skip = int(0)
        if (PrintRule == True):
            print("--->", Name_char2, "<---")

        match Character2ID:
            case 0:  # Grugg
                TurnTaken2 = True
                if (PrintRule == True):
                    print(Name_char2, "attacks using Grugg's Club!")
                    HitDamage = Meele2D6(Strength_char2, Name_char2, AC_char1, Rage_char2, Rage_char1,Character1ID,Character2ID,TurnTaken1,Reckless_char1)
                if (Character1ID == int(6) or Character1ID == int(7)):
                    SporeDamage(HP_char2,Name_char2,Name_char1)

            case 1:  # Clugg
                TurnTaken2 = True
                if (PrintRule == True):
                    print(Name_char2, "attacks using Grugg's Club!")
                HitDamage = Meele2D6(Strength_char2, Name_char2, AC_char1, Rage_char2, Rage_char1,Character1ID,Character2ID,TurnTaken1,Reckless_char1)
                if (Character1ID == int(6) or Character1ID == int(7)):
                    SporeDamage(HP_char2,Name_char2,Name_char1)

            case 2:  # Alice (Burning Hands)
                if (SpellSlot1_char2 > 0):
                    SpellSlot1_char2 = SpellSlot1_char2 - 1
                    if (PrintRule == True):
                        print("Alice has", SpellSlot1_char2, "Lv1 Spell Slots left")
                        print(Name_char2, "attacks using Burning Hands!")
                    HitDamage = AliceSpellsLV1(Name_char1, Dex_char1,Character1ID)
                else:
                    if (PrintRule == True):
                        print(Name_char2, "attacks using Chill Touch!")
                    HitDamage = ChillTouchCantrip(Name_char2, AC_char1)
                if (Character1ID == int(6) or Character1ID == int(7)):
                    SporeDamage(HP_char2,Name_char2,Name_char1)

            case 3:  # Alice (Magic Missile)
                if (SpellSlot1_char2 > 0):
                    SpellSlot1_char2 = SpellSlot1_char2 - 1
                    if (PrintRule == True):
                        print("Alice has", SpellSlot1_char2, "Lv1 Spell Slots left")
                        print(Name_char2, "attacks using Magic Missile!")
                    HitDamage = AliceSpellsLV1ALT()
                else:
                    if (PrintRule == True):
                        print(Name_char2, "attacks using Chill Touch!")
                    HitDamage = ChillTouchCantrip(Name_char1, Dex_char1)
                if (Character1ID == int(6) or Character1ID == int(7)):
                    SporeDamage(HP_char2,Name_char2,Name_char1)

            case 4:  # Petrov
                if (SpellSlot1_char2 > 0):
                    SpellSlot1_char2 = SpellSlot1_char2 - 1
                    if (PrintRule == True):
                        print("Petrov has", SpellSlot1_char2, "Lv1 Spell Slots left")
                        print(Name_char2, "attacks using Inflict Wounds!")
                    HitDamage = PetrovSpellsLV1(Name_char2, AC_char1)
                else:
                    if (PrintRule == True):
                        print(Name_char2, "attacks using Sacred Flame!")
                    HitDamage = PetrovSpellsCantrip(Name_char1, Dex_char1,Character1ID)
                if (Character1ID == int(6) or Character1ID == int(7)):
                    SporeDamage(HP_char2,Name_char2,Name_char1)

            case 5:  # Valdos
                if (PrintRule == True):
                    print(Name_char1, "attacks using his bare hands!")
                HitDamage1 = ValdosPunch(Dex_char2,Name_char2, AC_char1, Rage_char1,Character1ID,Character2ID,TurnTaken1,Reckless_char1)
                HitDamage2 = ValdosPunch(Dex_char2,Name_char2, AC_char1, Rage_char1,Character1ID,Character2ID,TurnTaken1,Reckless_char1)
                HitDamage3 = int(0)
                if (Ki_char2 > 0):
                    Ki_char2 = Ki_char2 - 1
                    if (PrintRule == True):
                        print("Valdos has", Ki_char2, "Ki points left")
                    HitDamage3 = ValdosPunch(Dex_char2,Name_char2, AC_char1, Rage_char1,Character1ID,Character2ID,TurnTaken1,Reckless_char1)
                HitDamage = HitDamage1 + HitDamage2 + HitDamage3
                if (Character1ID == int(6) or Character1ID == int(7)):
                    SporeDamage(HP_char2,Name_char2,Name_char1)

            case 6:  # Bark (Ice Knife)
                if (SpellSlot1_char2 > 0):
                    SpellSlot1_char2 = SpellSlot1_char2 - 1
                    if (PrintRule == True):
                        print("Bark has", SpellSlot1_char2, "Lv1 Spell Slots left")
                        print(Name_char2, "attacks using Ice Knife!")
                    HitDamage = BarkSpellsLV1(Name_char2, AC_char1, Rage_char1, Dex_char1, Name_char1,Character1ID,TurnTaken1)
                else:
                    if (PrintRule == True):
                        print(Name_char2, "attacks using Chill Touch!")
                    HitDamage = ChillTouchCantrip(Name_char1, Dex_char1)
                if (Character1ID == int(6) or Character1ID == int(7)):
                    SporeDamage(HP_char2,Name_char2,Name_char1)

            case 7:  # Bark (Thunderwave)
                if (SpellSlot1_char2 > 0):
                    SpellSlot1_char2 = SpellSlot1_char2 - 1
                    if (PrintRule == True):
                        print(Name_char2, "has", SpellSlot1_char2, "Lv1 Spell Slots left")
                        print(Name_char2, "attacks using Thunderwave!")
                    HitDamage = BarkSpellsLV1ALT(Name_char1, Const_char1)
                else:
                    if (PrintRule == True):
                        print(Name_char2, "attacks using Chill Touch!")
                    HitDamage = ChillTouchCantrip(Name_char1, Dex_char1)
                if (Character1ID == int(6) or Character1ID == int(7)):
                    SporeDamage(HP_char2,Name_char2,Name_char1)

            case 8:  # Tortimer
                if (PrintRule == True):
                    print(Name_char2, "attacks using " + Name_char2 + "'s Rapier!")
                HitDamage = DexMeele1D8(Dex_char2, Name_char2, AC_char1, Rage_char2, Rage_char1,Character1ID,Character2ID,TurnTaken1,Reckless_char1)
                if (Character1ID == int(6) or Character1ID == int(7)):
                    SporeDamage(HP_char2,Name_char2,Name_char1)

            case 9:
                if (PrintRule == True):
                    print(Name_char2, "bites down on " + Name_char1 + "!")
                HitDamage = TRexBite(Strength_char2, Name_char2, AC_char1, Rage_char2, Rage_char1, Character1ID,Character2ID, TurnTaken1,Reckless_char1)
                if (Character1ID == int(6) or Character1ID == int(7)):
                    SporeDamage(HP_char2,Name_char2,Name_char1)


            case _:
                print("Invalid Number")

        # Damage Calculation
        HPOLD_char1 = HP_char1
        HP_char1 = HP_char1 - HitDamage

        if (PrintRule == True):
            print(Name_char2, "dealt", HitDamage, "Damage")
            print(Name_char1, "has", HP_char1, "HP left! (Down from", HPOLD_char1, "HP)")
        if (HP_char1 <= 0):
            if (PrintRule == True):
                print(Name_char1, "has died!")
            Wins_char2 = Wins_char2 + 1
            TotalGames = TotalGames + 1
            break

print("----> ENDING RESULTS <----")
SimGames=str(SimGames)
print("A total of",TotalGames,"games were simulated. ("+SimGames+" games expected)")
print(Name_char1,"won",Wins_char1,"of them.")
print(Name_char2,"won",Wins_char2,"of them.")
Char1WinPercent=float((Wins_char1/TotalGames)*100)
Char2WinPercent=float((Wins_char2/TotalGames)*100)
Char1WinPercent=round(Char1WinPercent,2)
Char2WinPercent=round(Char2WinPercent,2)
if(Char1WinPercent>Char2WinPercent):
    print(Name_char1,"won overall, with a winrate of",Char1WinPercent,"%")
elif(Char1WinPercent<Char2WinPercent):
    print(Name_char2, "won overall, with a winrate of", Char2WinPercent, "%")
else:
    print("They are exactly evenly balanced! The winrate was exactly 50/50")

print(Name_char1, "had a winrate of", Char1WinPercent, "%")
print(Name_char2, "had a winrate of", Char2WinPercent, "%")
print(Name_char1,"went first",InitWins_char1,"times")
print(Name_char2,"went first",InitWins_char2,"times")