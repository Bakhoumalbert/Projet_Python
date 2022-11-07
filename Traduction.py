from tkinter import *
from googletrans import Translator
from tkinter import ttk

source = ""
destination = ""
t = ""

#--------- MES FONCTIONS -----------------------------------------------------------------

def comboAction(event): # recupere les selections des listes combobox
	global source
	global destination
	source = listDeroulantChoix.get()
	destination = listDeroulantTraduct.get()

def Traduct(event):
	trans = Translator()
	global t
	t = T1.get("1.0", END) # 1.0 signifie (1) premiere ligne (0) caractere numero 0
	print(t)
	# Traduire le texte
	translated = trans.translate(t, src = listDeroulantChoix.get(), dest = listDeroulantTraduct.get())
	print(translated)
	# Recuperer le texte traduit
	traduct = translated.text
	T2.delete('1.0', END) # Vider le champ de traduction
	T2.insert(END, traduct) # inserer la traduction
#------------------------------------------------------------------------------------
root = Tk()
root.geometry("800x300")

#---------------------------------------------------
# Creation de la liste combobox
#---------------------------------------------------
labelChoixLang = Label(root, text = "Choisi la langue source")
labelChoixLang.place(x = 20, y = 50)

labelLangTraduct = Label(root, text = "Langue destination")
labelLangTraduct.place(x = 430, y = 50)

#La liste des langues
languages = ['fr', 'en', 'es', 'ar']
#------------------------------------------------------------------
# Creation de liste deroulant pour les langues
listDeroulantChoix = ttk.Combobox(root, values = languages)
listDeroulantChoix.place(x = 200, y = 50)
listDeroulantChoix.current(1)
listDeroulantChoix.bind("<<ComboboxSelected>>", comboAction)

listDeroulantTraduct = ttk.Combobox(root, values = languages)
listDeroulantTraduct.place(x = 600, y = 50)
listDeroulantTraduct.bind("<<ComboboxSelected>>", comboAction)



T1 = Text(root)
T1.place(x = 20, y = 100, width = 400, height = 150)
T1.bind("<Return>", Traduct)

T2 = Text(root)
T2.place(x = 430, y = 100, width = 400, height = 150)


root.mainloop()
