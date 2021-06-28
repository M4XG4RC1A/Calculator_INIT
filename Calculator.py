#Import libraries
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame

#Start Screen
root=Tk()
root.title("Calculator")

#Start function for identify buttons
def setValue(id):
    translate = {11:'(',12:')',21:'-',22:'+',41:'.',51:'X',61:'*',62:'/'}
    if Value.get() == "Plotted":
        Value.set("")
    if id>=0 and id<=9:
        Value.set(Value.get()+str(id))
    if (id>=11 and id<=22) or (id==41) or (id==51) or (id>=61 and id<=62):
        Value.set(Value.get()+str(translate[id]))
    if id == 31:
        strVal = Value.get()
        Value.set(strVal[0:-1])
    if id == 32:
        if 'x' in Value.get():
            Value.set("Error")
        else:
            Value.set(eval(Value.get()))
    if id == 42:
        Value.set("")
    if id == 52:
        definition = ChangeEnt.get()
        startP = StartEnt.get()
        endP = EndEnt.get()
        f = lambda X: eval(Value.get())
        xdat = []
        for n in range(definition+1):
            xdat.append(startP+n*(endP-startP)/definition)
        ydat = []
        for i in xdat:
            ydat.append(f(i))
        data = {'X': xdat,
                'Y': ydat
                }
        plt.cla()
        df = DataFrame(data,columns=['X','Y'])
        df = df[['X','Y']].groupby('X').sum()
        ax.clear()
        df.plot(kind='line', legend=True, ax=ax, color='r',marker='o', fontsize=10)
        line = FigureCanvasTkAgg(figure, Principal)
        line.get_tk_widget().place(x=7*Small+5*Big,y=2*Small+0.25*Big)
        Value.set("Plotted")

#Stetic Variables
Small = 10
Big = 50
TotalY = Small*7 + Big*6
TotalX = Small*6 + Big*5
Bsize = (Big-(Big%15))/15
Bsize = 2

#Frame of Calculator
Principal = Frame(root, bg='black', width=TotalX*2, height=TotalY)
Principal.pack()

#Global Variables
Value = StringVar()
Value.set("")
StartEnt = IntVar()
StartEnt.set(0)
EndEnt = IntVar()
EndEnt.set(20)
ChangeEnt = IntVar()
ChangeEnt.set(50)

#Calculator Screen
T = Label(Principal,textvariable=Value,font="Helvetica 15 bold",width=Bsize*14,height=Bsize)
T.place(x=1*Small+0*Big,y=1*Small+0*Big)

#Calculator Buttons
B1 = Button(Principal,text="1",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(1))
B1.place(x=1*Small+0*Big,y=2*Small+1*Big)
B2 = Button(Principal,text="2",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(2))
B2.place(x=2*Small+1*Big,y=2*Small+1*Big)
B3 = Button(Principal,text="3",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(3))
B3.place(x=3*Small+2*Big,y=2*Small+1*Big)
BCO = Button(Principal,text="(",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(11))
BCO.place(x=4*Small+3*Big,y=2*Small+1*Big)
BCC = Button(Principal,text=")",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(12))
BCC.place(x=5*Small+4*Big,y=2*Small+1*Big)

B4 = Button(Principal,text="4",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(4))
B4.place(x=1*Small+0*Big,y=3*Small+2*Big)
B5 = Button(Principal,text="5",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(5))
B5.place(x=2*Small+1*Big,y=3*Small+2*Big)
B6 = Button(Principal,text="6",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(6))
B6.place(x=3*Small+2*Big,y=3*Small+2*Big)
BM = Button(Principal,text="-",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(21))
BM.place(x=4*Small+3*Big,y=3*Small+2*Big)
BP = Button(Principal,text="+",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(22))
BP.place(x=5*Small+4*Big,y=3*Small+2*Big)

B7 = Button(Principal,text="7",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(7))
B7.place(x=1*Small+0*Big,y=4*Small+3*Big)
B8 = Button(Principal,text="8",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(8))
B8.place(x=2*Small+1*Big,y=4*Small+3*Big)
B9 = Button(Principal,text="9",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(9))
B9.place(x=3*Small+2*Big,y=4*Small+3*Big)
BDel = Button(Principal,text="*",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(61))
BDel.place(x=4*Small+3*Big,y=4*Small+3*Big)
BE = Button(Principal,text="/",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(62))
BE.place(x=5*Small+4*Big,y=4*Small+3*Big)

B0 = Button(Principal,text="0",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(0))
B0.place(x=1*Small+0*Big,y=5*Small+4*Big)
BD = Button(Principal,text=".",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(41))
BD.place(x=2*Small+1*Big,y=5*Small+4*Big)
BC = Button(Principal,text="C",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(42))
BC.place(x=3*Small+2*Big,y=5*Small+4*Big)
BDel = Button(Principal,text="<-",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(31))
BDel.place(x=4*Small+3*Big,y=5*Small+4*Big)
BE = Button(Principal,text="=",font="Helvetica 15 bold",width=Bsize,height=Bsize,command=lambda:setValue(32))
BE.place(x=5*Small+4*Big,y=5*Small+4*Big)

BX = Button(Principal,text="X",font="Helvetica 15 bold",width=Bsize*4,height=Bsize,command=lambda:setValue(51))
BX.place(x=1*Small+0*Big,y=6*Small+5*Big)
BXP = Button(Principal,text="Plot",font="Helvetica 15 bold",width=Bsize*7,height=Bsize,command=lambda:setValue(52))
BXP.place(x=3*Small+2*Big,y=6*Small+5*Big)

#Figure for plot function
figure = plt.Figure(figsize=(5,5), dpi=(Small*4 + Big*5)/5)
ax = figure.add_subplot(111)
line = FigureCanvasTkAgg(figure, Principal)
line.get_tk_widget().place(x=7*Small+5*Big,y=2*Small+0.25*Big)
ax.set_title('Function Plot')

#Set parameters for plot
Label(Principal,text="Start",font="Helvetica 10 bold",fg="#FFF",bg="#000",justify='left').place(x=7*Small+5*Big,y=6*Small+5.5*Big)
EntStart = Entry(Principal,font="Helvetica 10 bold",width=4,textvariable=StartEnt)
EntStart.place(x=12*Small+5*Big,y=6*Small+5.5*Big)#7
Label(Principal,text="End",font="Helvetica 10 bold",fg="#FFF",bg="#000",justify='left').place(x=10*Small+7*Big,y=6*Small+5.5*Big)
EntEnd = Entry(Principal,font="Helvetica 10 bold",width=4,textvariable=EndEnt)
EntEnd.place(x=13*Small+7*Big,y=6*Small+5.5*Big)
Label(Principal,text="Rep",font="Helvetica 10 bold",fg="#FFF",bg="#000",justify='left').place(x=10*Small+9*Big,y=6*Small+5.5*Big)
EntStep = Entry(Principal,font="Helvetica 10 bold",width=4,textvariable=ChangeEnt)
EntStep.place(x=13*Small+9*Big,y=6*Small+5.5*Big)

#Define loop for root
root.mainloop()