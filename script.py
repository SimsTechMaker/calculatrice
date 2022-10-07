from tkinter import *

from numpy import full
from pyparsing import col

window = Tk()

#Personalisation de la fenetre
window.title("Calculatrice")
window.geometry("400x620")
window.minsize(400,620)
window.iconbitmap("logo.ico")
window.config(background="#B8CBD0")

#Ajouter des elements 
## Creation des frames
frame_master = Frame(window,  bg = "#B8CBD0")
myframe1= Frame(frame_master, bg = "#B8CBD0", bd=1, relief=SUNKEN )

ligne1 = Frame(frame_master,bg = "#B8CBD0",  relief=SUNKEN)
ligne2 = Frame(frame_master,bg = "#B8CBD0",  relief=SUNKEN)
ligne3 = Frame(frame_master,bg = "#B8CBD0",   relief=SUNKEN)
ligne4 = Frame(frame_master,bg = "#B8CBD0",  relief=SUNKEN)
ligne5 = Frame(frame_master,bg = "#B8CBD0",  relief=SUNKEN)


## Ajouter des textes
titre = Label(myframe1,text="Calculatrice", font=("Foco Black",30),bg = "#B8CBD0", fg="white")
titre.pack(pady=12)
titre2 = Label(myframe1,text="Calculatrice2", font=("Foco Black",30),bg = "#B8CBD0", fg="white")

#Mes fonctions 
bot_C = Button(ligne1, text="C" , font=("Foco Black",28), bg="white",fg = "#B8CBD0")
bot_C.grid(row=0,column=0, pady=5,padx=5)
bot_carre = Button(ligne1, text="x²" , font=("Foco Black",28), bg="white",fg = "#B8CBD0")
bot_carre.grid(row=0,column=1,pady=5,padx=5)
bot_racine = Button(ligne1, text="√", font=("Foco Black",28), bg="white",fg = "#B8CBD0")
bot_racine.grid(row=0,column=2,pady=5,padx=5)
bot_plus = Button(ligne1, text="+", font=("Foco Black",28), bg="white",fg = "#B8CBD0")
bot_plus.grid(row=0,column=3,pady=5,padx=5)


bot_7 = Button(ligne2, text="7" , font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_7.grid(row=1,column=0,pady=5,padx=5)
bot_8 = Button(ligne2, text="8" , font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_8.grid(row=1,column=1,pady=5,padx=5)
bot_9 = Button(ligne2, text="9" , font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_9.grid(row=1,column=2,pady=5,padx=5)
bot_moins = Button(ligne2, text="-", font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_moins.grid(row=1,column=3,pady=5,padx=5)

bot_4 = Button(ligne3, text="4" , font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_4.grid(row=2,column=0,pady=5,padx=5)
bot_5 = Button(ligne3, text="5" , font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_5.grid(row=2,column=1,pady=5,padx=5)
bot_6 = Button(ligne3, text="6" , font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_6.grid(row=2,column=2,pady=5,padx=5)
bot_div = Button(ligne3, text="/", font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_div.grid(row=2,column=3,pady=5,padx=5)

bot_1 = Button(ligne4, text="1" , font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_1.grid(row=3,column=0,pady=5,padx=5)
bot_2 = Button(ligne4, text="2" , font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_2.grid(row=3,column=1,pady=5,padx=5)
bot_3 = Button(ligne4, text="3" , font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_3.grid(row=3,column=2,pady=5,padx=5)
bot_mul = Button(ligne4, text="x", font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_mul.grid(row=3,column=3,pady=5,padx=5)

bot_0 = Button(ligne5, text="0" , font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_0.grid(row=4,column=1,pady=5,padx=5)
bot_vir = Button(ligne5, text=",", font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_vir.grid(row=4,column=2,pady=5,padx=5)
bot_egal = Button(ligne5, text="=", font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_egal.grid(row=4,column=3,columnspan=3,pady=5,padx=5)
 




#Affichage
#Afichage des frames

myframe1.grid(row=0,columnspan=10 ,pady=10)
ligne1.grid(row=1, column=0)
ligne2.grid(row=2,column=0)
ligne3.grid(row=3,column=0)
ligne4.grid(row=4,column=0)
ligne5.grid(row=5,column=0)

frame_master.pack()
#Affichage de la fenaitre 
window.mainloop()