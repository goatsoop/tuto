# -*- coding: utf-8 -*-

from Tkinter import *
from random import randrange
from math import fabs


# définition des gestionnaires
# d'événements :


# pour le changement de couleur, la réponse est là:
# http://www.developpez.net/forums/d27983/autres-langages/  {trou} 
# python-zope/gui/tkinter/changer-couleur-d-objet-existant/
def move():
	"déplacement de la balle"
	global x1, y1, dx, dy, flag, dif
	x1, y1 = x1 +dx, y1 + dy
	if x1 >210:
		x1, dx = 210, -dx
	if y1 >210:
		y1, dy = 210, -dy 
	if x1 <10:
		x1, dx = 10, int(fabs(dx))
	if y1 <10:
		y1, dy = 10, int(fabs(dy))
	can1.coords(oval1,x1,y1,x1+30,y1+30)
	diffic.configure(text='Difficulté : '+str(hard))
	
	if randrange(0,8)==0:
		dx,dy=dy,dx
	if flag >0:
		fen1.after(50,move)  	# => boucler, après 50 millisecondes

	
def stop_it():
	"arrêt de l'animation"
	global flag
	flag =0

def start_it():
	"démarrage de l'animation"
	global flag
	if flag ==0: 		# pour ne lancer qu’une seule boucle
		flag =1
		move()
		
def clic(event):
	global win, dx, dy, hard
	print(str(event.x)+' et '+str(event.y))
	print(str(x1))
	dx=fabs(dx)+1
	dy=fabs(dy)+1
	hard+=0.25
	if event.x>x1:
			if event.x<(x1+30):
				if event.y>y1:
					if event.y<(y1+30):
						win+=10
						print(win)
						score.configure(text='Score : '+str(win)+' ! ')

						
	


#========== Programme principal =============
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10  	# coordonnées initiales
dx, dy = 3,7		# 'pas' du déplacement
flag =0				# commutateur
win=0
hard=0
# Création du widget principal ("parent") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")

# création des widgets "enfants" :
can1 = Canvas(fen1,bg='dark grey',height=250, width=250)
can1.pack(side=LEFT, padx =5, pady =5)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2)
bou1 = Button(fen1,text='Quitter', width =8, command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Démarrer', width =8, command=start_it)
bou2.pack()
bou3 = Button(fen1, text='Arrêter', width =8, command=stop_it)
bou3.pack()
score = Label(fen1)
score.pack(pady=15)
diffic = Label(fen1)
diffic.pack(pady=15)

can1.bind("<Button-1>",clic)

# démarrage du réceptionnaire d'événements (boucle principale) :
fen1.mainloop()
