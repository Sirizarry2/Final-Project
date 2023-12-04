from tkinter import *
from PIL import ImageTk,Image

#First Window setup
window= Tk()
window.title("Kiki's Krystals")
window.resizable(width=True, height=True)

#Image placement in first window
Kikiscrystals = PhotoImage(file= 'C:\\Users\\Suzy\\OneDrive\\Software dev\\FinalProject\\Kikiscrystals.jpg')
my_img =ImageTk.PhotoImage(Image.open("Kikiscrystals.jpg"))
my_label = Label(image=my_img)
my_label.grid(row=0, column=0)

#Creating label widgets
myLabel = Label(window, text= "Kiki's Krystals")
myLabel.grid(row=0, column=3)
myLabel2 = Label(window, text= "Check out my crystals!")
myLabel2.grid(row=1, column=3)

#Function for button in first window
def myClick():
    myLabel = Label(window, text="The price of this crystal is $10.")
    myLabel.grid(row=5, column=4)

#Creating buttons for first window
myButton = Button(window, text= "Click Here", command= myClick, bg="purple", fg="white")
myButton.grid(row=4, column=4)

#Function for second window
def open():
    #Second window setup
    top = Toplevel()
    top.title("Kiki's Information")
    top.resizable(width=True, height=True)

#Button on Home page for second window
btn = Button(window, text="More about the brand", command= open, bg="purple", fg="white")
btn.grid(row=0, column=4)

#Label widgets for second window


#Button to quit program
btn_quit = Button(window, text= "Exit", command= window.quit)
btn_quit.grid(row=6, column=5)
window.mainloop()