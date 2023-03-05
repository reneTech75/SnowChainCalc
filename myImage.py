# this is a learning process on how to set an image as the background
# of a tkinter GUI. The key thing here is the PIL module together with 
# ImageTk and Image resouces in it. The resize() saves a lot of photo
#editing time in just one stroke.

# Import required libraries
import tkinter as tk
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = tk.Tk()

# Define the geometry of the window
win.geometry("500x500")

canvas=tk.Canvas(win,width=600,height=400)
canvas.pack()
#frame = Frame(win, width=600, height=400)
#frame.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("Atlanta.JPG").resize((600,400),Image.ANTIALIAS))
canvas.background=img
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Put a tkinter widget on the canvas.
#button = tk.Button(win, text="Start")
#button_window = canvas.create_window(10, 10, anchor=tk.NW, window=button)
button=tk.Button(canvas,bg='grey',text='start',fg='black',font=('',15),bd=3)
button.place(relx=0.05,rely=0.05,relwidth=0.15,relheight=0.08)
win.mainloop()