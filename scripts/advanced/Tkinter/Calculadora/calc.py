from tkinter import *
from math import sqrt

class GUI(Tk):
    def __init__(self):
        self.VC = 0
        super().__init__()
        self.title('Calculadora')
        self.geometry("1010x1970")
        self.entry = Entry(self, width=40)
        self.entry.grid(row=0, column=0, columnspan=35, ipady=65)
        self.b1 = Button(self, text="1", command=self.ev1, bg="white", fg="black",height=6, width=6)
        self.b1.grid(row=2,column=0)
        self.b2 = Button(self, text="2", command=self.ev2, bg="white", fg="black",height=6, width=6)
        self.b2.grid(row=2, column=1 )
        self.b3 = Button(self, text="3", command=self.ev3, bg="white", fg="black",height=6, width=6)
        self.b3.grid(row=2, column=2)
        self.bv = Button(self, text="×", command=self.ev_m, bg="black", fg="white",height=6, width=6)
        self.bv.grid(row=2, column=3)
        self.b4 = Button(self, text="4", command=self.ev4, bg="white", fg="black",height=6, width=6)
        self.b4.grid(row=3, column=0)
        self.b5 = Button(self, text="5", command=self.ev5, bg="white", fg="black",height=6, width=6)
        self.b5.grid(row=3, column=1)
        self.b6 = Button(self, text="6", command=self.ev6, bg="white", fg="black",height=6, width=6)
        self.b6.grid(row=3, column=2)
        self.bd = Button(self, text="÷", command=self.ev_d, bg="black", fg="white",height=6, width=6)
        self.bd.grid(row=3, column=3)
        self.b7 = Button(self, text="7", command=self.ev7, bg="white", fg="black",height=6, width=6)
        self.b7.grid(row=4, column=0)
        self.b8 = Button(self, text="8", command=self.ev8, bg="white", fg="black",height=6, width=6)
        self.b8.grid(row=4, column=1)
        self.b9 = Button(self, text="9", command=self.ev9, bg="white", fg="black",height=6, width=6)
        self.b9.grid(row=4, column=2)
        self.b0 = Button(self, text="0", command=self.ev0, bg="white", fg="black",height=6, width=6)
        self.b0.grid(row=5, column=1)
        self.bi = Button(self, text=",", command=self.ev_pn, bg="white", fg="black",height=6, width=6)
        self.bi.grid(row=5, column=0)
        self.bm = Button(self, text="+", command=self.ev_a, bg="black", fg="white",height=6, width=6)
        self.bm.grid(row=4, column=3)
        self.bme = Button(self, text="-", command=self.ev_s, bg="black", fg="white",height=6, width=6)
        self.bme.grid(row=5, column=3)
        self.bp = Button(self, text="=", command=self.onclick, bg="blue", fg="white",height=6, width=6)
        self.bp.grid(row=5, column=2)
        self.bp = Button(self, text="C", command=self.apagar, bg="orange", fg="black",height=6, width=6)
        self.bp.grid(row=6, column=1)
        self.bp = Button(self, text="DEL", command=self.apagar_1, bg="orange", fg="black",height=6, width=6)
        self.bp.grid(row=6, column=2)
        self.b5 = Button(self, text="^", command=self.ev_p, bg="black", fg="white",height=6, width=6)
        self.b5.grid(row=6, column=3)
        self.b5 = Button(self, text="√", command=self.ev_ra, bg="black", fg="white",height=6, width=6)
        self.b5.grid(row=6, column=0)
        
        
    def onclick(self):
        self.entre = self.entry.get()
        self.entre = self.entre.replace('÷', '/')
        self.entre = self.entre.replace('×', '*')
        self.entre = self.entre.replace('^', '**')
        self.entre = self.entre.replace(',', '.')
        self.entre = self.entre.replace('√', '**(1/2)')
        self.R = str(eval(self.entre))
        if len(self.R) > 30:
            self.R = self.R[0:31]+"..."+str(len(self.R[31:])).replace('.', ',')
            self.apagar()
            for self.element in self.R:
                self.VC = self.VC+1
                self.entry.insert(self.VC, self.element)
        else:
            self.apagar()
            for self.element in self.R:
                self.VC = self.VC+1
                self.entry.insert(self.VC, self.element)
     
     
    def apagar(self):
         self.VC = self.VC-len(self.entry.get())
         self.entry.delete(self.VC, END)
         self.VC = 0 if self.VC <= 0 else self.VC
    
    def apagar_1(self):
         self.VC = self.VC-1
         self.entry.delete(self.VC, END)
         self.VC = 0 if self.VC <= 0 else self.VC
    def ev_pn(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, ",")
    def ev_ra(self):
        self.raiz = True
        self.VC = self.VC+1
        self.entry.insert(self.VC, "√")
    def ev1(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "1")
    def ev2(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "2")
    def ev3(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "3")
    def ev_m(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "×")
    def ev4(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "4")
    def ev5(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "5")
    def ev6(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "6")
    def ev_d(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "÷")
    def ev7(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "7")
    def ev8(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "8")
    def ev9(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "9")
    def ev0(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "0")
    def ev_a(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "+")
    def ev_s(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "-")
    def ev_p(self):
        self.VC = self.VC+1
        self.entry.insert(self.VC, "^")
    

janela = GUI()
janela.mainloop()
