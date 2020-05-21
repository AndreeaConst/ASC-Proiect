# Cod Daniel - zona 2

def and_gate(i0, i1, i2, i3):

    if i0 == 1 and i1 == 1 and i2 == 1 and i3 == 1:
        return 1
    elif i0 == 0 and i1 == 0 and i2 == 0 and i3 == 0:
        return 1
    else:
        return 0

# Cod Claudiu - zona 1
def input():

    numar = 2  # numar de citit de la tastatura
    binar = bin(numar) # transformare numar din baza initiala in baza 2
    vector = [0, 0, 0, 0]
    i0 = i1 = i2 = i3 = 0

    vector[3] = binar[-1]
    i3 = vector[3]

    if numar > 1:
        vector[2] = binar[-2]
        i2 = vector[2]
    if numar > 3:
        vector[1] = binar[-3]
        i1 = vector[1]
    if numar > 7:
        vector[0] = binar[-4]
        i0 = vector[0]

    return i0, i1, i2, i3

# Cod Andreea - zona 3
def output(i0, i1, i2, i3):

    baza_finala_introdusa = 10 # numar de citit de la tastatura
    baza_finala = baza_finala_introdusa

    rezultat_final = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for index in range(0,15):
        rezultat_final[index] = and_gate(i0, i1, i2, i3)

    rezultat = 0
    for index in range (0,15):
        rezultat += pow(baza_finala, index) * rezultat_final[index]

    print(rezultat)

#################################################################################
############# MAIN ##############################################################
#################################################################################

def main():
    i0, i1, i2, i3  = input()
    output(i0, i1, i2, i3)

main()