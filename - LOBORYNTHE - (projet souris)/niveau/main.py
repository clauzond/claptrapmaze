from tkinter import*
from time import*
from random import*

mainF=Tk()
mainF.title("Claptrap's Maze")
mainF.resizable(width=False,height=False)
mainF.iconbitmap("img/icone/claptrap.ico")


# Images à charger
ImgPremier=PhotoImage(file="img/couronne1.gif")
ImgSecond=PhotoImage(file="img/couronne2.gif")
ImgTroisieme=PhotoImage(file="img/couronne3.gif")
Bonus=PhotoImage(file="img/bonus.gif")
Mur=PhotoImage(file="img/mur.gif")
Arrive=PhotoImage(file="img/goal.gif")
Clef=PhotoImage(file="img/clef.gif")
Porte=PhotoImage(file="img/porte1.gif")
ImgChrono=PhotoImage(file="img/chrono.gif")
Claptrap=PhotoImage(file="img/claptrapORIGINAL.gif")
background_image=PhotoImage(file="img/background.gif")
background_mainmenu=PhotoImage(file="img/background_mainmenu.gif")
background_mainmenu_bonus1=PhotoImage(file="img/background_mainmenu_bonus1.gif")
background_mainmenu_bonus2=PhotoImage(file="img/background_mainmenu_bonus2.gif")
Cercle=PhotoImage(file="img/cercle.gif")
NewCercle=PhotoImage(file="img/newcercle.gif")

x=45
y=45
hauteur=30
largeur=30

# Mouvement du personnage :
# Modifie les coordonnées du personnage en permanence
# Vérifie la touche appuyée
# Si "un objet autre que lui-même" se trouve à l'emplacement où il veut aller, alors ne pas se déplacer

def move(event):
    global x,y,Lab,BonusDestroy,C
    if event.keysym=='Up':

        collisionU=C.find_overlapping(x+14,y-16,x-14,y-44)
        bloc0=C.gettags(collisionU[0])
        if "mur" not in bloc0:
            if "porte" not in bloc0:
                y=y-30
                C.move(perso,0,-30)
                if "goal" in bloc0:
                    Lab.destroy()
                    Lab.quit()
                    goal()
                if "bonus" in bloc0[0] :
                    # Détecter lequel des bonus a été détecté
                    BonusDestroy=bloc0[0]
                    bonus()
                if "piege" in bloc0:
                    piege()
                if "clef" in bloc0:
                    clef()

    if event.keysym=='Down':

        collisionD=C.find_overlapping(x-14,y+16,x+14,y+44)
        bloc0=C.gettags(collisionD[0])
        if "mur" not in bloc0:
            if "porte" not in bloc0:
                C.move(perso,0,30)
                y=y+30
                if "goal" in bloc0:
                    Lab.destroy()
                    Lab.quit()
                    goal()
                if "bonus" in bloc0[0] :
                    # Détecter lequel des bonus a été détecté
                    BonusDestroy=bloc0[0]
                    bonus()
                if "piege" in bloc0:
                    piege()
                if "clef" in bloc0:
                    clef()


    if event.keysym=='Left':

        collisionL=C.find_overlapping(x-16,y-14,x-44,y+14)
        bloc0=C.gettags(collisionL[0])
        if "mur" not in bloc0:
            if "porte" not in bloc0:
                C.move(perso,-30,0)
                x=x-30
                if "goal" in bloc0:
                    Lab.destroy()
                    Lab.quit()
                    goal()
                if "bonus" in bloc0[0] :
                    # Détecter lequel des bonus a été détecté
                    BonusDestroy=bloc0[0]
                    bonus()
                if "piege" in bloc0:
                    piege()
                if "clef" in bloc0:
                    clef()

    if event.keysym=='Right':

        collisionR=C.find_overlapping(x+16,y+14,x+44,y-14)
        bloc0=C.gettags(collisionR[0])
        if "mur" not in bloc0:
            if "porte" not in bloc0:
                C.move(perso,30,0)
                x=x+30
                if "goal" in bloc0:
                    Lab.destroy()
                    Lab.quit()
                    goal()
                if "bonus" in bloc0[0] :
                    # Détecter lequel des bonus a été détecté
                    BonusDestroy=bloc0[0]
                    bonus()
                if "piege" in bloc0:
                    piege()
                if "clef" in bloc0:
                    clef()
    return


# Définition du labyrinthe
# Incomplète pour le moment, seulement les contours
# à générer AVANT la création du personnage
BonusNombre=0
def Labyrinthe():
    global C,Lab,perso,Pers,niveau,M,N,P,Q,BonusNombre,Bonus,Mur,Arrive,Clef,Porte
    Niveau.destroy()
    Niveau.quit()

    # Choix de la difficulté :
    # - Largeur et hauteur modifiable
    # - Fenêtre modifié selon largeur et hauteur
    # - Ouvre le fichier correspondant (du même nom)
    PathNiveau="niveau/"+str(niveau)+".txt"
    fich=open(PathNiveau,"r")
    ligne=fich.readlines()

    # Génération des carrés du labyrinthe :
    # - Première boucle pour la hauteur "y", deuxième pour largeur "x"
    # - Largeur et hauteur définie selon la difficulté choisie

    for y in range(0,hauteur):
        for x in range(0,largeur):
            goal="+"+str(x)+"+"
            bonus="/"+str(x)+"/"
            piege="-"+str(x)+"-"
            vide=","+str(x)+","
            clef="!"+str(x)+"!"
            porte="§"+str(x)+"§"
            # Crée un bloc d'arrivée lorsque "+x+" est écrit
            if goal in ligne[y]:
                C.create_image(15+30*x,15+30*y,image=Arrive,tags="goal")
                #C.create_rectangle(0+30*x,30*y,30+30*x,30+30*y,fill="green",width=0,tags="goal")
            # Crée un bloc de bonus lorsque "/x/" est écrit
            elif bonus in ligne[y]:
                BonusNombre+=1
                C.create_image(15+30*x,15+30*y,image=Bonus,tags="bonus%s"%BonusNombre)
                #C.create_rectangle(0+30*x,30*y,30+30*x,30+30*y,fill="orange",tags="bonus%s"%BonusNombre)
            # Crée un bloc de piège lorsque "-x-" est écrit
            elif piege in ligne[y]:
                C.create_image(15+30*x,15+30*y,image=Bonus,tags="piege")
                #C.create_rectangle(0+30*x,30*y,30+30*x,30+30*y,fill="orange",tags="piege")
            # Crée un carré lorsque ",x," n'est pas écrit
            elif clef in ligne[y]:
                #C.create_rectangle(0+30*x,30*y,30+30*x,30+30*y,fill="yellow",tags="clef")
                C.create_image(15+30*x,15+30*y,image=Clef,tags="clef")
                M=x
                N=y
            elif porte in ligne[y]:
                #C.create_rectangle(0+30*x,30*y,30+30*x,30+30*y,fill="gray",tags="porte")
                C.create_image(15+30*x,15+30*y,image=Porte,tags="porte")
                P=x
                Q=y
            elif vide not in ligne[y]:
                C.create_image(15+30*x,15+30*y,image=Mur,tags="mur")
                #C.create_rectangle(0+30*x,30*y,30+30*x,30+30*y,fill="#713A29",width=0,tags="mur")
    fich.close()

    # Définition du personnage

    Pers=PhotoImage(file="img/claptrap.gif")
    perso=C.create_image(45,45,image=Pers,tags="Personnage")

    # Bind pour se déplacer
    Lab.bind('<KeyPress>',move)



    Lab.deiconify()

    # Mise en place du chronomètre
    CreateChrono()


    C.mainloop()

# Ligne d'arrivée
def goal():
    global C,Lab,Niveau,temps,Goal,tvar,Classement

    mainF.deiconify()

    CheckClassement("pour victoire")
    if int(Classement)==1:
        TexteClassement=str(Classement)+"er"
    elif int(Classement)>=1:
        TexteClassement=str(Classement)+"ème"

    Goal=Toplevel()
    Goal.title("Niveau terminé")

    Goal.resizable(width=False,height=False)
    Goal.iconbitmap("img/icone/claptrap.ico")

    ScoreTexte="Bravo ! Vous avez fini en "+temps+". Vous êtes "+TexteClassement+". Entrez votre nom : "
    TexteWin=Label(Goal,text=ScoreTexte,font="Constantia 20")
    TexteWin.pack(side="top",padx=10,pady=10)

    tvar=StringVar()
    ChampNom=Entry(Goal,textvariable=tvar,font="Constantia 18")
    ChampNom.pack()

    BoutonNom=Button(Goal,text="Enregistrer",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=SaveScore)
    BoutonNom.pack(padx=10,pady=10)

def SaveScore():
    global temps,Goal,tvar,niveau,ScoreJoueur,NomJoueur,Classement
    Goal.destroy()
    Goal.quit()

    NomSave="scores/"+str(niveau)+".txt"

    ScoreJoueur=temps
    NomJoueur=tvar.get()
    fich=open(NomSave,"a")
    fich.write(NomJoueur+"\n")
    fich.write(ScoreJoueur+"\n")
    fich.close()

    CheckClassement("pour enregistrer")

    if niveau=="facile":
        DerniereSave="scores/dernier-facile.txt"
        fich=open(DerniereSave,"w")
        fich.write(NomJoueur+"\n")
        fich.write(ScoreJoueur+"\n")
        fich.write(Classement+"\n")
        fich.close()
    elif niveau=="moyen":
        DerniereSave="scores/dernier-moyen.txt"
        fich=open(DerniereSave,"w")
        fich.write(NomJoueur+"\n")
        fich.write(ScoreJoueur+"\n")
        fich.write(Classement+"\n")
        fich.close()
    elif niveau=="difficile":
        DerniereSave="scores/dernier-difficile.txt"
        fich=open(DerniereSave,"w")
        fich.write(NomJoueur+"\n")
        fich.write(ScoreJoueur+"\n")
        fich.write(Classement+"\n")
        fich.close()



def CheckClassement(string):
    global niveau,DernierJoueur,ListeComplete,ScoreJoueur,NomJoueur,Classement,temps
    TriScore(niveau)

    if string=="pour victoire":
        ScoreJoueur=temps
        ListeComplete.append(["",ScoreJoueur])
        ListeComplete.sort(key=lambda colonne: colonne[1])
        for k in range(len(ListeComplete)):
            if ScoreJoueur in ListeComplete[k]:
                Classement=str(k+1)
                break


    if string=="pour enregistrer":

        for k in range(len(ListeComplete)):
            if ScoreJoueur in ListeComplete[k]:
                Classement=str(k+1)
                break

# Bonus
def bonus():
    global C,Lab,perso,Pers,x,y
    # xx - yy correspondent aux coordonnées du labyrinthe (et non du canvas)
    #xx=(x-15)/30
    #yy=(y-15)/30
    #C.create_rectangle(0+30*xx,30*yy,30+30*xx,30+30*yy,fill="white",outline="white",width=0,tags="vide")
    #C.delete(perso)

    # Supprimer l'item correspondant au tag du bonus "trouvé"
    DetruireBonus=C.find_withtag(BonusDestroy)
    C.delete(DetruireBonus)

    r=randint(1,100)
    if 0<=r<=10:
        RandomPerso="img/claptrap5.gif"
    elif 11<=r<=30:
        RandomPerso="img/claptrap4.gif"
    elif 31<=r<=50:
        RandomPerso="img/claptrap3.gif"
    else:
        RandomPerso="img/claptrap2.gif"

    C.delete(perso)
    Pers=PhotoImage(file=RandomPerso)
    perso=C.create_image(x,y,image=Pers,tags="Personnage")



    C.after(7500,bonus2)


def bonus2():
    global C,Lab,perso,Pers,x,y
    C.delete(perso)
    Pers=PhotoImage(file="img/claptrap.gif")
    perso=C.create_image(x,y,image=Pers,tags="Personnage")


# Piege
def piege():
    global x,y,C,Lab
    x=45
    y=45
    C.coords(perso,45,45)
    Lab.mainloop()

def clef():
    global M,N,P,Q

    #Détruire la clef
    clefdetruire=C.find_withtag("clef")
    C.delete(clefdetruire)

    #Détruire le mur
    portedetruire=C.find_withtag("porte")
    C.delete(portedetruire)

def Quit():
    mainF.destroy()



def Facile():
    global niveau,hauteur,largeur,x,y
    x=45
    y=45
    hauteur=30
    largeur=30
    niveau="facile"
    Lab.title("Claptrap's Maze - Difficulté : FACILE")
    Labyrinthe()

def Moyen():
    global niveau,hauteur,largeur,x,y
    x=45
    y=45
    hauteur=30
    largeur=30
    niveau="moyen"
    Lab.title("Claptrap's Maze - Difficulté : MOYEN")
    Labyrinthe()

def Difficile():
    global niveau,hauteur,largeur,x,y
    x=45
    y=45
    hauteur=30
    largeur=30
    niveau="difficile"
    Lab.title("Claptrap's Maze - Difficulté : DIFFICILE")
    Labyrinthe()

def Tutoriel():
    global Claptrap,Mur,Arrive,Bonus,Clef,Porte,ImgChrono

    Aide=Toplevel()
    Aide.title("Description des éléments du labyrinthe")
    Aide.resizable(width=False,height=False)
    Aide.iconbitmap("img/icone/claptrap.ico")

    a="Claptrap, votre personnage : vous devez le déplacer pour finir le labyrinthe"
    LabelTuto=Label(Aide,text=a,image=Claptrap,compound="left",font="Constantia 12",padx=10,pady=10).pack()

    b="Les murs : ils servent à délimiter votre parcours. Vous ne pouvez pas les traverser."
    LabelTuto=Label(Aide,text=b,image=Mur,compound="left",font="Constantia 12",padx=10,pady=10).pack()

    c="Le bloc secret : quand vous atteignez ce bloc, un effet aura lieu sur votre parcours. A vous de le découvrir !"
    LabelTuto=Label(Aide,text=c,image=Bonus,compound="left",font="Constantia 12",padx=10,pady=10).pack()

    d="La clef : l'élément indispensable de votre périple qui vous permettra d'ouvrir..."
    LabelTuto=Label(Aide,text=d,image=Clef,compound="left",font="Constantia 12",padx=10,pady=10).pack()

    e="... la porte : elle s'ouvre une fois la clef en main. Le chemin débloqué vous permettra d'atteindre..."
    LabelTuto=Label(Aide,text=e,image=Porte,compound="left",font="Constantia 12",padx=10,pady=10).pack()

    f="... la ligne d'arrivée : une fois atteinte, la partie est gagnée."
    LabelTuto=Label(Aide,text=f,image=Arrive,compound="left",font="Constantia 12",padx=10,pady=10).pack()

    g="Le chronomètre : votre temps est compté pour atteindre la ligne d'arrivée ! Tentez de battre votre meilleur score lors de futures parties !"
    LabelTuto=Label(Aide,text=g,image=ImgChrono,compound="left",font="Constantia 12",padx=10,pady=10).pack()


    return

# Fenêtre du labyrinthe

def Niveau():
    global Niveau
    try:
        Lab.destroy()
        Lab.quit()
    except:
        False

    Niveau=Toplevel()

    Niveau.title("Sélection du niveau")
    Niveau.resizable(width=False,height=False)
    Niveau.iconbitmap("img/icone/claptrap.ico")

    canvasniveau=Canvas(Niveau)
    canvasniveau.grid(row=0,column=0,rowspan=2,columnspan=3)
    canvasniveau.create_image(0,0,image=background_image,anchor="nw")

    Bfacile=Button(canvasniveau,text="Facile",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=Facile)
    Bfacile.grid(row=0,column=0,padx=20,pady=30)

    Bmoyen=Button(canvasniveau,text="Moyen",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=Moyen)
    Bmoyen.grid(row=0,column=1)

    Bdifficile=Button(canvasniveau,text="Difficile",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=Difficile)
    Bdifficile.grid(row=0,column=2,padx=20)

    Tuto=Button(canvasniveau,text="Aide",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=Tutoriel)
    Tuto.grid(row=1,column=1,padx=20,pady=20)

    LabFen()

    Niveau.mainloop()

def LabFen():
    global C,Lab

    Lab=Toplevel()

    Lab.title("En attente du choix du niveau...")
    Lab.resizable(width=False,height=False)
    Lab.iconbitmap("img/icone/claptrap.ico")
    Lab.iconify()
    C=Canvas(Lab,width=900,height=900,background="white")
    C.pack()
    C.mainloop()

def LireScore(niv):
    global NombreScores,LB,ListeScore,FenScore,ListeComplete,DernierJoueur,ImgPremier,ImgSecond,ImgTroisieme


    TriScore(niv)
    TriDernierScore(niv)


    if len(DernierJoueur)<=3:
        if int(DernierJoueur[2])>1:
            d=str(DernierJoueur[2])+"ème"+" "+str(DernierJoueur[0])+" "+str(DernierJoueur[1])
        elif int(DernierJoueur[2])==1:
            d=str(DernierJoueur[2])+"er"+" "+str(DernierJoueur[0])+" "+str(DernierJoueur[1])
    else:
        d=DernierJoueur


    if len(ListeComplete)==0:
        LabelScore=Label(FenScore,text="Aucun score n'est enregistré pour ce niveau.",font="Constantia 20",padx=10,pady=10)
        LabelScore.pack()
    elif len(ListeComplete)==1:
        premier=ListeComplete[0]
        a=str(premier[0])+" "+str(premier[1])
        LabelPremier=Label(FenScore,text=a,image=ImgPremier,compound="left",font="Constantia 20",padx=10,pady=10)
        LabelPremier.pack()
        LabelDernier=Label(FenScore,text=d,font="Constantia 20",bg="gray",padx=10,pady=10)
        LabelDernier.pack()

    elif len(ListeComplete)==2:
        premier=ListeComplete[0]
        a=str(premier[0])+" "+str(premier[1])
        second=ListeComplete[1]
        b=str(second[0])+" "+str(second[1])
        LabelPremier=Label(FenScore,text=a,image=ImgPremier,compound="left",font="Constantia 20",padx=10,pady=10)
        LabelPremier.pack()
        LabelSecond=Label(FenScore,text=b,image=ImgSecond,compound="left",font="Constantia 20",padx=10,pady=10)
        LabelSecond.pack()
        LabelDernier=Label(FenScore,text=d,font="Constantia 20",bg="gray",padx=10,pady=10)
        LabelDernier.pack()

    elif len(ListeComplete)>=3:
        premier=ListeComplete[0]
        a=str(premier[0])+" "+str(premier[1])
        second=ListeComplete[1]
        b=str(second[0])+" "+str(second[1])
        troisieme=ListeComplete[2]
        c=str(troisieme[0])+" "+str(troisieme[1])

        LabelPremier=Label(FenScore,text=a,image=ImgPremier,compound="left",font="Constantia 20",padx=10,pady=10)
        LabelPremier.pack()
        LabelSecond=Label(FenScore,text=b,image=ImgSecond,compound="left",font="Constantia 20",padx=10,pady=10)
        LabelSecond.pack()
        LabelTroisieme=Label(FenScore,text=c,image=ImgTroisieme,compound="left",font="Constantia 20",padx=10,pady=10)
        LabelTroisieme.pack()
        LabelDernier=Label(FenScore,text=d,font="Constantia 20",bg="gray",padx=10,pady=10)
        LabelDernier.pack()

    FenScore.mainloop()




def TriScore(niv):
    global ListeComplete,DernierJoueur

    NomSave="scores/"+str(niv)+".txt"
    fich=open(NomSave,"r")
    ListeScore=fich.readlines()
    fich.close()

    ListeComplete=[]
    for compteur in range(0,len(ListeScore),2):
        namejoueur=ListeScore[compteur]
        timejoueur=ListeScore[compteur+1]
        if "\n" in timejoueur:
            timejoueur=timejoueur.replace("\n","")
        if "\n" in namejoueur:
            namejoueur=namejoueur.replace("\n","")

        ListeComplete.append([namejoueur,timejoueur])

    ListeComplete.sort(key=lambda colonne: colonne[1])

def TriDernierScore(niv):
    global DernierJoueur
    if niv=="facile":
        DerniereSave="scores/dernier-facile.txt"
        fich=open(DerniereSave,"r")
        DernierJoueur=fich.readlines()
        if len(DernierJoueur)>=2:
            DernierJoueur[0]=DernierJoueur[0].replace("\n","")
            DernierJoueur[1]=DernierJoueur[1].replace("\n","")
            DernierJoueur[2]=DernierJoueur[2].replace("\n","")
        else:
            DernierJoueur="Il n'y a pas de score enregistré récemment."
        fich.close()
    elif niv=="moyen":
        DerniereSave="scores/dernier-moyen.txt"
        fich=open(DerniereSave,"r")
        DernierJoueur=fich.readlines()
        if len(DernierJoueur)>=2:
            DernierJoueur[0]=DernierJoueur[0].replace("\n","")
            DernierJoueur[1]=DernierJoueur[1].replace("\n","")
            DernierJoueur[2]=DernierJoueur[2].replace("\n","")
        else:
            DernierJoueur="Il n'y a pas de score enregistré récemment."
        fich.close()
    elif niv=="difficile":
        DerniereSave="scores/dernier-difficile.txt"
        fich=open(DerniereSave,"r")
        DernierJoueur=fich.readlines()
        if len(DernierJoueur)>=2:
            DernierJoueur[0]=DernierJoueur[0].replace("\n","")
            DernierJoueur[1]=DernierJoueur[1].replace("\n","")
            DernierJoueur[2]=DernierJoueur[2].replace("\n","")
        else:
            DernierJoueur="Il n'y a pas de score enregistré récemment."
        fich.close()


def Scoreboard():
    global LB,NombreScores

    LB=Toplevel()
    LB.title("Tableau des scores")
    LB.resizable(width=False,height=False)
    LB.iconbitmap("img/icone/claptrap.ico")

    LBcanvas=Canvas(LB)
    LBcanvas.pack()
    LBcanvas.create_image(0,0,image=background_image,anchor="nw")

    ScoreFacile=Button(LBcanvas,text="Facile",font="Constantia 15",justify="center",overrelief="groove",bg="white",activeforeground="blue",activebackground="white",command=OngletFacile)
    ScoreFacile.pack(side="left",padx=20,pady=20)

    ScoreMoyen=Button(LBcanvas,text="Moyen",font="Constantia 15",justify="center",overrelief="groove",bg="white",activeforeground="blue",activebackground="white",command=OngletMoyen)
    ScoreMoyen.pack(side="left",padx=20)

    ScoreDifficile=Button(LBcanvas,text="Difficile",font="Constantia 15",justify="center",overrelief="groove",bg="white",activeforeground="blue",activebackground="white",command=OngletDifficile)
    ScoreDifficile.pack(side="left",padx=20,pady=20)

    LB.mainloop()


def OngletFacile():
    global FenScore
    FenScore=Toplevel()
    FenScore.title("Niveau : FACILE")
    FenScore.resizable(width=False,height=False)
    FenScore.iconbitmap("img/icone/claptrap.ico")
    LireScore("facile")
    return

def OngletMoyen():
    global FenScore
    FenScore=Toplevel()
    FenScore.title("Niveau : MOYEN")
    FenScore.resizable(width=False,height=False)
    FenScore.iconbitmap("img/icone/claptrap.ico")
    LireScore("moyen")
    return

def OngletDifficile():
    global FenScore
    FenScore=Toplevel()
    FenScore.title("Niveau : DIFFICILE")
    FenScore.resizable(width=False,height=False)
    FenScore.iconbitmap("img/icone/claptrap.ico")
    LireScore("difficile")
    return


def CreateChrono():
    global debut,TexteChrono,ImgChrono
    debut=time()
    FrameChrono=Frame(Lab,bg="black")
    FrameChrono.place(x=810,y=2)

    TexteChrono=Label(FrameChrono,text="00:00",font="Helvetica 14",fg="white",bg="black")
    TexteChrono.pack(side="right")

    imgchrono=Label(FrameChrono,image=ImgChrono,bg="black")
    imgchrono.pack(side="left")

    Chrono()


    Lab.mainloop()


def Chrono():
    global debut,TexteChrono,Status,temps
    fin=time()
    difference=fin-debut
    local=localtime(difference)
    temps=strftime("%M:%S",local)
    TexteChrono.config(text=temps)
    TexteChrono.update()
    Lab.after(1000,Chrono)


def MenuMove(event):
    #global Cercle_Menu,Claptrap_Menu
    mx,my=event.x,event.y
    try:
        canvasmenu.coords(Cercle_Menu,mx,my)
    except:
        False
    if PorteOuverte==0:
        if mx>44 and mx<212:
            canvasmenu.coords(Claptrap_Menu,mx,48)
    if PorteOuverte==1:
        if mx>44 and mx<455:
            canvasmenu.coords(Claptrap_Menu,mx,48)
        return

def MenuCheck(event):
    global clefx,clefy,bonusx,bonusy,PorteOuverte,Cercle_Menu,Reset_Check
    mx,my=event.x,event.y
    if abs(mx-clefx)<=20 and abs(my-clefy)<=20:
        canvasmenu.delete(Clef_Menu)
        canvasmenu.delete(Porte_Menu)
        PorteOuverte=1
    if PorteOuverte==1:
        if mx>425 and 33<=my<=63:
            canvasmenu.delete(Cercle_Menu)
            canvasmenu.unbind("<Button-1>")
            Reset_Check=0
            Clignotement()

    if abs(mx-bonusx)<=10 and abs(my-bonusy)<=10:
        canvasmenu.delete(Bonus_Menu)
        canvasmenu.delete(Cercle_Menu)
        Cercle_Menu=canvasmenu.create_image(mx,my,image=NewCercle)


def Clignotement():
    global Fond_Menu,Reset_Check
    if Reset_Check==0:
        canvasmenu.delete(Fond_Menu)
        Fond_Menu=canvasmenu.create_image(0,0,image=background_mainmenu_bonus1,anchor="nw")
        canvasmenu.lift(Claptrap_Menu)
        mainF.after(500,Clignotement2)

def Clignotement2():
    global Fond_Menu,Reset_Check
    if Reset_Check==0:
        canvasmenu.delete(Fond_Menu)
        Fond_Menu=canvasmenu.create_image(0,0,image=background_mainmenu_bonus2,anchor="nw")
        canvasmenu.lift(Claptrap_Menu)
        mainF.after(500,Clignotement)

def ResetMenu(event):
    global clefx,clefy,bonusx,bonusy,PorteOuverte,Cercle_Menu,Claptrap_Menu,Porte_Menu,Clef_Menu,Bonus_Menu,Reset_Check
    canvasmenu.delete("all")
    canvasmenu.unbind("<Motion>")
    canvasmenu.unbind("<Button-1>")
    Fond_Menu=canvasmenu.create_image(0,0,image=background_mainmenu,anchor="nw")
    Claptrap_Menu=canvasmenu.create_image(44+15,48,image=Claptrap,tags="Claptrap")
    PorteOuverte=0
    Porte_Menu=canvasmenu.create_image(242,48,image=Porte)
    clefx,clefy=randint(50,450),randint(100,500)
    Clef_Menu=canvasmenu.create_image(clefx,clefy,image=Clef)
    bonusx,bonusy=randint(50,450),randint(100,500)
    Bonus_Menu=canvasmenu.create_image(bonusx,bonusy,image=Bonus)
    Cercle_Menu=canvasmenu.create_image(event.x,event.y,image=Cercle)
    canvasmenu.bind("<Motion>",MenuMove)
    canvasmenu.bind("<Button-1>",MenuCheck)
    Reset_Check=1




canvasmenu=Canvas(mainF,width=500,height=600)
canvasmenu.pack()
Fond_Menu=canvasmenu.create_image(0,0,image=background_mainmenu,anchor="nw")


# Fonctionnalités pour le menu intéractif : introduit les éléments basiques du jeu
Claptrap_Menu=canvasmenu.create_image(44+15,48,image=Claptrap,tags="Claptrap")
PorteOuverte=0
Porte_Menu=canvasmenu.create_image(242,48,image=Porte)
clefx,clefy=randint(50,450),randint(100,500)
Clef_Menu=canvasmenu.create_image(clefx,clefy,image=Clef)
bonusx,bonusy=randint(50,450),randint(100,500)
Bonus_Menu=canvasmenu.create_image(bonusx,bonusy,image=Bonus)
Cercle_Menu=canvasmenu.create_image(250,300,image=Cercle)
Reset_Check=0

canvasmenu.bind("<Motion>",MenuMove)
canvasmenu.bind("<Button-1>",MenuCheck)
mainF.bind("<Return>",ResetMenu)

Jouer=Button(canvasmenu,text="Jouer",font="Constantia 15",width="14",justify="center",overrelief="groove",bg="white",activeforeground="blue",activebackground="white",command=Niveau)
Jouer.place(x=250,y=220,anchor="center")

Leaderboard=Button(canvasmenu,text="Tableau des scores",width="14",font="Constantia 15",justify="center",overrelief="groove",bg="white",activeforeground="blue",activebackground="white",command=Scoreboard)
Leaderboard.place(x=250,y=320,anchor="center")

Quitter=Button(canvasmenu,text="Quitter",width="14",font="Constantia 15",justify="center",overrelief="groove",bg="white",activeforeground="blue",activebackground="white",command=Quit)
Quitter.place(x=250,y=420,anchor="center")




mainF.mainloop()
