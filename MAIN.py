import PoartaNOT, PoartaAND

def Circuit(a):

    # a este vector care contine bitii din baza 2, in urma transformarii numarului citit de
    # la tastatura, din baza x in baza 2

    #poarta NOT are intrarea A si iesirea B
    #poarta AND  are intrarile A,B,C,D si iesirea E

    NOT0 = PoartaNOT.Not('NOT0')
    NOT0.B.vezi_output = 1

    NOT1 = PoartaNOT.Not('NOT1')
    NOT1.B.vezi_output = 1

    NOT2 = PoartaNOT.Not('NOT2')
    NOT2.B.vezi_output = 1

    NOT3 = PoartaNOT.Not('NOT3')
    NOT3.B.vezi_output = 1

    AND0 = PoartaAND.And('AND0')
    AND0.E.vezi_output = 1
    NOT0.B.conecteaza(AND0.A)
    NOT1.B.conecteaza(AND0.B)
    NOT2.B.conecteaza(AND0.C)
    NOT3.B.conecteaza(AND0.D)

    AND1 = PoartaAND.And('AND1')
    AND1.E.vezi_output = 1
    NOT0.B.conecteaza(AND1.A)
    NOT1.B.conecteaza(AND1.B)
    NOT2.B.conecteaza(AND1.C)
    AND1.D.set(a[3])

    AND2 = PoartaAND.And('AND2')
    AND2.E.vezi_output = 1
    NOT0.B.conecteaza(AND2.A)
    NOT1.B.conecteaza(AND2.B)
    AND2.C.set(a[2])
    NOT3.B.conecteaza(AND2.D)

    AND3 = PoartaAND.And('AND3')
    AND3.E.vezi_output = 1
    NOT0.B.conecteaza(AND3.A)
    NOT1.B.conecteaza(AND3.B)
    AND3.C.set(a[2])
    AND3.D.set(a[3])

    AND4 = PoartaAND.And('AND4')
    AND4.E.vezi_output = 1
    NOT0.B.conecteaza(AND4.A)
    AND4.B.set(a[1])
    NOT2.B.conecteaza(AND4.C)
    NOT3.B.conecteaza(AND4.D)

    AND5 = PoartaAND.And('AND5')
    AND5.E.vezi_output = 1
    NOT0.B.conecteaza(AND5.A)
    AND5.B.set(a[1])
    NOT2.B.conecteaza(AND5.C)
    AND5.D.set(a[3])

    AND6 = PoartaAND.And('AND6')
    AND6.E.vezi_output = 1
    NOT0.B.conecteaza(AND6.A)
    AND6.B.set(a[1])
    AND6.C.set(a[2])
    NOT3.B.conecteaza(AND6.D)

    AND7 = PoartaAND.And('AND7')
    AND7.E.vezi_output = 1
    NOT0.B.conecteaza(AND7.A)
    AND7.B.set(a[1])
    AND7.C.set(a[2])
    AND7.D.set(a[3])

    AND8 = PoartaAND.And('AND8')
    AND8.E.vezi_output = 1
    AND8.A.set(a[0])
    NOT1.B.conecteaza(AND8.B)
    NOT2.B.conecteaza(AND8.C)
    NOT3.B.conecteaza(AND8.D)

    AND9 = PoartaAND.And('AND9')
    AND9.E.vezi_output = 1
    AND9.A.set(a[0])
    NOT1.B.conecteaza(AND9.B)
    NOT2.B.conecteaza(AND9.C)
    AND9.D.set(a[3])

    AND10 = PoartaAND.And('AND10')
    AND10.E.vezi_output = 1
    AND10.A.set(a[0])
    NOT1.B.conecteaza(AND10.B)
    AND10.C.set(a[2])
    NOT3.B.conecteaza(AND10.D)

    AND11 = PoartaAND.And('AND11')
    AND11.E.vezi_output = 1
    AND11.A.set(a[0])
    NOT1.B.conecteaza(AND11.B)
    AND11.C.set(a[2])
    AND11.D.set(a[3])

    AND12 = PoartaAND.And('AND12')
    AND12.E.vezi_output = 1
    AND12.A.set(a[0])
    AND12.B.set(a[1])
    NOT2.B.conecteaza(AND12.C)
    NOT3.B.conecteaza(AND12.D)

    AND13 = PoartaAND.And('AND13')
    AND13.E.vezi_output = 1
    AND13.A.set(a[0])
    AND13.B.set(a[1])
    NOT2.B.conecteaza(AND13.C)
    AND13.D.set(a[3])

    AND14 = PoartaAND.And('AND14')
    AND14.E.vezi_output = 1
    AND14.A.set(a[0])
    AND14.B.set(a[1])
    AND14.C.set(a[2])
    NOT3.B.conecteaza(AND14.D)

    AND15 = PoartaAND.And('AND15')
    AND15.E.vezi_output = 1
    AND15.A.set(a[0])
    AND15.B.set(a[1])
    AND15.C.set(a[2])
    AND15.D.set(a[3])

    NOT0.A.set(a[0])
    NOT1.A.set(a[1])
    NOT2.A.set(a[2])
    NOT3.A.set(a[3])

    print(AND0.E.valoare_bit)
    print(AND1.E.valoare_bit)
    print(AND2.E.valoare_bit)
    print(AND3.E.valoare_bit)
    print(AND4.E.valoare_bit)
    print(AND5.E.valoare_bit)
    print(AND6.E.valoare_bit)
    print(AND7.E.valoare_bit)
    print(AND8.E.valoare_bit)
    print(AND9.E.valoare_bit)
    print(AND10.E.valoare_bit)
    print(AND11.E.valoare_bit)
    print(AND12.E.valoare_bit)
    print(AND13.E.valoare_bit)
    print(AND14.E.valoare_bit)
    print(AND15.E.valoare_bit)


def main():
    numar = 15  # numar de citit de la tastatura
    a = [0,0,0,0] # transformare numar din baza initiala in baza 2

    i = 4
    while int(numar) != 0:
        i -= 1
        a[i] = int(numar % 2)
        numar = int(numar/2)

    Circuit(a)

main()