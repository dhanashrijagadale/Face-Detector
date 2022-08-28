from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


def change(text="type",soe="English",desting="Hindi"):
    text1=text
    src1=soe
    dest1=desting
    trans=Translator(service_urls=['translate.googleapis.com'])
    trans1=trans.translate(text,soe=src1,desting=dest1)
    return trans1.text

def data():
    s=combo_src.get()
    d=des_src.get()
    message=srct.get(1.0,END)
    text_get= change(text=message, soe=s, desting=d)
    dest.delete(1.0,END)
    dest.insert(END,text_get)


root=Tk()
root.title("Google Translator")
root.geometry("500x700")
root.config(bg="pink")

lab_text=Label(root,text="Translator",font=("Times New Roman",30))
lab_text.place(x=100,y=20,width=300,height=50)
frame=Frame(root).pack(side=BOTTOM)


SRC_text=Label(root,text="Text",font=("Times New Roman",20),bg="pink")
SRC_text.place(x=5,y=110,width=100,height=40)


srct= Text(frame,font=("Times New Roman",30),wrap=WORD)
srct.place(x=10,y=150,width=480,height=50)

list_text=list(LANGUAGES.values())

combo_src=ttk.Combobox(frame,value=list_text)
combo_src.place(x=10,y=220,width=100,height=50)
combo_src.set("English")

button_change=Button(frame,text="Transalate",relief=RAISED,command=data)
button_change.place(x=120,y=220,width=100,height=50)

des_src= ttk.Combobox(frame,value=list_text)
des_src.place(x=230,y=220,width=100,height=50)
des_src.set("Hindi")

dest = Text(frame,font=("Times New Roman",30),wrap=WORD)
dest.place(x=10,y=300,width=480,height=100)


root.mainloop()