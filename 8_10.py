############################################################
#															
#	Création d'une fenetre graphique, et de deux boutons:
#	-le premier pour créer un damier
#	-le second pour placer un pion au hasard sur le damier
#															
############################################################

from tkinter import *
from random import randrange
 
############################################################

 
def damier():
	x0,y0,x1,y1,i=0,0,20,20,0
	"dessiner un damier"
	ligne(x0,y0,x1,y1)
	
def rempl_ligne(x0,y0,x1,y1):
	i=0
	while i<10:
		can.create_rectangle(x0,y0,x1,y1,fill='blue')
		x0+=40
		x1+=40
		i+=1
	
def ligne(x0,y0,x1,y1):
	ind=0
	while ind<10:
		if ind%2==0:
			x0=20
			x1=40
		else:
			x0=00
			x1=20
		rempl_ligne(x0,y0,x1,y1)
		y0+=20
		y1+=20
		ind+=1
		
def pion():
	adresse=[3,23,43,63,83,103,123,143,163,183]
	xOv0=adresse[randrange(9)]
	xOv1=xOv0+15
	yOv0=adresse[randrange(9)]
	yOv1=yOv0+15
	can.create_oval(xOv0,yOv0,xOv1,yOv1,fill='red')
	
	
 
##### Programme principal : ############
fen = Tk()
can = Canvas(fen, width =199, height =200, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(fen, text ='damier', command =damier)
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(fen, text ='pion', command =pion)
b2.pack(side =RIGHT, padx =3, pady =3)
fen.mainloop()
