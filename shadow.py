from tkinter import *
from tkinter import ttk
from tkinter import messagebox,Label
#global Variable
ActivePlayer=1
p1=[]
p2=[]

#Designing Interface##
    #Creating Dialog Box#
Box=Tk()
Box.title("Tic Tac Toe Developed BY ~Vikash")
    #####################

    #####  FIRST BUTTON  #######
bt1=ttk.Button(Box,text=' ')
bt1.grid(row=0,column=0,sticky=N,ipadx=40,ipady=40)
bt1.config(command=lambda:  ButtonClick(1))
    #####################

    #####  SECOND BUTTON  #######
bt2=ttk.Button(Box,text=' ')
bt2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bt2.config(command=lambda:  ButtonClick(2))
    #####################

    #####  THIRD BUTTON  #######
bt3=ttk.Button(Box,text=' ')
bt3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bt3.config(command=lambda:  ButtonClick(3))
    #####################

    #####  FOURTH BUTTON  #######
bt4=ttk.Button(Box,text=' ')
bt4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bt4.config(command=lambda:  ButtonClick(4))
    #####################

    #####  FIFTH BUTTON  #######
bt5=ttk.Button(Box,text=' ')
bt5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bt5.config(command=lambda:  ButtonClick(5))
    #####################

    #####  SIXTH BUTTON  #######
bt6=ttk.Button(Box,text=' ')
bt6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bt6.config(command=lambda:  ButtonClick(6))
    #####################

    #####  SEVENTH BUTTON  #######
bt7=ttk.Button(Box,text=' ')
bt7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bt7.config(command=lambda:  ButtonClick(7))
    #####################

    #####  EIGHT BUTTON  #######
bt8=ttk.Button(Box,text=' ')
bt8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bt8.config(command=lambda:  ButtonClick(8))
    #####################

    #####  NINETH BUTTON  #######
bt9=ttk.Button(Box,text=' ')
bt9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bt9.config(command=lambda:  ButtonClick(9))
reset=ttk.Button(Box,text='Reset')
reset.grid(row=3,column=0,sticky='snew',ipadx=10,ipady=10)
reset.config(command=ConnectionResetError)
def ButtonClick(id):
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
         # style=ttk.style()
         # style.theme_names()
         # style.them_naens()
         # ('aqua','clan','default','classic')
         # style.theme_use('classic')
         # style.configure('box',foreground='red')
         #    bt1.winfro
         # 'aqua'
         SetLayout(id,"X")
         p1.append(id)
         Box.title("Player First")
         ActivePlayer=2
         print("P1:{}".format(p1))
    elif(ActivePlayer==2):
        SetLayout(id,"O")
        p2.append(id )
        Box.title("Player Second")
        ActivePlayer=1
        print("P2:{}".format(p2))
    CheckWinner()
def SetLayout(id,PlayerSymbol):
    if id==1:
        bt1.config(text=PlayerSymbol)
        bt1.state(['disabled'])
    elif id==2:
        bt2.config(text=PlayerSymbol)
        bt2.state(['disabled'])
    elif id==3:
        bt3.config(text=PlayerSymbol)
        bt3.state(['disabled'])

    elif id==4:
        bt4.config(text=PlayerSymbol)
        bt4.state(['disabled'])
    elif id==5:
        bt5.config(text=PlayerSymbol)
        bt5.state(['disabled'])
    elif id==6:
        bt6.config(text=PlayerSymbol)
        bt6.state(['disabled'])
    elif id==7:
        bt7.config(text=PlayerSymbol)
        bt7.state(['disabled'])
    elif id==8:
        bt8.config(text=PlayerSymbol)
        bt8.state(['disabled'])
    elif id==9:
        bt9.config(text=PlayerSymbol)
        bt9.state(['disabled'])
def CheckWinner():
    winer=-1
    if((1 in p1) and (2 in p1) and (3 in p1)):
        winer=1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        winer = 2
    if((4 in p1) and (5 in p1) and (6 in p1)):
        winer=1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winer =2
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winer = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winer = 2

    if((1 in p1) and (4 in p1) and (7 in p1)):
        winer=1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winer =2

    if((2 in p1) and (5 in p1) and (8 in p1)):
        winer=1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winer =2
    if((3 in p1) and (6 in p1) and (9 in p1)):
        winer=1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winer=2
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winer=1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winer=2
    if((3 in p1) and (5 in p1) and (7in p1)):
        winer=1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        winer = 2
    if winer==1:
            messagebox.showinfo(title="Congrats.",message="Player First is the winner")
    elif winer==2:
            messagebox.showinfo(title="Congrats.", message="Player Second is the winner")
Box.mainloop()