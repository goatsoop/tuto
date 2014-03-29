
#
#
#	Un jeu du serpent!
#
#


from tkinter import *
from random import randrange

###############

def move():
	global x1,x2,y1,y2
	x1+=10
	x2+=10
	fen.after(50,move)
	
def go(event):
	move()


x1,x2,y1,y2=100,110,100,110

fen = Tk()

Label(fen, text='Le jeu du Serpent!',bg='dark gray').grid(pady=40)

can1 = Canvas(fen,bg="white",width=400,height=400)
can1.grid()

serp = can1.create_rectangle(x1,y1,x2,y2)

Button(fen,text='Quitter', width =8, command=fen.quit).grid(pady=20)
can1.bind("<Button-1>",go)

fen.mainloop()
