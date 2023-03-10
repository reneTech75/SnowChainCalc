from math import pi
import tkinter as tk
from PIL import ImageTk, Image

#SNOW CHAIN DETERMINATION
#The purpose of this application is to help the user see if a snow chain
#with specs close to but not exactly like those of their tires will fit.
#there are ten input fields on the gui, one of which is for the tire specs
#of the user, and the other nine are specs to be tested. The basic premise
#is to find which of the specs on the list closely matches those of the user.
#so the circumfrence of the user's tires is matched with the length of the
#snow chain, and the width of the snow chain is matched with the width plus
#roughly twice the height of the tire wall.

h=0.05 #height of entry is 0.05% of frame
w=0.90 #width is 90% of frame

def entryBuilder(name,space,xpos=0.01,ypos=0.01,h=0.30):
    name = tk.Entry(space,bg='grey',fg='black',font=('',20))
    name.place(relx=xpos,rely=ypos,relheight=h,relwidth=0.98)

win = tk.Tk()
win.title('Snow Chain Calculator')
canvas = tk.Canvas(win,height=400,width=600,bg='black')
canvas.pack()

img = ImageTk.PhotoImage(Image.open("Atlanta.JPG").resize((600,400),Image.ANTIALIAS))
canvas.background=img
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

#we are now going to create three frame.
leftFrame=tk.Frame(canvas,bg='#4287f5')
leftFrame.place(relx=0.01,rely=0.20,relheight=0.6,relwidth=0.327)

middleFrame=tk.Frame(canvas,bg='#4287f5')
middleFrame.place(relx=0.338,rely=0.01,relheight=0.98,relwidth=0.327)

rightFrame=tk.Frame(canvas,bg='#4287f5')
rightFrame.place(relx=0.666,rely=0.20,relheight=0.60,relwidth=0.327)

#entries for the left frame
entryBuilder('leftTop',leftFrame,0.01,0.01)#build lefttop entry
entryBuilder('leftMiddle',leftFrame,0.01,0.32)#build leftmiddle entry
entryBuilder('leftBottom',leftFrame,0.01,0.63)#build leftbottom entry

#entries for the middle frame
entryBuilder('myEntry',middleFrame,0.01,0.01,0.183)#build myEntry
entryBuilder('middleTop',middleFrame,0.01,0.198,0.183)#build myEntry
entryBuilder('middleMiddle',middleFrame,0.01,0.386,0.183)#build middleMiddle entry
entryBuilder('middleBottom',middleFrame,0.01,0.574,0.183)#build middleMiddle entry

#entries for the right frame
entryBuilder('rightTop',rightFrame,0.01,0.01)#build lefttop entry
entryBuilder('rightMiddle',rightFrame,0.01,0.32)#build leftmiddle entry
entryBuilder('rightBottom',rightFrame,0.01,0.63)#build leftbottom entry

#the calculate button
cal=tk.Button(middleFrame,text='CALCULATE',font=('',20),bg='grey',fg='black',bd=4)
cal.place(relx=0.01,rely=0.8,relheight=0.183,relwidth=0.98)
win.mainloop()