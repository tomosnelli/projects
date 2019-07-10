from tkinter import *
window = Tk()

def convertkg():
	grams = float(kg.get())*1000
	pounds = float(kg.get())*2.20462
	ounces = float(kg.get())*35.274
	g1.delete("1.0", END)
	g1.insert(END, grams, "grams")
	p1.delete("1.0", END)
	p1.insert(END, pounds)
	o1.delete("1.0", END)
	o1.insert(END, ounces)

b1 = Button(window, text = "Convert", command = convertkg)
b1.grid()

kg = StringVar()

e1 = Entry(window, textvariable = kg)
e1.grid(row=0,column=2)

g1 = Text(window, height=1, width=20)
g1.grid(row=1,column=0)

p1 = Text(window, height=1, width=20)
p1.grid(row=1,column=1)

o1 = Text(window, height=1, width=20)
o1.grid(row=1,column=2)

window.mainloop()
