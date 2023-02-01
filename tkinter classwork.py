from tkinter import *
window = Tk()

text1 = Label(window,text="username")
text1.grid(column=0,row=0)

text2 =Label(window,text="password")
text2.grid(column=0,row=1)


ent1 =Entry(window)
ent1.grid(column=1,row=0)

ent2 =Entry(window)
ent2.grid(column=1,row=1)

but =Button(window,text='Login' ,bg="light blue",fg="black",padx=10,pady=10)
but.grid(column=1,row=2)
            


window.mainloop()
