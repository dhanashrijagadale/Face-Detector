from tkinter import *
import os
def restart():
    os.system("shutdown /r/t/1")
def restartTime():
    os.system("shutdown /r/t/20")
def logoff():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s/t/1")

st=Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Pink")

r_button=Button(st,text="Restart",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button=Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,command=restartTime)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button=Button(st,text="logout",font=("Time New Roman",20,"bold"),relief=RAISED,command=logoff)
lg_button.place(x=150,y=270,height=50,width=200)

st_button=Button(st,text="shutdown",font=("Time New Roman",20,"bold"),relief=RAISED,command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)




st.mainloop()
