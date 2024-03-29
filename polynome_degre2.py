# computing. ready august 2019
# https://nsi.xyz/
# https://workshop.numworks.com/python/cent20/polynome_degre2
# Auteurs : Arthur Jacquin, Kevin Fedyna, Vincent Robert.

from math import sqrt
import sys

a, b, c = 0, 0, 0


def def_calc_trinome():
    global a, b, c, d, e, nb, x, y, x1, x2
    while a == 0:
        a = optimiser(float(input('a = ')))
    b = optimiser(float(input('b = ')))
    c = optimiser(float(input('c = ')))
    d = optimiser(float(b**2 - 4 * a * c))
    e = optimiser(float(a * (-b / (2 * a))**2 + b * (-b / (2 * a)) + c))
    if d == 0:
        nb = 1
    else:
        nb = 2
    x = optimiser((-b) / (2 * a))
    y = optimiser((sqrt(abs(d))) / (2 * a))
    x1 = optimiser(min(x + y, x - y))
    x2 = optimiser(max(x - y, x + y))


def aff_entete():
    optimiser(9, br=1)
    print("Polynome (equation) de degre 2")
    if a == 0:
        print("P(x)=ax^2+bx+c (=0)")
    else:
        print("P(x)={}{}{} (=0)".format(
                optimiser(a, ap="x^2", r=4),
                optimiser(b, p=1, ap="x", r=4, naf=1), optimiser(c, p=1, r=4, naf=1)))
        print("")


def aff_menu():
    # Choix 1
    print("1. Changer les valeurs a,b,c")
    # Choix 2
    if d < 0:
        s = "< 0"
    elif d > 0:
        s = "> 0"
    elif d == 0:
        s = ""
    print("2. Discriminant = {} {} ".format(d, s))
    # Choix 3
    if d < 0:
        print("3. Racines complexes conjuguees : 2 ")
        print("   z1= {} + {} i".format(x, y))
        print("   z2= {} - {} i".format(x, y))
    elif d > 0:
        print("3. Racines reelles distinctes : 2 ")
        print("   x1= {}".format(x1))
        print("   x2= {}".format(x2))
    elif d == 0:
        print("3. Racine reelle double : 1 ")
        print("   x1=x2= {}".format(x))
    # Choix 4
    if d < 0:
        if a < 0:
            print("4. Signe : -", end=" ")
        else:
            print("4. Signe : +", end=" ")
    elif d == 0:
        if a < 0:
            print("4. Signe : -0-", end=" ")
        else:
            print("4. Signe : +0+", end=" ")
    else:
        if a < 0:
            print("4. Signe : -+-", end=" ")
        else:
            print("4. Signe : +-+", end=" ")
    if a < 0:
        print(", extremum : M")
    else:
        print(", extremum : m")
    # Choix 5
    if d < 0:
        print("5. Factorisation dans les complexes")
    elif d >= 0:
        print("5. Factorisation dans les reels")
        # Choix 6
    print("6. Quitter")


def exec_menu(i):
    global a, b, c, d, x, y
    aff_entete()
    if i == 1:
        a, b, c = 0, 0, 0
        def_calc_trinome()
    elif i == 2:
        # Arthur
        print("2. Calcul du discriminant :")
        print("")
        print("d = b^2 + 4*a*c")
        print("  = {}^2 + 4*{}*{}".format(optimiser(b,par=1),optimiser(a,par=1),optimiser(c,par=1)))
        if b == 0 and c != 0:
            print(optimiser(4*a*c,av="  = "))
        else:
            print("  = {}{}".format(optimiser(b**2),optimiser(4*a*c,p=1,naf=1)))
            if c != 0:
                print(optimiser(d,av="  = "))
        print("")
        print(optimiser(d,av="d = "), end=" ")
        if d == 0:
            print("")
        elif d < 0:
            print("< 0")
        elif d > 0:
            print("> 0")
        if b != 0 and c != 0:
            print("")
    elif i == 3:
        # Arthur
        print("3. Calcul des racines :")
        print("")
        if d < 0:
            print("d < 0 donc il existe")
            print("2 racines complexes conjugees")
            print("telles que :")
            print("")
            print("z1 = -b/2a + %(|d|)/2a i")
            print("z2 = -b/2a - %(|d|)/2a i")
        elif d == 0:
            print("d = 0 donc il existe")
            print("1 racine reelle double")
            print("telle que :")
            print("")
            print("x1 = x2 = -b/2a")
            print("")
        elif d > 0:
            print("d > 0 donc il existe")
            print("2 racines reelles distinctes")
            print("telles que :")
            print("")
            if a > 0:
                print("x1 = (-b-%(d))/(2a)")
                print("x2 = (-b+%(d))/(2a)")
            else:
                print("x1 = (-b+%(d))/(2a)")
                print("x2 = (-b-%(d))/(2a)")
        input()
        aff_entete()
        print("3. Calcul des racines :")
        print("")
        if d < 0:
            print("z1 = -b/2a + %(|d|)/2a i")
            print("   = (-{0})/(2*{1}) + %(|{2}|)/(2*{1}) i".format(optimiser(b,par=1,r=4),optimiser(a,par=1,r=4),optimiser(d,r=4)))
            print("   = {} + {} i".format(x,optimiser(y,par=1)))
            print("z2 = -b/2a - %(|d|)/2a i")
            print("   = (-{0})/(2*{1}) - %(|{2}|)/(2*{1}) i".format(optimiser(b,par=1,r=4),optimiser(a,par=1,r=4),optimiser(d,r=4)))
            print("   = {} - {} i".format(x,optimiser(y,par=1)))
        elif d == 0:
            print("x1 = x2 = -b/2a")
            print("   = (-{})/(2*{})".format(optimiser(b,par=1,r=5),optimiser(a,par=1,r=5)))
            print(optimiser(x,av="   = "))
            for i in range(3): print("")
        elif d > 0:
            if a > 0:
                print("x1 = (-b-%(d))/(2a)")
                print("   = (-{}-%({}))/(2*{})".format(optimiser(b,par=1,r=4),optimiser(d,r=4),optimiser(a,par=1,r=4)))
                print(optimiser(x-abs(y),av="   = "))
                print("x2 = (-b+%(d))/(2a)")
                print("   = (-{}+%({}))/(2*{})".format(optimiser(b,par=1,r=4),optimiser(d,r=4),optimiser(a,par=1,r=4)))
                print(optimiser(x+abs(y),av="   = "))
            else:
                print("x1 = (-b+%(d))/(2a)")
                print("   = (-{}+%({}))/(2*{})".format(optimiser(b,par=1,r=4),optimiser(d,r=4),optimiser(a,par=1,r=4)))
                print(optimiser(x+abs(y),av="   = "))
                print("x2 = (-b-%(d))/(2a)")
                print("   = (-{}-%({}))/(2*{})".format(optimiser(b,par=1,r=4),optimiser(d,r=4),optimiser(a,par=1,r=4)))
                print(optimiser(x-abs(y),av="   = "))
    elif i == 4:
        # Vincent
        print("-----------------------------")
        if d <= 0:
            print("  x |        -b/(2a)        |")
            print("-----------------------------")
            if a > 0:
                print("P(x)|     +     m     +     |")
            else:
                print("P(x)|     -     M     -     |")
        else:
            print("  x |    x1  -b/(2a)  x2    |")
            print("-----------------------------")
            if a > 0:
                print("P(x)|  +  0  -  m  -  0  +  |")
            else:
                print("P(x)|  -  0  +  M  +  0  -  |")
        print("-----------------------------")
        print("Extremum : ")
        print("   (", optimiser(-b / (2 * a), r=4), ";", optimiser(e, r=4), ")")
        print("")
        print("")
    elif i == 5:
        # Kevin
        if d == 0:
            print("P(x) = a(x-(-b/2a))^2")
            if x1 != 0:
                print(optimiser(-x1, "P(x) = {}(x".format(a), ")^2", p=1))
            else:
                print("P(x) = {}x^2".format(a))
        elif d > 0:
            print("P(x) = a(x-x1)(x-x2)")
            print(optimiser(-x2,optimiser(-x1,"P(x) = {}(x".format(a),")(x",p=1,naf=2,r=4),")",p=1,naf=2,r=4))
        else:
            print("P(z) = a(z-z1)(z-z2)\nAvec:")
            print(optimiser(-x,"(z-z1) = (z",optimiser(y,ap="i",r=4,naf=1)+")",r=4,naf=2))
            print(optimiser(-x,"(z-z2) = (z",optimiser(-y,ap="i",r=4,naf=1)+")",r=4,naf=2))
    elif i == 6:
        pass
    if i != 6 and i != 1:
        input()


def optimiser(v, av="", ap="", p=0, r=8, naf=0, br=0, par=0):
    # valeur, str avant, str apres, afficher signe, arrondi,
    # ne pas afficher un 0 (1, 2 et 3: resultats differents), sauter v ligne
    # parentheses autour de v
    if br != 0:
        for i in range(v):
            print("")
    elif br == 0:
        if v == 0 and naf == 1:
            return ""
        if v == 0 and naf == 2:
            return str(av) + str(ap)
        if v == 0 and naf == 3:
            return str(av)
        if v == int(v):
            v = int(v)
        else:
            v = round(v, r)
        if av == "" and ap == "" and p == 0 and par == 0:
            return v
        if p == 1 and v > 0:
            v = "+" + str(v)
        if par == 1 and v < 0:
            v = "({})".format(v)
    return str(av) + str(v) + str(ap)


def menu(warning=""):
    aff_entete()
    aff_menu()
    if warning != "":
        print(warning)
    choix = 0
    while choix == 0:
        try:
            choix = int(input())
        except:
            choix = 0
            menu(">> saisir un entier entre 1 et 6 !")
    exec_menu(choix)
    if choix != 6:
        menu()


optimiser(9, br=1)
exec_menu(1)
menu()

# Supprimer 7 lignes ci dessous pour tester sur la numworks
s = 0
for name in dir():
    print("nom var = " + name)
    print(globals()[name])
    print(sys.getsizeof(globals()[name]))
    s = s + sys.getsizeof(globals()[name])
    print(s)