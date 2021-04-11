from tkinter import *

root= Tk()
root.title("Addition Calculator")

enter= Entry(root,width=35,borderwidth=3)
enter.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    #enter.delete(0,END)
    current= enter.get()
    enter.delete(0,END)
    enter.insert(0,str(current) + str(number))

def button_clear():
    enter.delete(0,END)

def button_add():
    first_number =enter.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    enter.delete(0,END)

def button_sub():
    first_number =enter.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    enter.delete(0,END)

def button_multi():
    first_number =enter.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    enter.delete(0,END)

def button_div():
    first_number =enter.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    enter.delete(0,END)
    

def button_equal():
    second_number =enter.get()
    enter.delete(0,END)
    if math == "addition":
        enter.insert(0,f_num+ int(second_number))
    if math == "subtraction":
        enter.insert(0,f_num - int(second_number))
    if math == "multiplication":
        enter.insert(0,f_num * int(second_number))
    if math == "divide":
        enter.insert(0,f_num / int(second_number))



One = Button(root,text=1,width=10,command=lambda:[button_click(1)])
One.grid(row=1,column=0)
Two = Button(root,text=2,width=10,command=lambda:[button_click(2)])
Two.grid(row=1,column=1)
Three = Button(root,text=3,width=10,command=lambda:[button_click(3)])
Three.grid(row=1,column=2)
Four = Button(root,text=4,width=10,command=lambda:[button_click(4)])
Four.grid(row=3,column=0)
Five = Button(root,text=5,width=10,command=lambda:[button_click(5)])
Five.grid(row=3,column=1)
Six = Button(root,text=6,width=10,command=lambda:[button_click(6)])
Six.grid(row=3,column=2)
Seven = Button(root,text=7,width=10,command=lambda:[button_click(7)])
Seven.grid(row=4,column=0)
Eight = Button(root,text=8,width=10,command=lambda:[button_click(8)])
Eight.grid(row=4,column=1)
Nine = Button(root,text=9,width=10,command=lambda:[button_click(9)])
Nine.grid(row=4,column=2)
Zero = Button(root,text=0,width=10,command=lambda:[button_click(0)])
Zero.grid(row=5,column=0)
add = Button(root,text="+",width=10,command=button_add,bg="lightyellow")
add.grid(row=5,column=1)
Clear = Button(root,text="Clear",width=10,command=button_clear)
Clear.grid(row=5,column=2)
Sub = Button(root,text="-",width=10,command=button_sub,bg="lightgreen")
Sub.grid(row=6,column=0)
multi = Button(root,text="*",width=10,command=button_multi,bg="lightblue3")
multi.grid(row=6,column=1)
div = Button(root,text="/",width=10,command=button_div,bg="salmon")
div.grid(row=6,column=2)
Eqaul = Button(root,text="=",width=35,command=button_equal,bg="thistle1")
Eqaul.grid(row=7,column=0,columnspan=3)



root.mainloop()