from tkinter import *
from tkinter import ttk

raiz = Tk() 
raiz.geometry("600x450")

#---------------Variables---------------
#Usuario
Fname = StringVar()
Lname = StringVar()
Country = StringVar()
#Bday
day = int()
mes = StringVar()
año = int()
#creditcard
card = int()
#Room
time=int()

#---------------Menu Bar---------------

notebook=ttk.Notebook(raiz)
notebook.configure(width=600, height=450)

addtab = ttk.Frame(notebook)
addtab.configure(width=100)
deltab = ttk.Frame(notebook)
deltab.configure(width=100)
searchtab = ttk.Frame(notebook)
searchtab.configure(width=100)
servtab = ttk.Frame(notebook)
servtab.config(width=100)
helptab = ttk.Frame(notebook)
helptab.config(width=100)


style=ttk.Style()
style.configure('TLabel', Font=("Arial",14))



ttk.Label(addtab).grid(column=0,row=0,padx=10,pady=10)
ttk.Label(deltab).grid(column=0,row=0,padx=10,pady=10)
ttk.Label(searchtab).grid(column=0,row=0,padx=10,pady=10)
ttk.Label(servtab).grid(column=0,row=0,padx=10,pady=10)
ttk.Label(helptab).grid(column=0,row=0,padx=10,pady=10)



notebook.add(addtab, text="       ADD        ")
notebook.add(deltab,text="        Delete        ")
notebook.add(searchtab,text="       Search        ")
notebook.add(servtab,text="       Services          ")
notebook.add(helptab,text="        Help          ")



style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook.Tab": {
        "configure": {"background": "skyblue1", "foreground": "black", "font": ("Arial", 14)},
        "map": {"background": [("selected", "Dodgerblue2")], "foreground": [("selected", "white")]}
    }
})
style.theme_use("MyStyle")


notebook.pack(expand=True, fill=BOTH)

#---------------Frame principal---------------
principal = ttk.Frame(addtab,padding="10 10 10 10")
principal.grid(column=0,row=0)


#---------------Frame Usuario---------------
usu=ttk.Frame(principal, padding="10 10 40 30", relief="groove")
usu.grid(column=0, row=0,sticky=(W))

Fname=ttk.Label(usu,text="First Name:",font="Italica").grid(column=0,row=0)
Fname=ttk.Entry(usu,textvariable=Fname).grid(column=1,row=0,columnspan=3)
Lname=ttk.Label(usu,text="Last Name:", font="Italica").grid(column=4,row=0)
Lname=ttk.Entry(usu,textvariable=Lname).grid(column=5,row=0)

#Bday
Bday=ttk.Label(usu,text="Birth Day",font="Italica").grid(column=0,row=3)
espacio=ttk.Label(usu,text="").grid(column=0,row=2)

dayBox=ttk.Combobox(usu,textvariable=day,width=5)
dayBox.grid(column=1,row=3,)
dayBox['values']= tuple(range(1,32))

mesbox=ttk.Combobox(usu,textvariable=mes,width=10)
mesbox.grid(column=2,row=3)
mesbox['values']=("January","February","March","April","May","June","July","August","September",
                    "Octuber","November","December")

añobox=ttk.Combobox(usu,textvariable=año,width=8)
añobox.grid(column=3,row=3)
añobox['values']=tuple(range(1500,2024))

#Contry
countrylabel=ttk.Label(usu,text="Country:",font="Italica").grid(column=4,row=3)
countryenty=ttk.Entry(usu,textvariable=Country).grid(column=5, row=3)

#---------------Frame Tarjeta---------------
card=ttk.Frame(principal, padding="10 10 185 10", relief="groove")
card.grid(column=0, row=1, sticky=(W))

creditlabel=ttk.Label(card,text="Credit Card(if any):", font="Italica").grid(column=0,row=0)
creditlabel=ttk.Entry(card,textvariable=card).grid(column=1,row=0)

typelabel=ttk.Label(card,text="Credit Type(if Any):",font="Italica").grid(column=0,row=2)
espacio=ttk.Label(card,text="").grid(column=0,row=1)

visa=ttk.Radiobutton(card, text="Visa").grid(column=1,row=2)
master=ttk.Radiobutton(card,text="MasterCard").grid(column=2,row=2)

#---------------Frame Room---------------
room=ttk.Frame(principal,padding="10 10 125 30", relief="groove")
room.grid(column=0,row=2,sticky=(W))

rtype=ttk.Label(room,text="Room Type:",font="Italica").grid(column=0,row=0)
normal=ttk.Radiobutton(room, text="Normal").grid(column=1,row=0,sticky=(W))
normal=ttk.Radiobutton(room, text="Familiar").grid(column=1,row=1,sticky=(W))
normal=ttk.Radiobutton(room, text="Special").grid(column=1,row=2,sticky=(W))

timelabel=ttk.Label(room,text="Total Staying Time (days):").grid(column=3,row=0,sticky=(E))
espacio=ttk.Label(room,text="").grid(column=2,row=0)
timeentry=ttk.Entry(room,textvariable=time).grid(column=4,row=0)

#---------------Frame Boton---------------
btn=ttk.Frame(principal,padding="10 10 10 10")
btn.grid(column=0,row=3)

btn=ttk.Button(btn,text="Submit").grid(column=2,row=2)

raiz.mainloop()