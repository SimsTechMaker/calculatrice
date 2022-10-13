from tkinter import *
from click import command



window = Tk()
def generate():
    zone_num.insert(0,"'000000000'")
class la_data():
    def __init__(self, data) -> None:
        self.data= data
    def add(self):
        pass
def add_data():
    a =zone_num.get()
    data = la_data(a)
def del_da():
    zone_num.delete(0,END)
    dico.clear()
def cont():
    if not dico and  not zone_num.get():
        del_da()   
def num_9():
    cont()
    zone_num.insert(END,9)

def num_8():
    cont()
    zone_num.insert(END,8)
def num_7():
    cont()
    zone_num.insert(END,7)
def num_6():
    cont()
    zone_num.insert(END,6)
def num_5():
    cont()
    zone_num.insert(END,5)
def num_4():
    cont()
    zone_num.insert(END,4)
def num_3():
    cont()
    zone_num.insert(END,3)
def num_2():
    cont()
    zone_num.insert(END,2)
def num_1():
    cont()
    zone_num.insert(END,1)
def num_0():
    cont()
    zone_num.insert(END,0)
def num_p():
    cont()
    zone_num.insert(END,".")
dico={}

def del_info():
    print (zone_num.get())
    
    chaine = zone_num.get()
    zone_num.delete(0,END)
    position =int(dico["plus"][1])
    print(chaine[-2])
    if chaine[position]== "+" or chaine[position]== "-" :
        resul = int(dico["plus"][0]) + int(chaine[position:])
    elif chaine[position]== "*":
        resul = int(dico["plus"][0]) * int(chaine[position+1:])
    elif chaine[position]== "/":
        resul = int(dico["plus"][0]) / int(chaine[position+1:])
    zone_num.insert(END,resul)
    dico.clear()

def verif(a):
    t =( a, len(a))
    dico["plus"]=t
      
def plus():
    a = zone_num.get()

    if not dico:
        verif(a)
    elif dico:
        position= dico["plus"][-1]
        t = (a[position:],len(a))
        som= int(dico["plus"][0])+int(t[0])
        dico["plus"]= (som,t[1])
    zone_num.insert(END,"+")
    
def moins():
    a = zone_num.get()
    if not dico :        
        verif(a)

    elif dico:
        position = dico["plus"][-1]
        t = (a[position:], len(a))
        moins = int(dico["plus"][0])+int(t[0])
        print(moins)
        dico["plus"]= (moins,t[1])
    zone_num.insert(END,"-") 
    
def multi():
    a = zone_num.get()
    if not dico:        
        verif(a)
    elif dico:
        position = dico["plus"][-1]
        t = (a[position+1:],len(a))
        if t[0]!= 0:
            multi = int(dico["plus"][0])*int(t[0])
            dico["plus"]= (multi,t[1])
    zone_num.insert(END,"*")
                 
def divi():
    a = zone_num.get()
    if not dico :        
        verif(a)
    elif dico :
        position = dico ["plus"][-1]
        t = (a[position+1:],len(a))
        if t[0]!=0:
            divi = int(dico["plus"][0])/int(t[0])
            dico["plus"] =  (divi, t[1])
    zone_num.insert(END,"/")
                
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
zone_num= Entry(myframe1,font=("Foco Black",38), bg= "#B8CBD0", fg="white")
zone_num.pack()
#Mes fonctions 
bot_C = Button(ligne1, text="C" , font=("Foco Black",28), bg="white",fg = "#B8CBD0" , command=del_da)
bot_C.grid(row=0,column=0, pady=5,padx=5)
bot_carre = Button(ligne1, text="x²" , font=("Foco Black",28), bg="white",fg = "#B8CBD0")
bot_carre.grid(row=0,column=1,pady=5,padx=5)
bot_racine = Button(ligne1, text="√", font=("Foco Black",28), bg="white",fg = "#B8CBD0")
bot_racine.grid(row=0,column=2,pady=5,padx=5)
bot_plus = Button(ligne1, text="+", font=("Foco Black",28), bg="white",fg = "#B8CBD0",  command= plus)
bot_plus.grid(row=0,column=3,pady=5,padx=5)


bot_7 = Button(ligne2, text="7" , font=("Foco Black",30), bg="white",fg = "#B8CBD0",command= num_7)
bot_7.grid(row=1,column=0,pady=5,padx=5)
bot_8 = Button(ligne2, text="8" , font=("Foco Black",30), bg="white",fg = "#B8CBD0",command= num_8)
bot_8.grid(row=1,column=1,pady=5,padx=5)
bot_9 = Button(ligne2, text="9" , font=("Foco Black",30), bg="white",fg = "#B8CBD0",command= num_9)
bot_9.grid(row=1,column=2,pady=5,padx=5)
bot_moins = Button(ligne2, text="-", font=("Foco Black",30), bg="white",fg = "#B8CBD0", command=moins)
bot_moins.grid(row=1,column=3,pady=5,padx=5)

bot_4 = Button(ligne3, text="4" , font=("Foco Black",30), bg="white",fg = "#B8CBD0",command= num_4)
bot_4.grid(row=2,column=0,pady=5,padx=5)
bot_5 = Button(ligne3, text="5" , font=("Foco Black",30), bg="white",fg = "#B8CBD0",command= num_5)
bot_5.grid(row=2,column=1,pady=5,padx=5)
bot_6 = Button(ligne3, text="6" , font=("Foco Black",30), bg="white",fg = "#B8CBD0",command= num_6)
bot_6.grid(row=2,column=2,pady=5,padx=5)
bot_div = Button(ligne3, text="/", font=("Foco Black",30), bg="white",fg = "#B8CBD0", command=divi)
bot_div.grid(row=2,column=3,pady=5,padx=5)

bot_1 = Button(ligne4, text="1" , font=("Foco Black",30), bg="white",fg = "#B8CBD0",command= num_1)
bot_1.grid(row=3,column=0,pady=5,padx=5)
bot_2 = Button(ligne4, text="2" , font=("Foco Black",30), bg="white",fg = "#B8CBD0",command= num_2)
bot_2.grid(row=3,column=1,pady=5,padx=5)
bot_3 = Button(ligne4, text="3" , font=("Foco Black",30), bg="white",fg = "#B8CBD0",command= num_3)
bot_3.grid(row=3,column=2,pady=5,padx=5)
bot_mul = Button(ligne4, text="x", font=("Foco Black",30), bg="white",fg = "#B8CBD0",command=multi)
bot_mul.grid(row=3,column=3,pady=5,padx=5)

bot_0 = Button(ligne5, text="0" , font=("Foco Black",30), bg="white",fg = "#B8CBD0",command= num_0)
bot_0.grid(row=4,column=1,pady=5,padx=5)
bot_vir = Button(ligne5, text=",", font=("Foco Black",30), bg="white",fg = "#B8CBD0")
bot_vir.grid(row=4,column=2,pady=5,padx=5)
bot_egal = Button(ligne5, text="=", font=("Foco Black",30), bg="white",fg = "#B8CBD0", command=del_info)
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