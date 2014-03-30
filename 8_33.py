		
# -*- coding: utf-8 -*-#
#
# Jeu de serpent
#

from Tkinter import *
from random import randrange

####################


def move():
	"deplacement de la balle"
	global x1,y1,dx,dy,flag,score,speed,i,coordx,coordy
		#moveq(x1,y1)
	if x1>380:
		stop_it()
	if x1<20:
		stop_it()
	if y1>380:
		stop_it()
	if y1<20:
		stop_it()


	
	

	x1=x1+dx
	y1=y1+dy
	
	coordx.append(x1)
	coordy.append(y1)
	
	#a=0
	#while a<(len(coordx)-1):
		#can1.coords(serpent[0],coordx[a],coordy[a],coordx[a]+20,coordy[a]+20)
		#a+=1
	
	
	if len(serpent)==1:
		a=0
		while a<(len(coordx)):
			can1.coords(serpent[0],coordx[a],coordy[a],coordx[a]+20,coordy[a]+20)
			a+=1
	
	if len(serpent)==2:
		a=0
		while a<(len(coordx)):
			can1.coords(serpent[0],coordx[a],coordy[a],coordx[a]+20,coordy[a]+20)
			can1.coords(serpent[1],coordx[a-1],coordy[a-1],coordx[a-1]+20,coordy[a-1]+20)
			a+=1
			
	if len(serpent)==3:
		a=0
		while a<(len(coordx)):
			can1.coords(serpent[0],coordx[a],coordy[a],coordx[a]+20,coordy[a]+20)
			can1.coords(serpent[1],coordx[a-1],coordy[a-1],coordx[a-1]+20,coordy[a-1]+20)
			can1.coords(serpent[2],coordx[a-2],coordy[a-2],coordx[a-2]+20,coordy[a-2]+20)
			a+=1
			
	if len(serpent)==4:
		a=0
		while a<(len(coordx)):
			can1.coords(serpent[0],coordx[a],coordy[a],coordx[a]+20,coordy[a]+20)
			can1.coords(serpent[1],coordx[a-1],coordy[a-1],coordx[a-1]+20,coordy[a-1]+20)
			can1.coords(serpent[2],coordx[a-2],coordy[a-2],coordx[a-2]+20,coordy[a-2]+20)
			can1.coords(serpent[3],coordx[a-3],coordy[a-3],coordx[a-3]+20,coordy[a-3]+20)
			a+=1

	if len(serpent)==5:
		a=0
		while a<(len(coordx)):
			can1.coords(serpent[0],coordx[a],coordy[a],coordx[a]+20,coordy[a]+20)
			can1.coords(serpent[1],coordx[a-1],coordy[a-1],coordx[a-1]+20,coordy[a-1]+20)
			can1.coords(serpent[2],coordx[a-2],coordy[a-2],coordx[a-2]+20,coordy[a-2]+20)
			can1.coords(serpent[3],coordx[a-3],coordy[a-3],coordx[a-3]+20,coordy[a-3]+20)
			can1.coords(serpent[4],coordx[a-4],coordy[a-4],coordx[a-4]+20,coordy[a-4]+20)
			a+=1
				
	if len(serpent)==5:
		Label(can1,text='GAGNE!').grid()
		stop_it()
	
	#print(coordx)
	#print(coordy)
	bouffe(x1,y1)		
	
	
	if len(coordx)>15:
		del coordx[0:5]
		
	if len(coordy)>15:
		del coordy[0:5]
	
	if flag>0:
		fen.after(100,move)







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

def bouffe(x1,y1):
	global a,b,manger,score,speed

	if a==x1 and b==y1:
		can1.delete(manger)
		print("miam!")
		a,b=(randrange(20,380,20)),(randrange(20,380,20))
		manger=can1.create_oval(a,b,a+20,b+20)
		score+=1
		print(score)
		serpent.append(can1.create_rectangle(x1,y1,x1+20,y1+20))
		
		

def start_it():
	"démarrage de l'animation"
	global flag,x1,y1
	if flag ==0:
		flag=1
		move()
	


fen = Tk()
speed=100
x1,y1=200,200
dx,dy=0,0
flag=0
score=0
coord=[0,0,0,0,0,0]
i=0
coordx=[200]
coordy=[200]


can1 = Canvas(fen, bg='gray', height=400, width=400)
can1.grid(pady=15)

fen.bind('<Any-KeyPress-Up>',depl_haut)
fen.bind('<Any-KeyPress-Down>',depl_bas)
fen.bind('<Any-KeyPress-Left>',depl_gauche)
fen.bind('<Any-KeyPress-Right>',depl_droite)

a,b=(randrange(20,380,20)),(randrange(20,380,20))
manger=can1.create_oval(a,b,a+20,b+20)

Label(text='Serpent').grid(pady=15)

serp = can1.create_rectangle(x1,y1,x1+20,y1+20)
serpent=[serp]


Button(fen,text='Go!',command=start_it).grid()



fen.mainloop()

