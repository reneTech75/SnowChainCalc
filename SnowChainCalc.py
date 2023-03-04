from math import pi
import tkinter as tk

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
names=['lefttop','leftMiddle','leftBottom','myEntry','middleTop','middleMiddle','middleBottom','rightTop','rightMiddle','rightBottom']

#def entryBuilder(xpos=0.01,ypos=0.01):
#    entry1 = tk.Entry(frame1,bg='grey',fg='black',font=('',20))
#    entry1.place(relx=xpos,rely=ypos,relheight=0.30,relwidth=0.98)

win = tk.Tk()
win.title('Snow Chain Calculator')
canvas = tk.Canvas(win,height=400,width=700,bg='black')
canvas.pack()

#we are now going to create three frame.
frame1=tk.Frame(canvas,bg='#4287f5')
frame1.place(relx=0.01,rely=0.20,relheight=0.6,relwidth=0.327)

frame2=tk.Frame(canvas,bg='#4287f5')
frame2.place(relx=0.338,rely=0.01,relheight=0.98,relwidth=0.327)

frame3=tk.Frame(canvas,bg='#4287f5')
frame3.place(relx=0.666,rely=0.20,relheight=0.60,relwidth=0.327)

#entryBuilder(0.01,0.01)#build the first entry in frame1
#entryBuilder(0.01,0.32)#build the second entry in frame1
#entryBuilder(0.01,0.63)#build the 3rd entry in frame1
#entryBuilder(0.01,0.01,frame2)#build the first entry in frame2


win.mainloop()