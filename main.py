__author__ = "Pol"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1"
__status__ = "Production"
from colorama import init
from colorama import Fore, Back, Style
from os import system
from time import time
from time import sleep
from random import randint
from pyinputplus import inputPassword
from sys import platform
from sys import exit
import hashlib
titulo = 'Soneto de la dulce queja, de Sonetos del amor oscuro'

poema = '''
\tJ[d]ec_[ZeWf[hZ[hbWcWhWl_bbW
\tZ[jkie`eiZ[[ijWjkW"o[bWY[dje
\tgk[Z[deY^[c[fed[[dbWc[`_bbW
\tbWieb_jWh_WheiWZ[jkWb_[dje$
\tJ[d]ef[dWZ[i[h[d[ijWeh_bbW
\tjhedYei_dhWcWi1obegk[c×ii_[dje
\t[idej[d[hbW\beh"fkbfWeWhY_bbW"
\tfWhW[b]kiWdeZ[c_ik\h_c_[dje$
\tI_jð[h[i[bj[ieheeYkbjecãe"
\ti_[h[ic_Yhkpoc_Zebehce`WZe"
\ti_ieo[bf[hheZ[jki[çehãe"
\tdec[Z[`[if[hZ[hbegk[^[]WdWZe
\toZ[YehWbWiW]kWiZ[jkhãe
\tYed^e`WiZ[c_ejeçe[dW`[dWZe$
'''


def main():
    if platform == 'win32':
        system('title Comprovación')
    comprovacion()
    if platform == 'win32':
        system('title Intro')
    if platform == 'win32':
        system('title Poema')
    global titulo
    global poema
    muestra = 0
    tt = 0
    poemat = ""
    for i in poema:
        if i != '\t' and i != '\n':
            poemat += chr(ord(i) + 10)
        else:
            poemat += i
    poema = poemat
    while muestra <= len(poema.split(" ")):
        t = time()
        system('cls')
        print(Back.BLACK + Fore.LIGHTCYAN_EX)
        print(titulo)
        print(Back.MAGENTA + Fore.WHITE, end='')
        for i in range(len(poema.split(" "))):
            if i <= muestra:
                print(poema.split(" ")[i], end=' ')
            else:
                for x in poema.split(" ")[i]:
                    if x == "\n":
                        print(x, end='\t')
                    else:
                        print(chr(randint(65, 122)), end='')
        print()
        print()
        print("\t\tGarcía Lorca"+Fore.BLACK)
        if tt *3 > muestra:
            muestra += 1
        sleep(0.05)
        tt += (time() - t)
    input()
    if platform == 'win32':
        system('title Fin')
    print()
    input('Fin, espero que te haya gustado')


tunel_ = []


def crear_tunel(radio):
    tunel = [[' ' for x in range(radio)] for x in range(radio)]
    return tunel


def mostrar_tunel(tunel):
    for a in tunel:
        for b in a:
            if str(type(b)).split()[1][1:-2] == 'int':
                if b % 2 == 0:
                    print(Back.BLUE + Fore.LIGHTRED_EX + '####', end='')
                else:
                    print(Back.LIGHTRED_EX + Fore.BLACK + '····', end='')
            else:
                print(Back.LIGHTMAGENTA_EX + Fore.BLUE + ' '*4, end='')
        print(Style.RESET_ALL, end='\n')


def construir():
    global tunel_
    avance = 0
    while tunel_[avance][len(tunel_)//2] != ' ':
        avance += 1
        if avance == len(tunel_):
            return False
    for i in range(avance, len(tunel_) - avance):
        tunel_[avance][i] = len(tunel_) - avance
        tunel_[len(tunel_)-avance-1][i] = len(tunel_)-avance
        tunel_[i][avance] = len(tunel_) - avance
        tunel_[i][len(tunel_)-avance-1] = len(tunel_) - avance
    return True


def comprovacion():
    system('cls')
    print(Fore.RED+Back.BLACK, end='')
    for i in range(3):
        passwd = inputPassword(f'Escribe la contraseña (intentos restantos: {3 - i}): ', mask='·').upper()
        # contraseña = passwd
        if hashlib.md5(passwd.encode('utf-8')).hexdigest() == 'f8467b120f4ed91f94074a286113f10a':
            return True
        system('cls')
    print('Fail')
    input()
    exit()




if __name__ == '__main__':
    init()
    main()

