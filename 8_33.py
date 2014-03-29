		
# -*- coding: utf-8 -*-#
#
# Jeu de serpent
#

from tkinter import *
from random import randrange

####################

def move():
	"deplacement de la balle"
	global x1,y1,dx,dy,flag,a,b,score,quex,quey
	
	quex,quey=x1,y1
	
	x1=x1+dx
	y1=y1+dy
	if x1>380:
		stop_it()
	if x1<20:
		stop_it()
	if y1>380:
		stop_it()
	if y1<20:
		stop_it()
	
	
	can1.coords(serp,x1,y1,x1+20,y1+20)
	
	if flag>0:
		fen.after(100,move)
		
	bouffe(x1,y1)		
	
	queue(quex,quey,score)


def stop_it():
	"arrêt de l'animation"
	global flag
	flag=0

def start_it():
	"démarrage de l'animation"
	global flag
	if flag ==0:
		flag=1
		move()
		
def depl_haut(event):
	global dy,dx
	dx=0
	dy=-20
	
def depl_gauche(event):
	global dy,dx
	dx=-20
	dy=0

def depl_droite(event):
	global dy,dx
	dx=20
	dy=0
	
def depl_bas(event):
	global dy,dx
	dx=0
	dy=20

def creque(score):
	nbq=0
	if (score==1) and (nbq==0):
		que=can1.create_rectangle(x1,y1,x1+20,y1+20)
		nbq+=1
	if (score==2):
		que2=can1.create_rectangle(x1+20,y1+20,x1+40,y1+40)

def bouffe(x1,y1):
	global a,b,manger,score

	if a==x1 and b==y1:
		can1.delete(manger)
		print("miam!")
		a,b=(randrange(20,380,20)),(randrange(20,380,20))
		manger=can1.create_oval(a,b,a+20,b+20)
		score+=1
		print(score)
		creque(score)

def queue(quex,quey,score):
	if score==1:
		can1.coords(que,quex,quey,quex+20,quey+20)
	elif score==2:
		can1.coords(que2,quex,quey,quex+20,quey+20)
	
	
	


fen = Tk()

x1,y1=200,200
dx,dy=0,0
flag=0
score=0
nbq=0
quex,quey=180,180

can1 = Canvas(fen, bg='gray', height=400, width=400)
can1.grid(pady=15)

fen.bind('<Any-KeyPress-Up>',depl_haut)
fen.bind('<Any-KeyPress-Down>',depl_bas)
fen.bind('<Any-KeyPress-Left>',depl_gauche)
fen.bind('<Any-KeyPress-Right>',depl_droite)

a,b=(randrange(20,380,20)),(randrange(20,380,20))
manger=can1.create_oval(a,b,a+20,b+20)

Label(text='Serpent').grid(pady=15)

serp = can1.create_rectangle(200,200,220,220)

Button(fen,text='Go!',command=start_it).grid()
Button(fen,text='Stop',command=stop_it).grid()

fen.mainloop()

