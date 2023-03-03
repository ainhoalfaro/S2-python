import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine
label1 = tk.Label(racine, text="Un texte long dans ma fenêtre", font = ("helvetica", "30")) # création d'un widget
label2 = tk.Label(racine, text="toto", font = ("helvetica", "30")) # création d'un widget
label3 = tk.Label(racine, text="toto1", font = ("helvetica", "15")) # création d'un widget

label1.grid(column=0, row=0) # positionnement du premier widget
label2.grid(row=1, column=0) # positionnement du premier widget
label3.grid(row=1, column=1) # positionnement du premier widget

racine.mainloop() # Lancement de la boucle principale
