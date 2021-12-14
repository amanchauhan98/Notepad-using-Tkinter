from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox as tsmg
import os


def submit():
    with open("notepad_feedback.txt","a") as f:
        f.write(str(feedback_text.get(1.0, END)))


def newfile():
    global File
    root.title("Untitled - Notepad")
    File = None
    textarea.delete(1.0, END)

def Open():
    File = None
    File = askopenfilename(defaultextension= ".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
    if File == "":
        File = None
    else:
        root.title(os.path.basename(File) + "- Notepad")
        textarea.delete(1.0, END)
        f = open(File,"r")
        textarea.insert(1.0,f.read())
        f.close()

    

def save():
    global File
    if File == None:
        File = asksaveasfilename(initialfile='Untitled.txt',defaultextension= ".txt" , filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])

        if File == "":

            File = None
        else:

            f = open(File, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(File)+ "- Notepad")
            print("save file")
    else :
        f = open(File,"w")
        f.write(textarea.get(1.0, END))
        f.close()        


         

def cut1():
    textarea.event_generate("<<Cut>>")

def copy1():
    textarea.event_generate("<<Copy>>")


def paste1():
    textarea.event_generate("<Paste>>")


def About():
    tsmg.showinfo("About", "This Notepad is created by aman chauhan")
def Feedback():
    askn =tsmg.askquestion("Feedback","Do you want to give your feedback?")
    if askn == "yes":
        root1 = Tk()
        root1.title("Feedback")
        global feedback_text
        feedback_text = Text(root1, height=3, width=30)
        feedback_text.pack(fill=BOTH)
        Button(root1, text="Submit", fg="green", command=submit).pack()
        tsmg.showinfo("Feedback - Submit", "Thanks for giving us a feedback")
    

    else :
        tsmg.showinfo("Feedback","OK! Enjoy the clone of notepad")



root = Tk()
root.title("Untitled - Notepad")
root.geometry("600x600")

textarea = Text(root, font= "lucida 15")
File = None
textarea.pack(fill=BOTH, expand= True)

menubar = Menu(root)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="File", command= newfile)
menu1.add_command(label="Open", command=Open)
menu1.add_command(label="Save", command=save)
menu1.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Cut", command= cut1)
menu2.add_command(label="Copy", command= copy1)
menu2.add_command(label="Paste", command= paste1)
menubar.add_cascade(label="Edit", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="About", command= About)
menu3.add_command(label="Feedback", command= Feedback)
menubar.add_cascade(label="Help", menu=menu3)
root.config(menu=menubar)


scroll  = Scrollbar(textarea)
scroll.pack(side= RIGHT, fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)




root.mainloop()
