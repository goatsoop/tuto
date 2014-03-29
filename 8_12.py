


# Écrivez un programme qui fait apparaître une fenêtre avec un canevas. Dans ce canevas on
# verra deux cercles (de tailles et de couleurs différentes), qui sont censés représenter deux
# astres. Des boutons doivent permettre de les déplacer à volonté tous les deux dans toutes les
# directions. Sous le canevas, le programme doit afficher en permanence : a) la distance séparant
# les deux astres;


from tkinter import *
from math import *
 
############################################################


# fonction d'actualisation (v. plus bas)
def actu():
	global x1,y1,x2,y2
	can.coords(astre1,x1,y1,x1+60,y1+60)
	can.coords(astre2,x2,y2,x2+100,y2+100)

# j'ai PRESQUE la bonne fonction ! j'ai trouvé le calcul sur wikipedia
# à la page "distance entre 2 points sur le plan cartésien"
#				   _______________________________
# en gros c'est : V (x2 - x1)**2  - (y2 - y1)**2
#
# le seul point noir c'est que je n'ai pas fait le calcul pour avoir
# comme coordonnée le centre du cercle...
def distance():
	global x1,y1,x2,y2
	val=(fabs((x2-x1)**2)+(y2-y1)**2)
	Label(fen,text=val).grid(row=7,columnspan=2,pady=20)


# qui suivent : les fonctions de déplacement. Il doit y avoir plus
# propre, mais bon ça marche... en gros, on récupère la variable
# globale et on la modifie dans la bonne direction, puis on appelle
# une fonction qui se charge uniquement de l'actualisation
def depl1G():
	global x1
	x1=x1-10
	actu()
	
def depl1D():
	global x1
	x1=x1+10
	actu()
	
def depl1H():
	global y1
	y1=y1-10
	actu()
	
def depl1B():
	global y1
	y1=y1+10
	actu()

# idem pour le 2e astre
def depl2G():
	global x2
	x2=x2-10
	actu()
	
def depl2D():
	global x2
	x2=x2+10
	actu()
	
def depl2H():
	global y2
	y2=y2-10
	actu()
	
def depl2B():
	global y2
	y2=y2+10
	actu()


##_______________________________

fen = Tk()

# coordonnées initiales des astres
x1,y1=100,100
x2,y2=220,240


can = Canvas(fen,width=400,height=400,bg='black')
can.grid(column=0,columnspan=2)

# ...
Label(fen,text='Bonjour à vous...',bg='white').grid(row=1,column=0,columnspan=2)

# création des astres
astre1=can.create_oval(x1,y1,x1+60,y1+60,fill='red')
astre2=can.create_oval(x2,y2,x2+100,y2+100,fill='green')

Button(fen,text='gauche',command=depl1G).grid(column=0,row=2)
Button(fen,text='droite',command=depl1D).grid(column=0,row=3)
Button(fen,text='haut',command=depl1H).grid(column=0,row=4)
Button(fen,text='bas',command=depl1B).grid(column=0,row=5)

Button(fen,text='gauche',command=depl2G).grid(column=1,columnspan=1,row=2)
Button(fen,text='droite',command=depl2D).grid(column=1,columnspan=1,row=3)
Button(fen,text='haut',command=depl2H).grid(column=1,columnspan=1,row=4)
Button(fen,text='bas',command=depl2B).grid(column=1,columnspan=1,row=5)

Button(fen,text='distance!',command=distance).grid(row=6,columnspan=2)

fen.mainloop()
