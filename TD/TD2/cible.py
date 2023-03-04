import turtle

# fonction qui dessine un cercle plein de la couleur donnée
def dessiner_cercle_plein(t, rayon, couleur):
    t.fillcolor(couleur)
    t.begin_fill()
    t.circle(rayon)
    t.end_fill()

# initialisation de la tortue
t = turtle.Turtle()

# définition des couleurs et des rayons des cercles
couleurs = ["blue", "green", "black", "yellow", "magenta", "red"]
rayons = [100, 90, 80, 70, 60, 50]

# dessin des cercles
for i in range(len(couleurs)):
    # dessiner le cercle plein
    dessiner_cercle_plein(t, rayons[i], couleurs[i])
    # dessiner le cercle vide
    t.penup()
    t.goto(0, -rayons[i])
    t.pendown()
    t.circle(rayons[i])

# cacher la tortue et terminer le dessin
t.hideturtle()
turtle.done()
