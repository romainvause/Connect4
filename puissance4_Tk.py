from tkinter import *
from tkinter import font

class Info(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=500, height=100)
        police = font.Font(self, size=20, family='Arial')
        self.t = Label(self, text="Tour de Jaune", font=police)
        self.t.grid(sticky=NSEW, pady=20)

class Piont(object):
    def __init__(self, x, y, can, coul="white", bg="red"):
        self.can = can
        self.x = x
        self.y = y
        self.coul = coul

        self.tour = 1
        
        self.r = 30
        self.piont = self.can.create_oval(self.x+10,self.y+10,self.x+61,self.y+61,fill=coul,outline="blue")
        
        

    def changeCouleur(self, coul):
        self.can.itemconfigure(self.piont, fill=coul)
        self.coul = coul

class Terrain(Canvas):
    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=500, height=400, bg="blue")

        self.joueur = 1
        self.coul = "yellow"
        self.p = []
        self.perm = True
        
        for i in range(0, 340, int(400/6)):
            liste_rangee = []
            for j in range(0, 440, int(500/7)):
                liste_rangee.append(Piont(j, i ,self))
                
            self.p.append(liste_rangee)
        
        self.bind("<Button-1>", self.detCol)

    def detCol(self, event):
        if self.perm:
            col = int(event.x/71)
            lig = 0
            
            lig = 0
            while lig < len(self.p):            
                if self.p[0][col].coul == "red" or self.p[0][0].coul == "yellow":
                    break
                
                if self.p[lig][col].coul == "red" or self.p[lig][col].coul == "yellow":
                    self.p[lig-1][col].changeCouleur(self.coul)
                    break
                
                elif lig == len(self.p)-1:
                    self.p[lig][col].changeCouleur(self.coul)
                    break

                
                if self.p[lig][col].coul != "red" and self.p[lig][col].coul != "yellow":
                    lig+=1

            
            
            if self.joueur == 1:
                self.joueur = 2
                info.t.config(text="Tour de rouge")
                self.coul = "red"

            elif self.joueur == 2:
                self.joueur = 1
                info.t.config(text="Tour de jaune")
                self.coul = "yellow"

            self.Horizontal()
            self.Vertical()
            self.Diagonal1()
            self.Diagonal2()

    def Horizontal(self):
        i = 0
        while(i < len(self.p)):
            j = 0
            while(j < 3):
                if(self.p[i][j].coul == self.p[i][j+1].coul == self.p[i][j+2].coul == self.p[i][j+3].coul == "red"):
                    info.t.config(text="Victoire de rouge !")
                    self.perm = False
                    break
                elif(self.p[i][j].coul == self.p[i][j+1].coul == self.p[i][j+2].coul == self.p[i][j+3].coul == "yellow"):
                    info.t.config(text="Victoire de Jaune !")
                    self.perm = False
                    break
                j +=1
            i += 1

    def Vertical(self):
        i = 0
        while(i < 3):
            j = 0
            while(j < len(self.p[i])):
                if(self.p[i][j].coul == self.p[i+1][j].coul == self.p[i+2][j].coul == self.p[i+3][j].coul == "red"):
                    info.t.config(text="Victoire de rouge !")
                    self.perm = False
                    break
                elif(self.p[i][j].coul == self.p[i+1][j].coul == self.p[i+2][j].coul == self.p[i+3][j].coul == "yellow"):
                    info.t.config(text="Victoire de Jaune !")
                    self.perm = False
                    break
                j+=1
            i+=1

    def Diagonal1(self):
        i = 0
        while(i < 3):
            j = 0
            while(j < 3):
                if(self.p[i][j].coul == self.p[i+1][j+1].coul == self.p[i+2][j+2].coul == self.p[i+3][j+3].coul == "red"):
                    info.t.config(text="Victoire de rouge !")
                    self.perm = False
                    break
                elif(self.p[i][j].coul == self.p[i+1][j+1].coul == self.p[i+2][j+2].coul == self.p[i+3][j+3].coul == "yellow"):
                    info.t.config(text="Victoire de Jaune !")
                    self.perm = False
                    break
                j += 1
            i += 1
                    
    def Diagonal2(self):
        i = 0
        while(i < 3):
            j = len(self.p[i])-1
            while(j > len(self.p)-4):
                if(self.p[i][j].coul == self.p[i+1][j-1].coul == self.p[i+2][j-2].coul == self.p[i+3][j-3].coul == "red"):
                    info.t.config(text="Victoire de rouge !")
                    self.perm = False
                    break
                elif(self.p[i][j].coul == self.p[i+1][j-1].coul == self.p[i+2][j-2].coul == self.p[i+3][j-3].coul == "yellow"):
                    info.t.config(text="Victoire de Jaune !")
                    self.perm = False
                    break
                j -= 1
            i += 1



root = Tk()
root.geometry("500x550")
root.title("Puissance 4 - V 1.0 -- Romain VAUSE")

info = Info(root)
info.grid(row=0, column=0)


t = Terrain(root)
t.grid(row=1, column=0)

def rein():
    global info
    info.t.config(text="")
    
    info = Info(root)
    info.grid(row=0, column=0)

    t = Terrain(root)
    t.grid(row=1, column=0)

Button(root, text="Réinitialiser", command=rein).grid(row=2, column=0, pady=30)

root.mainloop()


