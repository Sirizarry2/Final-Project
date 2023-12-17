import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

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
crystal1_pic = Image.open('C:/Users/Suzy/pythonProject/venv/RoseQuartz.jpg')
crystal2_pic = Image.open('C:/Users/Suzy/pythonProject/venv/TigersEye.jpg')
crystal3_pic = Image.open('C:/Users/Suzy/pythonProject/venv/Amethyst.jpg')

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
def myClick(): #Default button function to display text or get inputed data
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
def open(): #Function command to input in the first window button to open the second window
    #Second window setup
    top = Toplevel()
    top.title("Ordering Page")
    top.resizable(width=True, height=True)

    # Label widgets for second window
    greeting = Label(top, text= "Hi, my name is Kiki! Thank you for visting my site.")
    greeting.grid(row=0, column= 5)
    myLabel = Label(top, text= "You can place your order here.")
    myLabel.grid(row=1, column=5)

    # Image placement in second window
    global new_img
    top.iconbitmap('C:/Users/Suzy/pythonProject/venv/Kikiscrystals.ico')
    my_img = Image.open("C:/Users/Suzy/pythonProject/venv/Kikiscrystals.png")

    #Resizing the image on second window
    resized = my_img.resize((210, 100))

    #Placing brand logo on second window
    new_img = ImageTk.PhotoImage(resized)
    my_label = Label(top, image= new_img)
    my_label.grid(row=0, column=0)

    #Drop down menu button function to order crystals
    def show(): #Drop down menu function to create the menu and make the options
        orderOptions = Label(top, text= clicked.get())
        orderOptions.grid(row= 2, column= 5)

    #Drop down menu options
    options = [
        "Rose Quartz",
        "Tigers Eye",
        "Amethyst"
    ]

    #Creating the Drop Down Menu
    clicked = StringVar()
    clicked.set(options[0])

    drop = OptionMenu(top, clicked, *options)
    drop.grid(row= 3,column= 5)

    #Button for drop down menu in second window
    optionsBtn = Button(top, text= "Add to Cart", command=show, bg= "purple", fg= "white")
    optionsBtn.grid(row=3, column= 6)

    #Address text box on second window
    e = Entry(top, width= 70)
    e.grid(row= 5, column= 5)
    e.get()
    e.insert(0, "Address: ")

    #City text box
    e = Entry(top, width= 70)
    e.grid(row= 6, column= 5)
    e.get()
    e.insert(0, "City: ")

    #State text box
    e = Entry(top, width= 70)
    e.grid(row= 7, column= 5)
    e.get()
    e.insert(0, "State: ")

    #Zipcode text box
    e = Entry(top, width= 50)
    e.grid(row= 8, column= 5)
    e.get()
    e.insert(0, "Zipcode: ")

    #Function for email button command
    def infoPopup(): #message pop up box command to show the user that their information was receieved
        messagebox.askyesno("Information Recieved", "Your information was recieved. Would you like to place your order?")

    #Email text box on second window
    e = Entry(top, width= 50)
    e.grid(row= 9, column= 5)
    e.get()
    e.insert(0, "Email: ")

    #Button for all mailing info to be entered
    infoBtn = Button(top, text= "Enter", command= infoPopup, bg= "purple", fg= "white")
    infoBtn.grid(row= 10, column= 5)

    #Exit button on second window
    btn_quit = Button(top, text= "Exit", command= top.quit, bg= "red", fg= "white")
    btn_quit.grid(row= 12, column= 10)

#Button on Home page for second window
btn = Button(window, text="Click to make an order!", command= open, bg="purple", fg="white")
btn.grid(row=0, column=9)

#Button to quit program
btn_quit = Button(window, text= "Exit", command= window.quit, bg= "red", fg= "white")
btn_quit.grid(row=9, column=10)

window.mainloop()