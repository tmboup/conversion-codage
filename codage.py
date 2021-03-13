#writen by Talla 
#coding : utf-8


from tkinter import *
from tkinter.messagebox import showwarning

def decimalBinary(value_10) :
    bin = list()
    if int(value_10) == 0 :
        bin = 0
    else : 
        try :
            value_10 = int(value_10) 
            while(value_10 !=0):
                bin += [value_10%2]
                value_10 //=2
            bin.reverse()
        except ValueError :
            showwarning("Erreur","Les données saisies ne peuvent qu'être que des entiers")
    return bin

def decimalOctal(value_10) :
    octal = list()
    if int(value_10) == 0 :
        octal = 0 #on affecte octal à la valeur 0
    else : 
        try :
            value_10 = int(value_10)
            while(value_10 != 0 ) :
                octal += [value_10%8]
                value_10 //= 8
            octal.reverse() 
        except ValueError :
            showwarning("Erreur","Les données saisies ne peuvent qu'être que des entiers") 
    return octal

def decimalHexadecimal(value_10) :
    hexa = list()
    if int(value_10) == 0 :
        hexa = 0
    else :
        try :
            value_10 = int(value_10)
            while (value_10 != 0 ) :
                t = value_10%16
                if t == 10 :
                    t = "A"
                elif t == 11 :
                    t = "B"
                elif t == 12 :
                    t = "C"
                elif t == 13 :
                    t = "D"
                elif t == 14 :
                    t = "E"
                elif t == 15 :
                    t = "F"
                else :
                    pass
                hexa += [t]
                value_10 //= 16
            hexa.reverse()
        except ValueError :
            showwarning("Erreur","les données saisies doivent être des entiers")
    return hexa

def binaryDecimal(binaire) :
    if int(binaire) == 0 :
        decimalValue = 0
    else :
        try :
            binaire = list(binaire) # convertie n liste
            binaire.reverse()
            decimalValue,indexValue = 0,0 
            for element in binaire :
                element = int(element)
                decimalValue += element*(2**indexValue)
                indexValue +=1
        except ValueError :
            showwarning("Erreur","les données saisies doivent être des entiers")
    return decimalValue

def octalDecimal(octal) :
    if int(octal) == 0 :
        decimalValue = 0
    else :
        try :
            octal = list(octal) # convrtie en liste
            octal.reverse()
            decimalValue,indexValue = 0,0 
            for element in octal :
                element = int(element)
                decimalValue += element*(8**indexValue)
                indexValue +=1
        except ValueError :
            showwarning("Erreur","les données saisies doivent être des entiers")
    return decimalValue

def hexadecimalDecimal(hexadecimal) :
    if int(hexadecimal) == 0 :
        decimalValue = 0
    else :
        hexadecimal = list(hexadecimal) # convrtie n liste
        hexadecimal.reverse()
        decimalValue,indexValue = 0,0 
        for element in hexadecimal :
            if element == "A" :
                element = 10
            elif element == "B" :
                element = 11
            elif element == "C" :
                element = 12
            elif element == "D" :
                element = 13
            elif element == "E" :
                element = 14
            elif element == "F" :
                element = 15
            else :
                pass
            element = int(element)
            decimalValue += element*(16**indexValue)
            indexValue +=1
    return decimalValue

def convert() :
    getValue = str(entry2.get())

    #decimal vers les autres bases
    if spinbox2.get() == "Decimal" and spinbox1.get() == "Binary" :
        entry3.delete(0,END)
        entry3.insert(0,decimalBinary(getValue))
    elif spinbox2.get() == "Decimal" and spinbox1.get() == "Octal" :
        entry3.delete(0,END)
        entry3.insert(0,decimalOctal(getValue))
    elif spinbox2.get() == "Decimal" and spinbox1.get() == "Hexadecimal" :
        entry3.delete(0,END)
        entry3.insert(0,decimalHexadecimal(getValue))

    #binaire vers les autres bases
    elif spinbox2.get() == "Binary" and spinbox1.get() == "Decimal" :
        entry3.delete(0,END)
        entry3.insert(0,binaryDecimal(getValue))
    elif spinbox2.get() == "Binary" and spinbox1.get() == "Octal" :
        entry3.delete(0,END)
        entry3.insert(0,decimalOctal(binaryDecimal(getValue)))
    elif spinbox2.get() == "Binary" and spinbox1.get() == "Hexadecimal" :
        entry3.delete(0,END)
        entry3.insert(0,decimalHexadecimal(binaryDecimal(getValue)))
    
    #octal vers les autres bases
    elif spinbox2.get() == "Octal" and spinbox1.get() == "Decimal" :
        entry3.delete(0,END)
        entry3.insert(0,octalDecimal(getValue))
    elif spinbox2.get() == "Octal" and spinbox1.get() == "Binary" :
        entry3.delete(0,END)
        entry3.insert(0,decimalBinary(octalDecimal(getValue)))
    elif spinbox2.get() == "Octal" and spinbox1.get() == "Hexadecimal" :
        entry3.delete(0,END)
        entry3.insert(0,decimalHexadecimal(octalDecimal(getValue)))

    #hexadecimal vers les autres bases
    elif spinbox2.get() == "Hexadecimal" and spinbox1.get() == "Decimal" :
        entry3.delete(0,END)
        entry3.insert(0,hexadecimalDecimal(getValue))
    elif spinbox2.get() == "Hexadecimal" and spinbox1.get() == "Binary" :
        entry3.delete(0,END)
        entry3.insert(0,decimalBinary(hexadecimalDecimal(getValue)))
    elif spinbox2.get() == "Hexadecimal" and spinbox1.get() == "Octal" :
        entry3.delete(0,END)
        entry3.insert(0,decimalOctal(hexadecimalDecimal(getValue)))
    #vers les bases identiques
    elif spinbox2.get() == "Decimal" and spinbox1.get() == "Decimal" :
        entry3.delete(0,END)
        entry3.insert(0,entry2.get())
    elif spinbox2.get() == "Binary" and spinbox1.get() == "Binary" :
        entry3.delete(0,END)
        entry3.insert(0,entry2.get())
    elif spinbox2.get() == "Octal" and spinbox1.get() == "Octal" :
        entry3.delete(0,END)
        entry3.insert(0,entry2.get())
    elif spinbox2.get() == "Hexadecimal" and spinbox1.get() == "Hexadecimal" :
        entry3.delete(0,END)
        entry3.insert(0,entry2.get())
    else :
         showwarning("Erreur","le commande n'est pas disponible. Veillez bien verifié votre choix")

def clearInput():
    entry2.delete(0,END)
    entry3.delete(0,END)
    
window = Tk()
window.title("Base conversion")
window.geometry("1000x730")
window.minsize(480, 360)
window.maxsize(600,500)
#"window.iconbitmap("")
window.config(background="#14B77F")

frame1=Frame(window, bg="#14B77F",relief=SUNKEN,bd=1)
frame1.pack(padx=10,pady=10)

frame2=Frame(frame1, bg="#14B77F",relief=SUNKEN,bd=0)
frame2.pack(side=TOP,padx=5,pady=5)

frame3=Frame(frame1, bg="#14B77F",relief=SUNKEN,bd=0)
frame3.pack(side=TOP,padx=5,pady=5)

frame4=Frame(frame1, bg="#14B77F",relief=SUNKEN,bd=0)
frame4.pack(side=TOP,padx=5,pady=5)

frame5=Frame(frame1, bg="#14B77F",relief=SUNKEN,bd=0)
frame5.pack(side=BOTTOM,padx=5,pady=5)


label2 = Label(frame2,bg="#14B77F",fg="white",text="Select",font=("Courrier",15))
label2.pack(side=LEFT,padx=5,pady=5)
#on doit modifier ici 
spinbox1 = Spinbox(frame2,values=('Decimal','Binary','Octal','Hexadecimal'),state='readonly',width=18)
spinbox1.pack(side = RIGHT,padx=5,pady=5)
label2 = Label(frame2,bg="#41B77F",fg="white",text=" to ",font=("Courrier",10),width=3)
label2.pack(side = RIGHT,padx=5,pady=5)
spinbox2 = Spinbox(frame2,values=('Decimal','Binary','Octal','Hexadecimal'),state='readonly',width=17)
spinbox2.pack(side = RIGHT,padx=5,pady=5)

label3 = Label(frame3,bg="#14B77F",fg="white",text="Value",font=("Courrier",15))
label3.pack(side=LEFT,padx=5,pady=5)
entry2 = Entry(frame3,bg="white",fg="black",width=45)
entry2.pack(side=RIGHT,padx=5,pady=5)

label4 = Label(frame4,bg="#14B77F",fg="white",text="Result",font=("Courrier",15))
label4.pack(side=LEFT,padx=5,pady=5)
entry3 = Entry(frame4,bg="white",fg="black",width=45)
entry3.pack(side=RIGHT,padx=5,pady=5)

bouton1 = Button(frame5,bg="#14B77F",fg="white",text="Convert",font=("Courrier",20),command=convert)
bouton1.pack(side=RIGHT,padx=5,pady=5)

bouton2 = Button(frame5,bg="#14B77F",fg="white",text="Delete",font=("Courrier",20),command=clearInput)
bouton2.pack(side=LEFT,padx=5,pady=5)

main_menu = Menu(window)
first_menu = Menu(main_menu,tearoff=0)
first_menu.add_command(label="À propos")
first_menu.add_command(label="Quitter",command=window.quit)

main_menu.add_cascade(label="Options",menu=first_menu)
window.config(menu=main_menu)
window.mainloop()