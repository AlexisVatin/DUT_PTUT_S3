import tkinter
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import tkinter.ttk as ttk

# fenetre = Tk()
# Dimension fenêtre
#fenetre.geometry('400x400')



# def action(event):
#     # Obtenir l'élément sélectionné
#     select = Liste.get()
#     print("Vous avez sélectionné : '", select, "'")
#
# #Liste youtubeurs
# Liste = ttk.Combobox(fenetre, values=["Squeezie", "Cyprien", "Norman", "Amixem"])
# Liste.bind("<<ComboboxSelected>>", action)
# Liste.pack()
#
#
# #Ajout / affichage liste
# def print_file () :
#     print(Liste.get())
#
# def add () :
#     Valeur = Liste.get()
#     Liste.set(Valeur)
#     valeur = StringVar()
#     if valeur not in self.Liste['values']:
#         self.Liste['values'] += (valeur)
#
#
# #ajouter a la liste
# bAjouter = tkinter.Button (fenetre, text="Ajouter")
# #bAjouter.config (command = add())
# bAjouter.pack ()
#
#
# # bouton de sortie
# bFermer=Button(fenetre, text="Fermer", command=fenetre.quit)
# bFermer.pack()
#
#
# # checkbutton
# b3 = Checkbutton(fenetre, text="Nouveau?")
# b3.pack()
#
#
# # radiobutton
# value = StringVar()
# b4 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
# b5 = Radiobutton(fenetre, text="Non", variable=value, value=2)
# b4.pack()
# b5.pack()
#
#
# #incrementeur
# s = Spinbox(fenetre, from_=0, to=10)
# s.get()
# s.pack()
#
#
# #couleur
# # p = PanedWindow(fenetre, orient=HORIZONTAL)
# # p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
# # p.add(Label(p, text='Volet 1', background='blue', anchor=CENTER))
# # p.add(Label(p, text='Volet 2', background='white', anchor=CENTER) )
# # p.add(Label(p, text='Volet 3', background='red', anchor=CENTER) )
# # p.pack()
#
# #Action
# def callback():
#     if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
#         showwarning('Titre 2', 'Tant pis...')
#         showerror('Titre3', 'Tout est détruit maintenant')
#     else:
#         showinfo('Titre 4', 'Vous avez peur!')
#         showerror("Titre 5", "Aha")
#
# Button(text='Action', command=callback).pack()
#
#
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
#
# #Recuperer Input
# def recupere():
#     showinfo("Alerte", entree.get())
#
# value = StringVar()
# entree = Entry(fenetre, textvariable=value, width=30)
# entree.pack()
#
# bouton = Button(fenetre, text="Valider", command=recupere)
# bouton.pack()
#
#
#
#
# fenetre.mainloop()
#
# # Affichage interface graphique
#
#
# #---------------------------Code Baptiste---------------------------
#
# fenetre = Tk()
#
# #Bouton lancement
# b1=Button(fenetre, text="Lancer", command=fenetre.quit())
# b1.pack()
#
# #Affichage liste
# #bList=Button(fenetre, text="Afficher liste", command=fenetre.tk)
# #bList.pack()
#
# # bouton de sortie
# b2=Button(fenetre, text="Fermer", command=fenetre.quit)
# b2.pack()
#
#
# # checkbutton
# b3 = Checkbutton(fenetre, text="Nouveau?")
# b3.pack()
#
#
# # radiobutton
# value = StringVar()
# b4 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
# b5 = Radiobutton(fenetre, text="Non", variable=value, value=2)
# b4.pack()
# b5.pack()
#
#
# # liste
# liste = Listbox(fenetre)
# liste.insert(1, "Python")
# liste.insert(2, "PHP")
# liste.insert(3, "jQuery")
# liste.insert(4, "CSS")
# liste.insert(5, "Javascript")
#
# liste.pack()
#
#
# #incrementeur
# s = Spinbox(fenetre, from_=0, to=10)
# s.pack()
#
#
# #couleur
# # p = PanedWindow(fenetre, orient=HORIZONTAL)
# # p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
# # p.add(Label(p, text='Volet 1', background='blue', anchor=CENTER))
# # p.add(Label(p, text='Volet 2', background='white', anchor=CENTER) )
# # p.add(Label(p, text='Volet 3', background='red', anchor=CENTER) )
# # p.pack()
#
# #Action
# def callback():
#     if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
#         showwarning('Titre 2', 'Tant pis...')
#         showerror('Titre3', 'Tout est détruit maintenant')
#     else:
#         showinfo('Titre 4', 'Vous avez peur!')
#         showerror("Titre 5", "Aha")
#
# Button(text='Action', command=callback).pack()
#
#
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
#
# #Recuperer Input
# def recupere():
#     showinfo("Alerte", entree.get())
#
# value = StringVar()
# value.set("Valeur")
# entree = Entry(fenetre, textvariable=value, width=30)
# entree.pack()
#
# bouton = Button(fenetre, text="Valider", command=recupere)
# bouton.pack()
#
#
# #Frame
# fenetre['bg']='white'
# # frame 1
# Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
# Frame1.pack(side=LEFT, padx=10, pady=10)
#
# # frame 2
# Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
# Frame2.pack(side=LEFT, padx=10, pady=10)
#
# # frame 3
# Frame3 = Frame(fenetre, borderwidth=2, relief=GROOVE)
# Frame3.pack(side=LEFT, padx=10, pady=10)
# # Ajout de labels
# Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
# Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
# Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)
#
# fenetre.mainloop()


# Affichage interface graphique

# ----------------Classe Tableau Dynamique----------------

class IHM(Frame):
    def __init__(self, fenetre, height, width):
        Frame.__init__(self, fenetre)
        self.numberLines = height
        self.numberColumns = width
        self.pack(fill=BOTH)
        self.data = list()
        for i in range(self.numberLines):
            line = list()
            for j in range(self.numberColumns):
                cell = Entry(self)
                cell.insert(0, 0)
                line.append(cell)
                cell.grid(row=i, column=j)
            self.data.append(line)

        self.results = list()
        for i in range(self.numberColumns):
            cell = Entry(self)
            cell.insert(0, 0)
            cell.grid(row=self.numberLines, column=i)
            self.results.append(cell)
        self.buttonSum = Button(self, text="somme des colonnes", fg="red", command=self.sumCol)
        self.buttonSum.grid(row=self.numberLines, column=self.numberColumns)

    def sumCol(self):
        for j in range(self.numberColumns):
            result = int(0)
            for i in range(self.numberLines):
                result += int(self.data[i][j].get())
            self.results[j].delete(0, END)
            self.results[j].insert(0, result)

fenetre = Tk()
interface = IHM(fenetre, 2, 1)
interface.mainloop()
