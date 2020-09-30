from tkinter import*
from time import*
from random import*
from math import*
import pyautogui

# Définition de la fenêtre du menu principal
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

JouerBouton=PhotoImage(file="img/bouton/jouer.gif")
TableauBouton=PhotoImage(file="img/bouton/tableau.gif")
QuitterBouton=PhotoImage(file="img/bouton/quitter.gif")


# Mouvement du personnage :
# Modifie les coordonnées du personnage en permanence
# Vérifie la touche appuyée avant d'effectuer le déplacement
# Fonction détaillée dans le dossier-projet

collision_status=0
def move(event):
    global Lab,C,perso,new_coords,largeur,hauteur
    mouse_coords=pyautogui.position()
    new_coords=(mouse_coords[0],mouse_coords[1])
    mx,my=new_coords[0],new_coords[1]

    largeur_big=(largeur*3)*32+60
    hauteur_big=(hauteur*3)*22+60
    if abs(mx-C.coords(perso)[0])<50 and abs(my-C.coords(perso)[1])<50:
        if 0<=mx<=largeur_big and 0<=my<=hauteur_big:

            tuple_id=C.find_overlapping(mx-10,my-10,mx+10,my+10)
            tag_collision=C.gettags(tuple_id[0])

            if "mur" not in tag_collision:
                C.coords(perso,mx,my)
            else:
                pyautogui.moveTo(C.coords(perso)[0],C.coords(perso)[1])
    else:
        pyautogui.moveTo(C.coords(perso)[0],C.coords(perso)[1])
    return

def click(event):
    mouse_coords=pyautogui.position()
    new_coords=(mouse_coords[0],mouse_coords[1])
    mx,my=new_coords[0],new_coords[1]





def Pause(event):
    return

# Définition du labyrinthe qui fonctionne selon deux boucles "for" en lisant dans un fichier formaté spécialement
# Le bonus marche différemment, celui-ci doit être supprimé un par un donc il nécessite des tags différents

def make_maze(w,h):
    global perso
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["m##"] * w + ['m'] for _ in range(h)] + [[]]
    hor = [["mmm"] * w + ['m'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "m##"
            if yy == y: ver[y][max(x, xx)] = "###"
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s

def Tkinter_Maze(event):
    global Lab,C,largeur,hauteur,perso
    C.delete("all")
    C.config(width=(largeur*3)*32+60,height=(hauteur*3)*22+60)
    Maze=make_maze(largeur,hauteur)
    fich=open("maze.txt","w")
    fich.write(str(Maze))
    fich.close()

    fich=open("maze.txt","r")
    List_Maze=fich.readlines()
    fich.close()

    a,b=0,0
    Goal_Number=0
    for y in range(0,len(List_Maze)-1):
        a+=1
        b=0
        Goal_Random_a=randint(len(List_Maze)-6,len(List_Maze)-2)
        if Goal_Number==0 and y==len(List_Maze)-3:
            Goal_Random_a=a

        for k in List_Maze[y]:
            b+=1

            if Goal_Number==0 and b==len(List_Maze[y])-2:
                Goal_Random_b=b
            else:
                Goal_Random_b=randint(1,len(List_Maze[y])-2)

            if "m" in k:
                #C.create_image(15+30*x,15+30*y,image=Mur,tags="piege")
                C.create_image(15+30*b,15+30*a,image=Mur,tags="mur")
            elif Goal_Number==0 and Goal_Random_a==a and Goal_Random_b==b:
                C.create_image(15+30*b,15+30*a,image=Arrive,tags="goal")
                Goal_Number=1
    if Goal_Number==0:
        print(Goal_Random_a,Goal_Random_b)
    Pers=PhotoImage(file="img/only_mouse.gif")
    perso=C.create_image(90,90,image=Pers,tags="Personnage")
    C.mainloop()

def Labyrinthe():
    global C,Lab,perso,Pers,niveau,hauteur,largeur
    Lab.deiconify()


    Niveau.quit()

    C.config(width=(largeur*3)*32+60,height=(hauteur*3)*22+60)
    Maze=make_maze(largeur,hauteur)
    fich=open("maze.txt","w")
    fich.write(str(Maze))
    fich.close()

    fich=open("maze.txt","r")
    List_Maze=fich.readlines()
    fich.close()

    a,b=0,0
    Goal_Number=0
    for y in range(0,len(List_Maze)-1):
        a+=1
        b=0
        Goal_Random_a=randint(len(List_Maze)-6,len(List_Maze)-2)
        if Goal_Number==0 and y==len(List_Maze)-3:
            Goal_Random_a=a

        for k in List_Maze[y]:
            b+=1

            if Goal_Number==0 and b==len(List_Maze[y])-2:
                Goal_Random_b=b
            else:
                Goal_Random_b=randint(1,len(List_Maze[y])-2)

            if "m" in k:
                C.create_image(15+30*b,15+30*a,image=Mur,tags="mur")
            elif Goal_Number==0 and Goal_Random_a==a and Goal_Random_b==b:
                C.create_image(15+30*b,15+30*a,image=Arrive,tags="goal")
                Goal_Number=1
    if Goal_Number==0:
        print(Goal_Random_a,Goal_Random_b)



    Pers=PhotoImage(file="img/only_mouse.gif")
    perso=C.create_image(90,90,image=Pers,tags="Personnage")

    pyautogui.FAILSAFE=False
    #CreateChrono()

    Lab.bind("<Motion>",move)
    Lab.bind("<Escape>",Tkinter_Maze)
    Lab.bind("<Button-1>",click)


    C.mainloop()

# Ligne d'arrivée
def goal():
    global C,Lab,Niveau,temps,Goal,tvar,Classement

    mainF.deiconify()

    # Simule l'entrée dans score pour retrouver le classement (utile pour afficher sans avoir encore enregistré dans le fichier)
    # Pour l'écriture "1er" et "nème" vérifie le classement
    CheckClassement("pour victoire")
    if int(Classement)==1:
        TexteClassement=str(Classement)+"er"
    elif int(Classement)>=1:
        TexteClassement=str(Classement)+"ème"

    # Fenêtre pour enregistrer le score. Affiche le classement et le temps, demande le nom du joueur pour enregistrer
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

    # Exécute "SaveScore()" lorsque le bouton est appuyé
    BoutonNom=Button(Goal,text="Enregistrer",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=SaveScore)
    BoutonNom.pack(padx=10,pady=10)

# Fonction qui sert à enregistrer un score. Elle enregistre alors le nom et le temps dans un fichier de score commun au niveau, et également en tant que dernier score enregistré avec son classement
def SaveScore():
    global temps,Goal,tvar,niveau,ScoreJoueur,NomJoueur,Classement
    Goal.destroy()
    Goal.quit()

    NomSave="scores/"+str(niveau)+".txt"

    # Enregistre le score dans le fichier commun au niveau
    ScoreJoueur=temps
    NomJoueur=tvar.get()
    fich=open(NomSave,"a")
    fich.write(NomJoueur+"\n")
    fich.write(ScoreJoueur+"\n")
    fich.close()

    # Enregistre en tant que "dernier score" du niveau, avec son classement
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


# Méthode permettant de récupérer le classement d'un score.
# Exécuté deux fois : l'une pour afficher simplement le classement sans l'enregistrer, le second servant à enregistrer le classement (ce qui sert au tableau des scores)
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


# Bouton pour quitter le jeu (sur la fenêtre principale)
def Quit():
    mainF.destroy()


# Lorsque le joueur appuie sur le bouton "Facile" dans la sélection du niveau.
# Défini les coordonnées du personnage (pour gérer les mouvements), la hauteur/largeur à 30/30 (pareil pour tous les niveaux), défini la variable "niveau" utile pour enregistrer les scores, et ouvre le labyrinthe
def BoutonConfirmer():
    global niveau,hauteur,largeur,hauteurvar,largeurvar
    hauteur=int(hauteurvar.get())
    largeur=int(largeurvar.get())
    niveau="facile"
    Lab.title("Claptrap's Maze - Difficulté : FACILE")

    Labyrinthe()






# Fenêtre de sélection du niveau
# D'abord, ferme le labyrinthe ou la fenêtre de sélectiondu niveau si ils existaient déjà
def SelectionNiveau():
    global Niveau,hauteurvar,largeurvar

    try:
        Lab.destroy()
        Lab.quit()
        Niveau.destroy()
        Niveau.quit()
    except:
        False

    Niveau=Toplevel()

    Niveau.title("Sélection du niveau")
    Niveau.resizable(width=False,height=False)
    Niveau.iconbitmap("img/icone/claptrap.ico")

    canvasniveau=Canvas(Niveau)
    canvasniveau.grid(row=0,column=0,rowspan=2,columnspan=3)
    canvasniveau.create_image(0,0,image=background_image,anchor="nw")



    hauteurvar=IntVar()
    ChampHauteur=Entry(canvasniveau,textvariable=hauteurvar,font="Constantia 18",width=10)
    ChampHauteur.grid(row=0,column=0,padx=10,pady=10)

    largeurvar=IntVar()
    ChampLargeur=Entry(canvasniveau,textvariable=largeurvar,font="Constantia 18",width=10)
    ChampLargeur.grid(row=0,column=2,padx=10,pady=10)

    Confirm=Button(canvasniveau,text="Confirmer",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=BoutonConfirmer)
    Confirm.grid(row=1,column=1,padx=10,pady=10)


    # Démarre la fonction qui initialise le labyrinthe
    LabFen()

    Niveau.mainloop()

# Fonction qui initialise le labyrinthe avant que le niveau soit sélectionné
def LabFen():
    global C,Lab

    Lab=Toplevel()

    Lab.title("En attente du choix du niveau...")
    Lab.iconbitmap("img/icone/claptrap.ico")
    Lab.attributes("-fullscreen",1)
    #Lab.config(cursor="none")
    Lab.iconify()

    C=Canvas(Lab,width=1920,height=1080)
    C.pack(anchor="nw")

# Fonction qui permet l'affichage des scores.
# Utilise les deux fonctions "TriScore" et "TriDernierScore"
# Selon le nombre de scores, et s'il existe ou non un dernier score, la fonction va afficher différement le tableau des scores.

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


# Fonction qui permet de trier la liste des scores d'un niveau
# Fonction détaillée dans le dossier-projet
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

# Fonction qui permet de trier le dernier score d'un niveau
# Fonction détaillée dans le dossier-projet
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

# Fenêtre du tableau des scores
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

# Onglet facile du tableau des scores
# Utilise la fonction "LireScore" pour afficher les scores du niveau "facile"
def OngletFacile():
    global FenScore
    FenScore=Toplevel()
    FenScore.title("Niveau : FACILE")
    FenScore.resizable(width=False,height=False)
    FenScore.iconbitmap("img/icone/claptrap.ico")
    LireScore("facile")
    return

# Onglet moyen du tableau des scores
# Utilise la fonction "LireScore" pour afficher les scores du niveau "moyen"
def OngletMoyen():
    global FenScore
    FenScore=Toplevel()
    FenScore.title("Niveau : MOYEN")
    FenScore.resizable(width=False,height=False)
    FenScore.iconbitmap("img/icone/claptrap.ico")
    LireScore("moyen")
    return

# Onglet difficile du tableau des scores
# Utilise la fonction "LireScore" pour afficher les scores du niveau "difficile"
def OngletDifficile():
    global FenScore
    FenScore=Toplevel()
    FenScore.title("Niveau : DIFFICILE")
    FenScore.resizable(width=False,height=False)
    FenScore.iconbitmap("img/icone/claptrap.ico")
    LireScore("difficile")
    return

# Fonction qui crée l'interface du chronomètre, et récupère la première input du temps
# Exécute à la fin la fonction "Chrono"
def CreateChrono():
    global debut,TexteChrono,ImgChrono
    # Temps de début, récupéré une seule fois par niveau
    debut=time()
    FrameChrono=Frame(Lab,bg="black")
    FrameChrono.place(x=810,y=2)

    TexteChrono=Label(FrameChrono,text="00:00",font="Helvetica 14",fg="white",bg="black")
    TexteChrono.pack(side="right")

    imgchrono=Label(FrameChrono,image=ImgChrono,bg="black")
    imgchrono.pack(side="left")

    Chrono()


    Lab.mainloop()

# Fait fonctionner le chronomètre en actualisant chaque seconde le temps affiché
# Le temps affiché est une différence entre le temps de début et le temps de fin
def Chrono():
    global debut,TexteChrono,Status,temps
    # Temps récupéré chaque seconde, permettant de faire la différence entre "début" et "fin"
    fin=time()
    difference=fin-debut

    # Formate le temps sous le format "MINUTE : SECONDE"
    local=localtime(difference)
    temps=strftime("%M:%S",local)

    TexteChrono.config(text=temps)
    TexteChrono.update()

    # S'actualise chaque seconde
    Lab.after(1000,Chrono)


# Chaque fois que la souris bouge, déplace le cercle sur la souris si c'est possible et déplace également Claptrap (y=48 correspond à la hauteur du passage sans mur)
# Si la porte est fermée, Claptrap ne peut pas la dépasser (x=44 correspond au départ, 212 à la porte)
# Si la porte est ouverte, Claptrap peut se déplacer au-delà (x=455 correspond à la fin de l'arrivée)

def MenuMove(event):
    #global Cercle_Menu,Claptrap_Menu
    mx,my=event.x,event.y
    if 0<=mx<=500 and 0<=my<=600:
        canvasmenu.coords(Cercle_Menu,mx,my)
    if PorteOuverte==0:
        if mx>44 and mx<212:
            canvasmenu.coords(Claptrap_Menu,mx,48)
    if PorteOuverte==1:
        if mx>44 and mx<455:
            canvasmenu.coords(Claptrap_Menu,mx,48)
        return


# En appuyant sur le clic, vérifie quel objet est appuyé pour agir en conséquence
def MenuCheck(event):
    global clefx,clefy,bonusx,bonusy,PorteOuverte,Cercle_Menu,Reset_Check,canvasmenu,Clignotement_Status
    mx,my=event.x,event.y


    # Vérifie si le clic est sur la ligne d'arrivée - exécute le clignotement du niveau, en annulant "Reset_Check"
    if PorteOuverte==1:
        if mx>425 and 33<=my<=63 and Clignotement_Status==0:
            canvasmenu.delete(Cercle_Menu)
            Clignotement_Status=1
            Reset_Check=0
            Clignotement()


    # Vérifie si le clic est sur la clef - cela détruit la clef et la porte
    if abs(mx-clefx)<=16 and abs(my-clefy)<=16:
        canvasmenu.delete(Clef_Menu)
        canvasmenu.delete(Porte_Menu)
        PorteOuverte=1


    # Vérifie si le clic est sur le bonus - cela agrandit le cercle autour du curseur
    elif abs(mx-bonusx)<=10 and abs(my-bonusy)<=10 and Clignotement_Status==0:
        canvasmenu.delete(Bonus_Menu)
        canvasmenu.delete(Cercle_Menu)
        Cercle_Menu=canvasmenu.create_image(mx,my,image=NewCercle)


    # Vérifie pour les boutons. x=250 / y(Jouer)=220 / y(Tableau)=320 / y(Quitter)=420
    # Hauteur d'un bouton : 41
    # Largeur d'un bouton : 177
    elif abs(mx-250)<=88 and abs(my-220)<=20:
        SelectionNiveau()

    elif abs(mx-250)<=88 and abs(my-320)<=20:
        Scoreboard()

    elif abs(mx-250)<=88 and abs(my-420)<=20:
        Quit()


# Exécuté quand la ligne d'arrivée est appuyée (si la porte est ouverte)
# Fait clignoter le menu entre deux images, mais arrête si le bouton de reset (entrée) est appuyé (vérifié par Reset_Check)
def Clignotement():
    global Fond_Menu,Reset_Check
    if Reset_Check==0:
        canvasmenu.delete(Fond_Menu)
        Fond_Menu=canvasmenu.create_image(0,0,image=background_mainmenu_bonus1,anchor="nw")
        canvasmenu.lift(Claptrap_Menu)
        canvasmenu.lift(Jouer)
        canvasmenu.lift(Tableau)
        canvasmenu.lift(Quitter)

        mainF.after(500,Clignotement2)

def Clignotement2():
    global Fond_Menu,Reset_Check
    if Reset_Check==0:
        canvasmenu.delete(Fond_Menu)
        Fond_Menu=canvasmenu.create_image(0,0,image=background_mainmenu_bonus2,anchor="nw")
        canvasmenu.lift(Claptrap_Menu)
        canvasmenu.lift(Jouer)
        canvasmenu.lift(Tableau)
        canvasmenu.lift(Quitter)
        mainF.after(500,Clignotement)

# En appuyant sur la touche entrée, cela réinitialise
def ResetMenu(event):
    global clefx,clefy,bonusx,bonusy,PorteOuverte,Cercle_Menu,Claptrap_Menu,Porte_Menu,Clef_Menu,Bonus_Menu,Reset_Check,Jouer,Tableau,Quitter,Clignotement_Status
    canvasmenu.delete("all")
    canvasmenu.unbind("<Motion>")
    canvasmenu.unbind("<Button-1>")
    Fond_Menu=canvasmenu.create_image(0,0,image=background_mainmenu,anchor="nw")
    Jouer=canvasmenu.create_image(250,220,image=JouerBouton)
    Tableau=canvasmenu.create_image(250,320,image=TableauBouton)
    Quitter=canvasmenu.create_image(250,420,image=QuitterBouton)
    Claptrap_Menu=canvasmenu.create_image(44+15,48,image=Claptrap,tags="Claptrap")
    PorteOuverte=0
    Porte_Menu=canvasmenu.create_image(242,48,image=Porte)
    clefx,clefy=randint(50,450),randint(100,500)
    Clef_Menu=canvasmenu.create_image(clefx,clefy,image=Clef)
    bonusx,bonusy=randint(50,450),randint(100,500)
    Bonus_Menu=canvasmenu.create_image(bonusx,bonusy,image=Bonus)
    Cercle_Menu=canvasmenu.create_image(event.x,event.y,image=Cercle)
    Clignotement_Status=0
    canvasmenu.bind("<Motion>",MenuMove)
    canvasmenu.bind("<Button-1>",MenuCheck)
    Reset_Check=1




canvasmenu=Canvas(mainF,width=500,height=600)
canvasmenu.pack()
Fond_Menu=canvasmenu.create_image(0,0,image=background_mainmenu,anchor="nw")

Jouer=canvasmenu.create_image(250,220,image=JouerBouton)
Tableau=canvasmenu.create_image(250,320,image=TableauBouton)
Quitter=canvasmenu.create_image(250,420,image=QuitterBouton)


# Fonctionnalités pour le menu intéractif
# Sert de mini-tutoriel pour introduire les éléments basiques du jeu
# Utilise les fonctions : MenuMove - MenuCheck - ResetMenu

Claptrap_Menu=canvasmenu.create_image(44+15,48,image=Claptrap,tags="Claptrap")
Porte_Menu=canvasmenu.create_image(242,48,image=Porte)
clefx,clefy=randint(50,450),randint(100,500)
Clef_Menu=canvasmenu.create_image(clefx,clefy,image=Clef)
bonusx,bonusy=randint(50,450),randint(100,500)
Bonus_Menu=canvasmenu.create_image(bonusx,bonusy,image=Bonus)
Cercle_Menu=canvasmenu.create_image(250,300,image=Cercle)
PorteOuverte=0
Reset_Check=0
Clignotement_Status=0

canvasmenu.bind("<Motion>",MenuMove)
canvasmenu.bind("<Button-1>",MenuCheck)
mainF.bind("<Return>",ResetMenu)


mainF.mainloop()
