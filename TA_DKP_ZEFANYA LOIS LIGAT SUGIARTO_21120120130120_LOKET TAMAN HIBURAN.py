from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#KELUAR PROGRAM
def keluar():
    top.destroy()


#Pengecekan Input
def warning():
    if len (nama.get()) == 0:
        messagebox.showerror("ERROR", "SILAHKAN ISI NAMA ANDA TERLEBIH DAHULU")
        return
    if radio.get() == 0:
        messagebox.showerror("ERROR", "SILAHKAN PILIH GENDER")
        return
    if tinggi.get() == 0:
        messagebox.showerror("ERROR", "SILAHKAN ISI TINGGI BADAN ANDA")
        return
    if tinggi.get() == 2:
        top.destroy()
        page2b()
        return
    if tinggi.get() == 1:
        top.destroy()
        page2a()
        return


#PAGE 3
def next2(lst_wahana, total, page):
    if radio.get() == 1:
        depan ="Bapak"
    elif radio.get() == 2:
        depan ="Ibu"
    selamat= "Halo " + depan + " " + nama.get() + ","
    pilihan= "\nBerikut Wahana yang Anda Pilih:\n"
    semua_wahana = "\n"
    number = 1
    if len(lst_wahana) <= 0:
        semua_wahana = "\nBELUM ADA WAHANA YANG DIPILIH!\n"
    else:
        for i in lst_wahana:
            semua_wahana += f"{number}. {i}\n"
            number += 1
    total_harga = f"\nTotal Harga: Rp{str(total)},-"
    messagebox.showinfo("Fun Amusement Park", selamat + pilihan + semua_wahana + total_harga)
    if page == "a":
        page2a.top.destroy()
    else:
        page2b.top.destroy()


#PAGE 2A
def page2a():
    #Template 2
    page2a.top = Tk()
    page2a.top.geometry("350x350")
    page2a.top.title("Fun Amusement Park")
    #Label
    LBjudul = Label(page2a.top,text = "Selamat Datang di Taman Hiburan Fun Park").place(x = 60, y =10)
    LBpilih = Label(page2a.top,text = "Silahkan Pilih Wahana yang ingin Anda Naiki :\t").place(x = 30, y = 50)
    LBharga = Label(page2a.top,text = "=Harga Wahana=").place(x = 190, y = 70)
    #Harga Wahana
    harga1 = Label(page2a.top,text = "Rp35.000").place(x = 210, y = 90)
    harga2 = Label(page2a.top,text = "Rp50.000").place(x = 210, y = 110)
    harga3 = Label(page2a.top,text = "Rp40.000").place(x = 210, y = 130)
    harga4 = Label(page2a.top,text = "Rp55.000").place(x = 210, y = 150)
    harga5 = Label(page2a.top,text = "Rp60.000").place(x = 210, y = 170)
    #Daftar Wahana
    page2a.CheckVar1 = IntVar()
    page2a.CheckVar2 = IntVar()
    page2a.CheckVar3 = IntVar()
    page2a.CheckVar4 = IntVar()
    page2a.CheckVar5 = IntVar()
    c1 = Checkbutton(page2a.top, text = "Bom-Bom Car", variable=page2a.CheckVar1, onvalue=1, offvalue=0).place(x=30,y=90)
    c2 = Checkbutton(page2a.top, text = "Battle Star", variable=page2a.CheckVar2, onvalue=1, offvalue=0).place(x=30,y=110)
    c3 = Checkbutton(page2a.top, text = "Paranoia", variable=page2a.CheckVar3, onvalue=1, offvalue=0).place(x=30,y=130)
    c4 = Checkbutton(page2a.top, text = "Haunted House", variable=page2a.CheckVar4, onvalue=1, offvalue=0).place(x=30,y=150)
    c5 = Checkbutton(page2a.top, text = "Pandora Box", variable=page2a.CheckVar5, onvalue=1, offvalue=0).place(x=30,y=170)
    #NEXT Button
    btn3 = Button(page2a.top, command = hitung2a, text="NEXT").place(x=300, y=300)
#PAGE 2A Hitung
def hitung2a():
    total = 0
    lst_wahana = []
    if page2a.CheckVar1.get() == 1 :
        total += 35000
        lst_wahana.append("Bom-Bom Car")
    if page2a.CheckVar2.get() == 1 :
        total += 50000
        lst_wahana.append("Battle Star")
    if page2a.CheckVar3.get() == 1 :
        total += 40000
        lst_wahana.append("Paranoia")
    if page2a.CheckVar4.get() == 1 :
        total += 55000
        lst_wahana.append("Haunted House")
    if page2a.CheckVar5.get() == 1 :
        total += 60000
        lst_wahana.append("Pandora Box")
    next2(lst_wahana, total, "a")
    pass


#PAGE 2B
def page2b():
    #Template 2
    page2b.top = Tk()
    page2b.top.geometry("350x350")
    page2b.top.title("Fun Amusement Park")
    #Label
    LBjudul = Label(page2b.top,text = "Selamat Datang di Taman Hiburan Fun Park").place(x = 60, y =10)
    LBpilih = Label(page2b.top,text = "Silahkan Pilih Wahana yang ingin Anda Naiki :\t").place(x = 30, y = 50)
    LBharga = Label(page2b.top,text = "=Harga Wahana=").place(x = 190, y = 70)
    #Harga Wahana
    harga1 = Label(page2b.top,text = "Rp30.000").place(x = 210, y = 90)
    harga2 = Label(page2b.top,text = "Rp20.000").place(x = 210, y = 110)
    harga3 = Label(page2b.top,text = "Rp40.000").place(x = 210, y = 130)
    harga4 = Label(page2b.top,text = "Rp55.000").place(x = 210, y = 150)
    harga5 = Label(page2b.top,text = "Rp60.000").place(x = 210, y = 170)
    harga6 = Label(page2b.top,text = "Rp35.000").place(x = 210, y = 190)
    harga7 = Label(page2b.top,text = "Rp50.000").place(x = 210, y = 210)
    #Daftar Wahana
    page2b.CheckVar1 = IntVar()
    page2b.CheckVar2 = IntVar()
    page2b.CheckVar3 = IntVar()
    page2b.CheckVar4 = IntVar()
    page2b.CheckVar5 = IntVar()
    page2b.CheckVar6 = IntVar()
    page2b.CheckVar7 = IntVar()
    c1 = Checkbutton(page2b.top, text = "The Scream", variable= page2b.CheckVar1, onvalue=1, offvalue=0).place(x=30,y=90)
    c2 = Checkbutton(page2b.top, text = "Histeria", variable=page2b.CheckVar2, onvalue=1, offvalue=0).place(x=30,y=110)
    c3 = Checkbutton(page2b.top, text = "Paranoia", variable=page2b.CheckVar3, onvalue=1, offvalue=0).place(x=30,y=130)
    c4 = Checkbutton(page2b.top, text = "Haunted House", variable=page2b.CheckVar4, onvalue=1, offvalue=0).place(x=30,y=150)
    c5 = Checkbutton(page2b.top, text = "Pandora Box", variable=page2b.CheckVar5, onvalue=1, offvalue=0).place(x=30,y=170)
    c6 = Checkbutton(page2b.top, text = "Bom-Bom Car", variable=page2b.CheckVar6, onvalue=1, offvalue=0).place(x=30,y=190)
    c7 = Checkbutton(page2b.top, text = "Battle Star", variable=page2b.CheckVar7, onvalue=1, offvalue=0).place(x=30,y=210)
    #NEXT Button
    btn3 = Button(page2b.top, command = hitung2b, text="NEXT").place(x=300, y=300)
#PAGE 2B Hitung
def hitung2b():
    total = 0
    lst_wahana = []
    if page2b.CheckVar1.get() == 1 :
        total += 30000
        lst_wahana.append("The Scream")
    if page2b.CheckVar2.get() == 1 :
        total += 20000
        lst_wahana.append("Histeria")
    if page2b.CheckVar3.get() == 1 :
        total += 40000
        lst_wahana.append("Paranoia")
    if page2b.CheckVar4.get() == 1 :
        total += 55000
        lst_wahana.append("Haunted House")
    if page2b.CheckVar5.get() == 1 :
        total += 60000
        lst_wahana.append("Pandora Box")
    if page2b.CheckVar6.get() == 1 :
        total += 35000
        lst_wahana.append("Bom-Bom Car")
    if page2b.CheckVar7.get() == 1 :
        total += 50000
        lst_wahana.append("Battle Star")
    next2(lst_wahana, total, "b")
    pass


#Pengarahan Ke Pengecekan
def next1():
    warning()

#PAGE 1
#Template
top = Tk()  
top.geometry("350x350")
top.title("Fun Amusement Park")
#Input Data 
nama = StringVar()
Inama = Entry(top,width = 25, textvariable=nama).place(x = 110, y = 50)  
#Label
LBjudul = Label(top,text = "Selamat Datang di Taman Hiburan Fun Park").place(x = 60, y = 10)
LBnama = Label(text = "Nama\t: ").place(x = 30,y = 50)
LBjk = Label(text = "Gender\t:").place(x = 30, y=80)
LBtinggi = Label(text = "Tinggi\t:").place(x=30,y=150)
#Radio Button
radio = IntVar()
R1 = Radiobutton(top, text="Pria", variable=radio, value=1).place(x=105, y=80)  
R2 = Radiobutton(top, text="Wanita", variable=radio, value=2).place(x=105, y=100)  
R3 = Radiobutton(top, text="Lainnya", variable=radio, value=3).place(x=105, y=120) 
tinggi = IntVar()
Ra = Radiobutton(top,text="< 160 cm", variable=tinggi, value=1).place(x=105, y=150)
Rb = Radiobutton(top,text=">= 160 cm", variable=tinggi, value=2).place(x=105, y=170)
#NEXT & QUIT Button
btn1 = Button(top, command = next1, text="NEXT").place(x=300, y=300)
btn2 = Button(top, command = keluar, text="QUIT").place(x=250, y=300)


top.mainloop()
