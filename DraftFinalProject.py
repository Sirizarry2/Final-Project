import tkinter
from tkinter import *
from PIL import ImageTk, Image

#First Window setup
window= Tk()
window.title("Kiki's Krystals")
window.resizable(width=True, height=True)
window.iconbitmap('C:/Users/Suzy/pythonProject/venv/Kikiscrystals.ico')

#Creating label widgets
myLabel = Label(window, text= "Kiki's Krystals")
myLabel.grid(row=0, column=4)
myLabel2 = Label(window, text= "Check out my crystals!")
myLabel2.grid(row=1, column=4)
crystal1 = Label(window, text= "This crystal is Rose Quartz. It is for love.")
crystal1.grid(row= 2, column= 3)
crystal2 = Label(window, text= "This is Tigers Eye. It brings clarity and luck.")
crystal2.grid(row= 5, column=3)
crystal3 = Label(window, text= "This crystal is Amethyst. It helps relive stress.")
crystal3.grid(row= 7, column=3)

#Images for first window
crystal1_pic = Image.open('venv/RoseQuartz.jpg')
crystal2_pic = Image.open('venv/TigersEye.jpg')
crystal3_pic = Image.open('venv/Amethyst.jpg')

#Resized first image
resized = crystal1_pic.resize((300, 225))
newCrystalPic_1 = ImageTk.PhotoImage(resized)

#Resized first image placed in first window
crystal1_pic = Label(window, image=newCrystalPic_1)
crystal1_pic.grid(row= 3, column= 3)

#Resized second image
resized = crystal2_pic.resize((300, 225))
newCrystalPic_2 = ImageTk.PhotoImage(resized)

#Resized second image placed in first window
crystal2_pic = Label(window, image= newCrystalPic_2)
crystal2_pic.grid(row= 6, column= 3)

#Resized third image
resized = crystal3_pic.resize((300, 225))
newCrystalPic_3 = ImageTk.PhotoImage(resized)

#Resized thrid image placed in first window
crystal3_pic = Label(window, image= newCrystalPic_3)
crystal3_pic.grid(row= 8, column= 3)

#Function for button in first window
def myClick():
    crystal_1 = Label(window, text="The price of this crystal is $10.")
    crystal_1.grid(row=3, column=6)
    crystal_2 = Label(window, text= "The price of this crystal is $12.")
    crystal_2.grid(row= 6, column= 6)
    crystal_3 = Label(window, text= "The price of this crystal is $10.")
    crystal_3.grid(row= 8, column= 6)

#Creating buttons for first window
crystal_1 = Button(window, text= "Click Here", command= myClick, bg="purple", fg="white")
crystal_1.grid(row=3, column=5)
crystal_2 = Button(window, text= "Click Here", command= myClick, bg= "purple", fg= "white")
crystal_2.grid(row= 6, column= 5)
crystal_3 = Button(window, text= "Click Here", command= myClick, bg= "purple", fg= "white")
crystal_3.grid(row= 8, column= 5)


#Function to open second window
def open():
    #Second window setup
    top = Toplevel()
    top.title("Kiki's Information")
    top.resizable(width=True, height=True)

    # Label widgets for second window
    greeting = Label(top, text= "Hi, my name is Kiki! Thank you for visting my site.")
    greeting.grid(row=0, column= 5)
    myLabel = Label(top, text= "I believe that crystals have the power to boost your mood and help you with other aspects of your life.")
    myLabel.grid(row=1, column=5)

    # Image placement in second window
    global new_img
    top.iconbitmap('C:/Users/Suzy/pythonProject/venv/Kikiscrystals.ico')
    my_img = Image.open("venv/Kikiscrystals.png")

    #Resizing the image on second window
    resized = my_img.resize((210, 100))

    #Placing brand logo on second window
    new_img = ImageTk.PhotoImage(resized)
    my_label = Label(top, image= new_img)
    my_label.grid(row=0, column=0)

    def emailClick():
        emailLabel = Label(top, text= e.get())
        emailLabel.grid(row= 6, column= 5)

    #Email text box on second window
    e = Entry(top, width= 50)
    e.grid(row= 4, column= 5)
    e.get()

    #Button for Email text box
    emailBtn = Button(top, text= "Enter Your Email", command= emailClick, bg= "purple", fg= "white")
    emailBtn.grid(row= 5, column= 5)

#Button on Home page for second window
btn = Button(window, text="More about the brand", command= open, bg="purple", fg="white")
btn.grid(row=0, column=9)

#Button to quit program
btn_quit = Button(window, text= "Exit", command= window.quit, bg= "red", fg= "white")
btn_quit.grid(row=9, column=10)

window.mainloop()