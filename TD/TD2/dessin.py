import tkinter as tk 

racine = tk.Tk() 
racine.title("Mon dessin")

canvas = tk.Canvas(racine, bg= "black", height=500, width= 500)
canvas.grid(column=1, row=1, columnspan=3, rowspan=3)

couleur = tk.Button(racine, text='Choisir une couler', command=None)
couleur.grid(column=2, row=0)

cercle = tk.Button(racine, texte='Cercle', command=None)
cercle.grid(column=0, row=1)

carre = tk.Button(racine, text= 'Carré', command=None)
carre.grid(column=0, row=2)

croix = tk.Button(racine, texte='Croix', command=None)
croix.grid(column=0, row=3)

racine.mainloop()