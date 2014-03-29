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
	"dessine un simple damier, en renvoyant à 2 fonctions"
	x0,y0,x1,y1,i=0,0,20,20,0
	ligne(x0,y0,x1,y1)
	
def rempl_ligne(x0,y0,x1,y1):
	"trace pour de vrai la ligne"
	i=0
	while i<10:
		can.create_rectangle(x0,y0,x1,y1,fill='blue')
		x0+=40
		x1+=40
		i+=1
	
def ligne(x0,y0,x1,y1):
	"fonction qui trace les lignes du damier et les colorie"

	## création d'une boucle qui servira seulement à alterner
	## dessin de carré puis vide, pour faire le damier
	## le truc, pas très propre, consiste à alterner à chaque ligne
	ind=0
	while ind<10:
		if ind%2==0:
			x0=20
			x1=40
		else:
			x0=00
			x1=20
			
		## on dessine les cases sur la ligne en cours
		rempl_ligne(x0,y0,x1,y1)
		
		## puis on décale vers le bas pour la ligne suivante
		y0+=20
		y1+=20
		ind+=1
		
def pion():
	adresse=[3,23,43,63,83,103,123,143,163,183]
	xOv0=adresse[randrange(9)]
	yOv0=adresse[randrange(9)]
	can.create_oval(xOv0,yOv0,xOv0+15,yOv0+15,fill='red')
	
	
 
##### Programme principal : ############


fen = Tk()

## Création du canevas où seront dessinés les objets
can = Canvas(fen, width =199, height =200, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)

## ici, du code compacté selon l'astuce donnée p.100 du tuto! ##
## simple création des boutons ##
Button(fen, text ='damier', command =damier).pack(side =LEFT, padx =3, pady =3)
Button(fen, text ='pion', command =pion()).pack(side =RIGHT, padx =3, pady =3)

## et boucle de programme...##
fen.mainloop()
