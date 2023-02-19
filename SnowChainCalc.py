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

win = tk.Tk()
win.title('Snow Chain Calculator')
canvas = tk.Canvas(win,height=500,width=700,bg='black')
canvas.pack()





win.mainloop()
