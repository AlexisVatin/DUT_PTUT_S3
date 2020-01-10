import tkinter
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import tkinter.ttk as ttk

fenetre = Tk()

# Dimension fenêtre
# fenetre.geometry('400x400')


def action(event):
    # Obtenir l'élément sélectionné
    select = Liste.get()
    print("Vous avez sélectionné : '", select, "'")


# Liste youtubeurs
Liste = ttk.Combobox(fenetre, values=["Squeezie", "Cyprien", "Norman", "Amixem"])
Liste.bind("<<ComboboxSelected>>", action)
Liste.pack()


# Ajout / affichage liste
def print_file():
    print(Liste.get())


def add():
    Valeur = Liste.get()
    Liste.set(Valeur)
    valeur = StringVar()
    if valeur not in self.Liste['values']:
        self.Liste['values'] += (valeur)


# ajouter a la liste
bAjouter = tkinter.Button(fenetre, text="Ajouter")
# bAjouter.config (command = add())
bAjouter.pack()

# bouton de sortie
bFermer = Button(fenetre, text="Fermer", command=fenetre.quit)
bFermer.pack()

# # checkbutton
# b3 = Checkbutton(fenetre, text="Nouveau?")
# b3.pack()


# radiobutton
value = StringVar()
b4 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
b5 = Radiobutton(fenetre, text="Non", variable=value, value=2)
b4.pack()
b5.pack()

# incrementeur
s = Spinbox(fenetre, from_=0, to=10)
s.get()
s.pack()


# Action
def callback():
    showinfo('Titre 4', "Le nombre de vidéo vue sera de : [variable]", )
    # if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
    #     showwarning('Titre 2', 'Tant pis...')
    #     showerror('Titre3', 'Tout est détruit maintenant')
    # else:
    #     showerror("Titre 5", "Aha")


Button(text='Action', command=callback).pack()


# #Barre du menu
# def alert():
#     showinfo("alerte", "Bravo!")
#
# menubar = Menu(fenetre)
#
# menu1 = Menu(menubar, tearoff=0)
# menu1.add_command(label="Créer", command=alert)
# menu1.add_command(label="Editer", command=alert)
# menu1.add_separator()
# menu1.add_command(label="Quitter", command=fenetre.quit)
# menubar.add_cascade(label="Fichier", menu=menu1)
#
# menu2 = Menu(menubar, tearoff=0)
# menu2.add_command(label="Couper", command=alert)
# menu2.add_command(label="Copier", command=alert)
# menu2.add_command(label="Coller", command=alert)
# menubar.add_cascade(label="Editer", menu=menu2)
#
# menu3 = Menu(menubar, tearoff=0)
# menu3.add_command(label="A propos", command=alert)
# menubar.add_cascade(label="Aide", menu=menu3)
#
# fenetre.config(menu=menubar)

# Recuperer Input
def recupere():
    showinfo("Alerte", entree.get())


value = StringVar()
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

bouton = Button(fenetre, text="Valider", command=recupere)
bouton.pack()

fenetre.mainloop()

# Affichage interface graphique
