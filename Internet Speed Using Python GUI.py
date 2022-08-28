from tkinter import *
import speedtest

def speed():
    import speedtest
    sp = speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/((10**6))*0.125,3)) + " MBPS"
    up= str(round(sp.upload()/((10**6))*0.125,3)) + " MBPS"
    lab_d.config(text=down)
    lab_u.config(text=up)



st=Tk()
st.title("Internet Speed")
st.geometry("500x700")
st.config(bg="Pink")
lab=Label(st,text="Internet Speed",font=("Time New Roman",20,"bold"),cursor="plus")
lab.place(x=50,y=50,height=50,width=400)

lab_down=Label(st,text="Downloading Speed",font=("Time New Roman",20,"bold"),cursor="plus")
lab_down.place(x=50,y=130,height=50,width=400)

lab_u=Label(st,text="00",font=("Time New Roman",20,"bold"),cursor="plus")
lab_u.place(x=50,y=200 ,height=50,width=400)

lab_up=Label(st,text="Uploading Speed",font=("Time New Roman",20,"bold"),cursor="plus")
lab_up.place(x=50,y=290,height=50,width=400)

lab_d=Label(st,text="00",font=("Time New Roman",20,"bold"),cursor="plus")
lab_d.place(x=50,y=360,height=50,width=400)

r_button=Button(st,text="Start",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=speed)
r_button.place(x=150,y=460,height=50,width=200)

st.mainloop()
