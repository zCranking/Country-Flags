from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.geometry("700x700")
root.title("Country Flags")
root.config(background="#21B1FF")

india = ImageTk.PhotoImage(Image.open("india.png"))
england = ImageTk.PhotoImage(Image.open("england.png"))
france = ImageTk.PhotoImage(Image.open("france.png"))
germany = ImageTk.PhotoImage(Image.open("germany.png"))
italy = ImageTk.PhotoImage(Image.open("italy.png"))
japan = ImageTk.PhotoImage(Image.open("japan.png"))
spain = ImageTk.PhotoImage(Image.open("spain.png"))
switzerland = ImageTk.PhotoImage(Image.open("switzerland.jpg"))
usa = ImageTk.PhotoImage(Image.open("usa.png"))

flags = {
    "india":india,
    "england":england,
    "france":france,
    "germany":germany,
    "italy":italy,
    "japan":japan,
    "spain":spain,
    "switzerland":switzerland,
    "usa":usa
}

flagInput = Entry(root, text="usa", background = "#47BFFF", foreground="#FF218C", font=("Comic Sans MS", "10", "bold"))
flagInput.place(relx=0.5, rely=0.4, anchor=CENTER)

displayFlag = Label(root, image=usa)
displayFlag.place(relx=0.5, rely=0.6, anchor=CENTER)

def find():
    Finput = flagInput.get()
    print(Finput)
    lowerF = Finput.lower()
    print(lowerF)
    try:
        theFlag = flags[lowerF]
        displayFlag['image'] = theFlag
    except:
        messagebox.showinfo("Error", "We don't have that country in our database.")
btn = Button(root, text="findImage", background = "#FFD800", foreground="#FF218C", font=("Comic Sans MS", "10", "bold"), command=find)
btn.place(relx=0.5, rely=0.8, anchor=CENTER)
root.mainloop()