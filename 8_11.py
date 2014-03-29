############################################################
#															
#	
#															
############################################################


# Détection et positionnement d'un clic de souris dans une fenêtre :
from tkinter import *

def pointeur(event):
	cadre.create_oval(event.x,event.y,event.x+10,event.y+10, fill='red')
	chaine.configure(text = "Clic détecté en X =" + str(event.x) +", Y =" + str(event.y))

fen = Tk()

cadre = Canvas(fen, width =200, height =150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()
