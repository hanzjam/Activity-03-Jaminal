# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import scripty1 as one
import scripty2 as two

def ev_ulet():
    eff = int(input("Effort Values: "))
    if eff <= 255:
        global ort
        ort = eff
        global d1
        d1 = two.owow.dabest(bv, val, ort, level4)
        print('Answer: ', two.owow.ev_yarn(stat, modf, d1, level4), end ='\n\n')
    else:
        print('Values are between 0 to 255 only. Try again.')
        ev_ulet()

def iv_ulet():
    indi = int(input("Individual Value: "))
    if indi <= 31:
        global val
        val = indi
        ev_ulet()
    else:
        print('Values are between 0 to 31 only. Try again.')
        iv_ulet()

def modif():
    nature = float(input("Nature value: "))
    if nature == 1.1 or 0.9:
        global modf
        modf = nature
        level3 = int(input("Target Level: "))
        global level4
        level4 = level3
        base3 = int(input("Base Stat: "))
        global bv
        bv = base3
        iv_ulet()
    else:
        print('Values can only be 1.1 or 0.9 if beneficial or hindering. Try again.')
        modif()

def nature_form():
    nature = float(input("Nature value: "))
    if nature == 1.1 or 0.9:
        global nat
        nat = nature
        print('Loading ...')
        print('Answer: ', one.forever.other_stat(nat, bp, vi, ve, lev), end ='\n\n')
    else:
        print('Values can only be 1.1 or 0.9 if beneficial or hindering. Try again.')
        nature_form()
  
def level2_form():
    level2 = int(input("Target Level: "))
    global lev
    lev = level2
    nature_form()

def level1_form():
    level1 = int(input("Target Level: "))
    global level
    level = level1
    print('\nAnswer: ', one.forever.hp_stat(base, iv, ev, level), end ='\n\n')

def ev2_form():
    ev2 = int(input("Effort Values: "))
    if ev2 <= 255:
        global ve
        ve = ev2
        level2_form()
    else:
        print('Values are between 0 to 255 only. Try again.')
        ev2_form()

def ev1_form():
    ev1 = int(input("Effort Values: "))
    if ev1 <= 255:
        global ev
        ev = ev1
        level1_form()
    else:
        print('Values are between 0 to 255 only. Try again.')
        ev1_form()

def iv2_form():
    iv2 = int(input("Individual Value: "))
    if iv2 <= 31:
        global vi
        vi = iv2
        ev2_form()
    else:
        print('Values are between 0 to 31 only. Try again.')
        iv2_form()

def iv1_form():
    iv1 = int(input("Individual Value: "))
    if iv1 <= 31:
        global iv
        iv = iv1
        ev1_form()
    else:
        print('Values are between 0 to 31 only. Try again.')
        iv1_form()

def choosy():
    in_on = int(input('\nStat Calculator: \nChoose: \n1. Individual Stat \n2. Other Stat \nAnswer: '))
    if in_on == 1:
        print("\n\nStat Calculator: \nThis is your Pokemon HP stat values: \nPut the values for:\n")
        base1 = int(input("Base HP:"))
        global base
        base = base1
        iv1_form()
    elif in_on == 2:
        print("\n\nStat Calculator: \nThis is the other Pokemon HP stat values: \nPut the values for:\n")
        base2 = int(input("Base HP: "))
        global bp
        bp = base2
        iv2_form()
    else:
        print("Sorry try again!")
        choosy()


def intro():
    stev = int(input("Choose your calculator: \n1: Statistics \n2. EV? \nAnswer: "))
    if stev == 1:
        choosy()
    elif stev == 2:
        print("EV Calculator: \nPut the Stat Values for: \n")
        global stat
        desire = int(input("Desired increase stat: "))
        stat = desire
        modif()
    else:
        print("Sorry try again!")
        intro()

print("Welcome to Pokemon Calculator")
intro()
