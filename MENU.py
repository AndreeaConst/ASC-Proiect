import tkinter as tk
import tkinter
from tkinter import font  as tkfont
import PoartaAND, PoartaNOT
from tkinter import messagebox
from PIL import ImageTk,Image

NumarLabel = 0
Numar = 0
ok = 1 # daca ok = 0, atunci numarul in baza 8 se scrie pe mai mult de 4 biti, deci neconvertibil
a = [0,0,0,0]
baza_finala = 0
baza_initiala = 0


def imagineCircuit(string):
    nwin = tk.Toplevel()
    photo = ImageTk.PhotoImage(Image.open(string))
    label_nwin = tk.Label(nwin, image=photo)
    label_nwin.pack()
    nwin.mainloop()

def output(output0, output1, output2, output3, output4, output5, output6, output7, output8, output9,
           output10, output11, output12, output13, output14, output15):

    bit = 0

    if output0 == 1:
        bit = 0
    elif output1 == 1:
        bit = 1
    elif output2 == 1:
        bit = 2
    elif output3 == 1:
        bit = 3
    elif output4 == 1:
        bit = 4
    elif output5 == 1:
        bit = 5
    elif output6 == 1:
        bit = 6
    elif output7 == 1:
        bit = 7
    elif output8 == 1:
        bit = 8
    elif output9 == 1:
        bit = 9
    elif output10 == 1:
        bit = 10
    elif output11 == 1:
        bit = 11
    elif output12 == 1:
        bit = 12
    elif output13 == 1:
        bit = 13
    elif output14 == 1:
        bit = 14
    elif output15 == 1:
        bit = 15

    if baza_finala == 10:
        if baza_initiala == 2:
            tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(a) + ' din baza ' + str(baza_initiala)
                                        + ' convertit in baza ' + str(baza_finala) + ' este ' + str(bit))
        else:
             tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(Numar) + ' din baza ' + str(baza_initiala)
                                    + ' convertit in baza ' + str(baza_finala) + ' este ' + str(bit))
    elif baza_finala == 16:
        if bit == 10:
            if baza_initiala == 2:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(a) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('A'))
            else:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(Numar) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('A'))
        elif bit == 11:
            if baza_initiala == 2:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(a) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('B'))
            else:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(Numar) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('B'))
        elif bit == 12:
            if baza_initiala == 2:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(a) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('C'))
            else:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(Numar) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('C'))
        elif bit == 13:
            if baza_initiala == 2:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(a) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('D'))
            else:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(Numar) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('D'))
        elif bit == 14:
            if baza_initiala == 2:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(a) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('E'))
            else:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(Numar) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('E'))
        elif bit == 15:
            if baza_initiala == 2:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(a) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('F'))
            else:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(Numar) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str('F'))
        else:
            if baza_initiala == 2:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(a) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str(bit))
            else:
                tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(Numar) + ' din baza ' + str(baza_initiala)
                                            + ' convertit in baza ' + str(baza_finala) + ' este ' + str(bit))
    else:
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # a contine numarul convertit in baza de numeratie finala

        i = -1
        while int(bit) != 0:
            i += 1
            b[i] = int(bit % baza_finala)
            bit = int(bit / baza_finala)

        rezultat = 0
        index = i
        while index > -1:
            rezultat = rezultat * 10 + b[index]
            index -= 1

        if baza_initiala == 2:
            tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(a) + ' din baza ' + str(baza_initiala)
                                        + ' convertit in baza ' + str(baza_finala) + ' este ' + str(rezultat))
        else:
            tkinter.messagebox.showinfo('REZULTAT', 'Numarul ' + str(Numar) + ' din baza ' + str(baza_initiala)
                                        + ' convertit in baza ' + str(baza_finala) + ' este ' + str(rezultat))


def Circuit():
    # a este vector care contine bitii din baza 2, in urma transformarii numarului citit de
    # la tastatura, din baza x in baza 2

    # poarta NOT are intrarea A si iesirea B
    # poarta AND  are intrarile A,B,C,D si iesirea E

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


    output0 = (AND0.E.valoare_bit)
    output1 = (AND1.E.valoare_bit)
    output2 = (AND2.E.valoare_bit)
    output3 = (AND3.E.valoare_bit)
    output4 = (AND4.E.valoare_bit)
    output5 = (AND5.E.valoare_bit)
    output6 = (AND6.E.valoare_bit)
    output7 = (AND7.E.valoare_bit)
    output8 = (AND8.E.valoare_bit)
    output9 = (AND9.E.valoare_bit)
    output10 = (AND10.E.valoare_bit)
    output11 = (AND11.E.valoare_bit)
    output12 = (AND12.E.valoare_bit)
    output13 = (AND13.E.valoare_bit)
    output14 = (AND14.E.valoare_bit)
    output15 = (AND15.E.valoare_bit)

    output(output0, output1, output2, output3, output4, output5, output6, output7, output8,
           output9, output10, output11, output12, output13, output14, output15)

    if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
        imagineCircuit("./pictures/0.jpg")
    elif a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 1:
        imagineCircuit("./pictures/1.jpg")
    elif a[0] == 0 and a[1] == 0 and a[2] == 1 and a[3] == 0:
        imagineCircuit("./pictures/2.jpg")
    elif a[0] == 0 and a[1] == 0 and a[2] == 1 and a[3] == 1:
        imagineCircuit("./pictures/3.jpg")
    elif a[0] == 0 and a[1] == 1 and a[2] == 0 and a[3] == 0:
        imagineCircuit("./pictures/4.jpg")
    elif a[0] == 0 and a[1] == 1 and a[2] == 0 and a[3] == 1:
        imagineCircuit("./pictures/5.jpg")
    elif a[0] == 0 and a[1] == 1 and a[2] == 1 and a[3] == 0:
        imagineCircuit("./pictures/6.jpg")
    elif a[0] == 0 and a[1] == 1 and a[2] == 1 and a[3] == 1:
        imagineCircuit("./pictures/7.jpg")
    elif a[0] == 1 and a[1] == 0 and a[2] == 0 and a[3] == 0:
        imagineCircuit("./pictures/8.jpg")
    elif a[0] == 1 and a[1] == 0 and a[2] == 0 and a[3] == 1:
        imagineCircuit("./pictures/9.jpg")
    elif a[0] == 1 and a[1] == 0 and a[2] == 1 and a[3] == 0:
        imagineCircuit(".pictures/10.jpg")
    elif a[0] == 1 and a[1] == 0 and a[2] == 1 and a[3] == 1:
        imagineCircuit("./pictures/11.jpg")
    elif a[0] == 1 and a[1] == 1 and a[2] == 0 and a[3] == 0:
        imagineCircuit("./pictures/12.jpg")
    elif a[0] == 1 and a[1] == 1 and a[2] == 0 and a[3] == 1:
        imagineCircuit("./pictures/13.jpg")
    elif a[0] == 1 and a[1] == 1 and a[2] == 1 and a[3] == 0:
        imagineCircuit("./pictures/14.jpg")
    elif a[0] == 1 and a[1] == 1 and a[3] == 1 and a[4] == 1:
        imagineCircuit("./pictures/15.jpg")




root = tk.Tk()
def MESAJ():
    global a
    a[0] = 0
    a[1] = 0
    a[2] = 0
    a[3] = 0

    if baza_initiala == 0 or baza_finala == 0:
        tkinter.messagebox.showerror('EROARE', 'Nu ati selectat o baza! Incercati din nou!')
    else:
        root1 = tk.Tk()
        global Numar, NumarLabel
        Numar = NumarLabel = 0

        def transforma_baza2():
            i = 4
            global a, Numar

            if baza_initiala == 8:
                if NumarLabel > 15:
                    tkinter.messagebox.showerror('EROARE', 'Numar neconvertibil in circuitul prezent! '
                                                           'Numarul se scrie pe mai mult de 4 biti!')
                    return
                if NumarLabel > 8:
                    Numar = NumarLabel

            copieNumar = Numar

            while int(copieNumar) != 0:

                i -= 1
                a[i] = int(copieNumar % 2)
                copieNumar = int(copieNumar / 2)

            Circuit()

        def changeValueMinus(index, button1, button2, btn_pin):
            global a
            a[index] = 0
            button1['state'] = 'disabled'
            button2['state'] = 'normal'
            btn_pin.config(text=a[index])
            label_a.config(text=a)
            # print(a)
            return

        def changeValuePlus(index, button1, button2, btn_pin):
            global a
            a[index] = 1
            button1['state'] = 'normal'
            button2['state'] = 'disabled'
            btn_pin.config(text=a[index])
            label_a.config(text=a)
            # print(a)
            return

        def label_baza16():
            global NumarLabel
            if Numar == 10:
                NumarLabel = "A"
            elif Numar == 11:
                NumarLabel = "B"
            elif Numar == 12:
                NumarLabel = "C"
            elif Numar == 13:
                NumarLabel = "D"
            elif Numar == 14:
                NumarLabel = "E"
            elif Numar == 15:
                NumarLabel = "F"

        def label_baza8():
            global NumarLabel
            if Numar == 8:
                NumarLabel = 10
            elif Numar == 9:
                NumarLabel = 11
            elif Numar == 10:
                NumarLabel = 12
            elif Numar == 11:
                NumarLabel = 13
            elif Numar == 12:
                NumarLabel = 14
            elif Numar == 13:
                NumarLabel = 15
            elif Numar == 14:
                NumarLabel = 16
            elif Numar == 15:
                NumarLabel = 17

        def changeNumberMinus(button1, button2, btn_pin):
            global Numar,NumarLabel
            if Numar - 1 >= 0:
                Numar -= 1
                button2['state'] = 'normal'
                btn_pin.config(text=Numar)
                if baza_initiala == 8:
                   label_baza8()
                   if Numar > 7:
                     label_Numar.config(text="Baza initiala 8 : " + str(NumarLabel))
                     label_Numar.place(x=115, y=230)
                   else:
                    label_Numar.config(text="Baza initala 8 : " + str(Numar))
                    label_Numar.place(x=115, y=230)

                elif baza_initiala == 10:
                    label_Numar.config(text="Baza initiala 10 : " + str(Numar))
                    label_Numar.place(x=115, y=230)
                elif baza_initiala == 16:
                    label_baza16()
                    if Numar > 9:
                        label_Numar.config(text="Baza initiala 16 : " + str(NumarLabel))
                        label_Numar.place(x=115, y=230)
                    else:
                        label_Numar.config(text="Baza initiala 16 : " + str(Numar))
                        label_Numar.place(x=115, y=230)
            else:
                button1['state'] = 'disabled'
            #print(Numar)
            return

        def changeNumberPlus(button1, button2, btn_pin):
            global Numar,NumarLabel
            if Numar + 1 <= 15:
                Numar += 1
                button1['state'] = 'normal'
                btn_pin.config(text=Numar)
                if baza_initiala == 8:
                   label_baza8()
                   if Numar > 7:
                       label_Numar.config(text="Baza initiala 8 : " + str(NumarLabel))
                       label_Numar.place(x = 115, y = 230)
                   else:
                       label_Numar.config(text="Baza initiala 8 : " + str(Numar))
                       label_Numar.place(x=115, y=230)
                elif baza_initiala == 10:
                    label_Numar.config(text="Baza initiala 10 : " + str(Numar))
                    label_Numar.place(x=115, y=230)
                elif baza_initiala == 16:
                    label_baza16()
                    if Numar > 9:
                        label_Numar.config(text="Baza initiala 16 : " + str(NumarLabel))
                        label_Numar.place(x=115, y=230)
                    else:
                        label_Numar.config(text="Baza initiala 16 : " + str(Numar))
                        label_Numar.place(x=115, y=230)

            else:
                button2['state'] = 'disabled'
            #print(Numar)
            return

        if baza_initiala == 2:
            # 0
            label_a = tk.Label(root1, text=a)
            label_a.place(x=150, y=230)

            btn_pin0 = tk.Button(root1, text='bit 3', width=4, state='disabled', bg="white")
            btn_pin0.place(x=30, y=10)
            btn_minus0 = tk.Button(root1, text="-", state='disabled', bg='maroon1', fg='navy',
                                   command=lambda: changeValueMinus(0, btn_minus0, btn_plus0, btn_pin0))
            btn_minus0.place(x=30, y=40)
            btn_plus0 = tk.Button(root1, text="+", fg="red2", bg='SkyBlue1',
                                  command=lambda: changeValuePlus(0, btn_minus0, btn_plus0, btn_pin0))
            btn_plus0.place(x=50, y=40)

            # 1
            btn_pin1 = tk.Button(root1, text='bit 2', width=4, state='disabled', bg="white")
            btn_pin1.place(x=30, y=90)
            btn_minus1 = tk.Button(root1, text="-", state='disabled', bg='maroon1', fg='navy',
                                   command=lambda: changeValueMinus(1, btn_minus1, btn_plus1, btn_pin1))
            btn_minus1.place(x=30, y=120)
            btn_plus1 = tk.Button(root1, text="+", fg="red2", bg='SkyBlue1',
                                  command=lambda: changeValuePlus(1, btn_minus1, btn_plus1, btn_pin1))
            btn_plus1.place(x=50, y=120)

            # 2
            btn_pin2 = tk.Button(root1, text='bit 1', width=4, state='disabled', bg="white")
            btn_pin2.place(x=30, y=170)
            btn_minus2 = tk.Button(root1, text="-", state='disabled', bg='maroon1', fg='navy',
                                   command=lambda: changeValueMinus(2, btn_minus2, btn_plus2, btn_pin2))
            btn_minus2.place(x=30, y=200)
            btn_plus2 = tk.Button(root1, text="+", fg="red2", bg='SkyBlue1',
                                  command=lambda: changeValuePlus(2, btn_minus2, btn_plus2, btn_pin2))
            btn_plus2.place(x=50, y=200)

            # 3
            btn_pin3 = tk.Button(root1, text='bit 0', width=4, state='disabled', bg="white")
            btn_pin3.place(x=30, y=250)
            btn_minus3 = tk.Button(root1, text="-", state='disabled', bg='maroon1', fg='navy',
                                   command=lambda: changeValueMinus(3, btn_minus3, btn_plus3, btn_pin3))
            btn_minus3.place(x=30, y=280)
            btn_plus3 = tk.Button(root1, text="+", fg="red2", bg='SkyBlue1',
                                  command=lambda: changeValuePlus(3, btn_minus3, btn_plus3, btn_pin3))
            btn_plus3.place(x=50, y=280)

            btn_convert = tk.Button(root1, text="Converteste", width=10, height=3, bg='SkyBlue1', command=Circuit)
            btn_convert.place(x=300, y=100)


        else:
            # transformare numar din baza initiala in baza 2

            label_Numar = tk.Label(root1, text=Numar)
            label_Numar.place(x=150, y=230)

            btn_pin = tk.Button(root1, text='NUMAR', state='disabled', width=17, height = 5, bg="white")
            btn_pin.place(x=100, y=90)
            btn_minus = tk.Button(root1, text="-", bg='maroon1', fg='navy', state = 'disabled', width = 7, height = 2,
                                   command=lambda: changeNumberMinus(btn_minus, btn_plus, btn_pin))
            btn_minus.place(x=100, y=176)
            btn_plus = tk.Button(root1, text="+", fg="red2", bg='SkyBlue1', width = 8, height = 2,
                                  command=lambda: changeNumberPlus(btn_minus, btn_plus, btn_pin))
            btn_plus.place(x=160, y=176)

            btn_convert = tk.Button(root1, text="Converteste", width=10, height=3, bg='SkyBlue1',
                                    command=transforma_baza2)
            btn_convert.place(x=300, y=100)

        btn_quit = tk.Button(root1, text="Exit", width=10, height=3, bg='Purple', command=root1.destroy)
        btn_quit.place(x=300, y=220)

        root1.geometry("450x340")
        root1.mainloop()

def setValueInitial(baza):
    global baza_initiala
    baza_initiala = baza
    label_mesaj = tk.Label(root, text="Baza initiala selectata este " + str(baza_initiala))
    label_mesaj.place(x=50, y=320)
    #print(baza_initiala)

def setValueFinal(baza):
    global baza_finala
    baza_finala = baza
    label_mesaj = tk.Label(root, text="Baza finala selectata este " + str(baza_finala))
    label_mesaj.place(x=260, y=320)
    #print(baza_finala)


label_baze = tk.Label(root, text = "Selectati baza initiala")
label_baze.place(x = 60, y = 90)
Baza2 = tk.Button(root,text = "Baza 2", bg = "white",command = lambda:setValueInitial(2))
Baza2.place(x = 90,y = 120)
Baza8 = tk.Button(root,text = "Baza 8", bg = "white",command = lambda:setValueInitial(8))
Baza8.place(x = 90,y = 170)
Baza10 = tk.Button(root,text = "Baza 10", bg = "white",command = lambda:setValueInitial(10))
Baza10.place(x = 90,y = 220)
Baza16 = tk.Button(root,text = "Baza 16", bg = "white",command = lambda:setValueInitial(16))
Baza16.place(x = 90,y = 270)


label_baze = tk.Label(root, text = "Selectati baza finala")
label_baze.place(x = 270, y = 90)
baza2 = tk.Button(root,text = "Baza 2", bg = "white", command = lambda:setValueFinal(2))
baza2.place(x = 300,y = 120)
baza8 = tk.Button(root,text = "Baza 8", bg = "white", command = lambda:setValueFinal(8))
baza8.place(x = 300,y = 170)
baza10 = tk.Button(root,text = "Baza 10", bg = "white",command = lambda:setValueFinal(10))
baza10.place(x = 300,y = 220)
baza16 = tk.Button(root,text = "Baza 16", bg = "white",command = lambda:setValueFinal(16))
baza16.place(x = 300,y = 270)

title_font = tkfont.Font(family = 'Helvetica', size = 24, weight = "bold", slant = "italic")
label_titlu = tk.Label(root, text = "DECODOR", font = title_font)
label_titlu.pack()

btn_alege_numar = tk.Button(root, text = "Alege numar",width = 10, height = 3, bg = "SkyBlue1", command = MESAJ)
btn_alege_numar.place(x = 450, y = 130)
btn_quit = tk.Button (root, text = "Exit",width = 10, height = 3, bg = "purple", command = root.destroy)
btn_quit.place(x = 450, y = 237)

root.geometry("550x400")
root.mainloop()
