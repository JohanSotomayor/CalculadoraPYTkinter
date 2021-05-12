# libreria de Interfaz grafica Tkinter integrada en Phyton
from  tkinter import Tk, Entry, Label, Grid, mainloop, Button
from tkinter.ttk import Combobox

Root = Tk() #Llamar a la ventana


Root.title("Calculadora Phyton" ) #Nombre ventana
Root.geometry("300x400") #Tamaño Calculadora
Root.config(background="red", ) #Color Fondo

#Interfaz

TxtTitle = Label(Root, text="0")
TxtTitle.grid(row=1, column=1, columnspan=3) 

Num1= Button(Root, text="1")
Num1.grid(row=2,column=1)
Num2= Button(Root, text="2")
Num2.grid(row=2,column=2)
Num3 = Button(Root, text="3")
Num3.grid(row=2,column=3)
Num4 = Button(Root, text="4")
Num4.grid(row=3,column=1)
Num5 = Button(Root, text="5")
Num5.grid(row=3,column=2)
Num6 = Button(Root , text="6")
Num6.grid(row=3,column=3)
Num7 = Button(Root , text="7")
Num7.grid(row=4,column=1)
Num8 = Button(Root , text="8")
Num8.grid(row=4,column=2)
Num9 = Button(Root , text="9")
Num9.grid(row=4,column=3)
Num0 = Button(Root , text="0")
Num0.grid(row=5,column=0, columnspan=3)






Root.mainloop() #Final del ciclo de la ventana


