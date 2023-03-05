# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("birthdday.JPG"))

# Create a Label Widget to display the text or Image
label1 = Label(win,bg='grey',fg='black',text='help us')
label1.place(relx=0.01,rely=0.01,relwidth=0.1,relheight=0.1)
label = Button(frame, bd=4,image = img)
label.pack()

win.mainloop()