from tkinter import *
from notifypy import Notify
from tkinter import filedialog as FileDialog
from io import open

notify = Notify()
root = Tk()
root.title("Text Editor")
r = "" #saved file 

#FUNCTIONS
def new():
    global r
    r = ""
    text.delete(1.0,END)
    notify.title = "Text Editor"
    notify.message = "a file has been created successfully"
    notify.send()

def openfile():
    global r
    r = FileDialog.askopenfilename(
        initialdir='.',
        filetype=(("Fichero de texto", "*.txt"),),
        title="Open File")
    if r != "":
        file = open(r,'r')
        content = file.read()
        text.delete(1.0,'end')
        text.insert('insert',content)
        file.close()
        root.title(r + " / Text Editor")
        notify.title = "Text Editor"
        notify.message = "The file has been opened correctly"
        notify.send()

def save():
    if r != "":
        content = text.get(1.0,'end-1c')
        file = open(r,'w+')
        file.write(content)
        file.close()
        notify.title = "Text Editor"
        notify.message = "Saved successfully"
        notify.send()
    else:
        savas()

def savas():
    global r
    file = FileDialog.asksaveasfile(title = "Save file", mode="w", defaultextension=".txt")
    if file is not None:
        r = file.name
        content = text.get(1.0,'end-1c')
        file = open(r,'w+')
        file.write(content)
        file.close()
        notify.title = "Text Editor"
        notify.message = f"File saved as {r}"
        notify.send()
    else:
        notify.title = "Text Editor"
        notify.message = "Canceled process"
        notify.send()

#MAIN
barmenu = Menu(root)
fmenu = Menu(barmenu,tearoff=0)
fmenu.add_command(label="New",command=new)
fmenu.add_command(label="Open",command=openfile)
fmenu.add_command(label="Save",command=save)
fmenu.add_command(label="Save as",command=savas)
fmenu.add_separator()
fmenu.add_command(label="Exit",command=root.quit)
barmenu.add_cascade(menu=fmenu,label="Archive")
#BOX
text = Text(root)
text.pack(fill="both",expand=1)
text.config(bd=0,padx=6,pady=4,font=("Consolas",12))

menssage = StringVar()
menssage.set("By Santiago Abuawad")
monitor = Label(root,textvar=menssage,justify='left')
monitor.pack(side='left')

root.config(menu=barmenu)
root.mainloop()

#github @santiago-abuawad