from tkinter import *
import pygame
from tkinter import filedialog
import os
from pygame import mixer

root=Tk()
root.title("music player")
root.geometry("500x300")
root.config(bg='white')
mixer.init()




song_box=Listbox(root,bg='blue',fg='light pink',width='60')
song_box.grid (pady=20)

def add_songs():
    song=filedialog.askopenfilename(initialdir=r"C:/Users/MORNING SESSION SDL5/Documents/Audio",title="choose a song",filetypes=(("mp3 files","*.mp3"),))
    song_box.insert(END,song)
    song = song.replace(r"C:/Users/MORNING SESSION SDL5/Documents/Audio","")
    song=song.replace(".mp3","")
                                                                                            

def play():
    song =song_box.get(ACTIVE)
    song =  f'C:/Users/MORNING SESSION SDL5/Documents/Audio{song}.mp3'
    song = song.replace(".mp3","")
    mixer.music.load(song_box.get(ACTIVE))
    pygame.mixer.music.play()

def stop():
    mixer.music.stop()


global paused
paused=False

def pause():
    global paused
    if paused:
       pygame.mixer.music.unpause()
       paused=False
    
    else:
         pygame.mixer.music.pause()
         paused=True

def previous():
    previous=song_box.curselection()
    previous=previous[0]-1
    song=song_box.get(previous)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    song_box.selection_clear(0,END)
    song_box.activate(previous)
    song_box.selection_set(previous)

def next():
    next=song_box.curselection()
    next=next[0]+1
    song=song_box.get(next)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    song_box.selection_clear(0,END)
    song_box.activate(next)
    song_box.selection_set(next)


def volume(val):
    volume= float(val)/100
    mixer.music.set_volume(volume)
    muted=FALSE



prev_btn_img=PhotoImage(file=r"C:\Users\MORNING SESSION SDL5\Desktop\prev.png ")
next_btn_img=PhotoImage(file=r"C:\Users\MORNING SESSION SDL5\Desktop\next.png")
play_btn_img=PhotoImage(file=r"C:\Users\MORNING SESSION SDL5\Desktop\play.png")
pause_btn_img=PhotoImage(file=r"C:\Users\MORNING SESSION SDL5\Desktop\pause.png")
stop_btn_img=PhotoImage(file=r"C:\Users\MORNING SESSION SDL5\Desktop\stop.png")


controls_frame=Frame(root)
controls_frame.grid()


#Buttons
prev_btn=Button(controls_frame,image=prev_btn_img,borderwidth=0,command=previous)
next_btn=Button(controls_frame,image=next_btn_img,borderwidth=0,command=next)
play_btn=Button(controls_frame,image=play_btn_img,borderwidth=0,command=play)
pause_btn=Button(controls_frame,image=pause_btn_img,borderwidth=0,command=pause)
stop_btn=Button(controls_frame,image=stop_btn_img,borderwidth=0,command=stop)

prev_btn.grid(row=0,column=0,padx=10)
next_btn.grid(row=0,column=1,padx=10 )
play_btn.grid(row=0,column=2,padx=10 )
pause_btn.grid(row=0,column=3,padx=10 )
stop_btn.grid(row=0,column=4,padx=10)

my_menu=Menu(root)
root.config(menu=my_menu)

volume_frame=LabelFrame(root,text="volume")
volume_frame.grid(column=2,row=3)
volume_slide = Scale(root,command=volume,width=10,length=150)
mixer.music.set_volume(0.7)
volume_slide.grid(column=5,row=0)

add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="add songs", menu=add_song_menu,command=add_songs)
add_song_menu.add_command(label="add song to playlist",command=add_songs)






root.mainloop()
