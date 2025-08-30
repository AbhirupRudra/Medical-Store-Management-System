import pickle
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Treeview, Style
from subprocess import call
import os

class view_bills:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1919x1079+0+0")
        self.root.title("MEDICAL STORE MANAGEMENT SYSTEM ~ ABHIRUP RUDRA")
        bg_colour = "#16fad8"
        fg_colour = "#fa23ab"
        title = Label(self.root, text="DASHBOARD ~ PHARMASIST", bd=12, relief="groove", bg=bg_colour, fg="black", font=("times new roman", 35, "bold"), pady=2).pack(fill=X)

        #--------------------------VARIABLES--------------------------#

        self.search_name = StringVar()

        #--------------------------VIEW USER FRAME--------------------------#

        f1 = Frame(self.root, bd=12, relief="groove",  bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1, height=690)

        frame = Frame(f1, bg="white")
        frame.place(x=400, y=50, height=500, width=700)

        tree_frame = Frame(frame, bg="white")
        tree_frame.place(y=120, x=0, width=680)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        title2 = Label(frame, text="VIEW BILLS", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title2.pack(fill=X, pady=10)

        search_entry = Entry(frame, width=30, textvariable=self.search_name, font=("arial", 12), bd=5, relief="groove")
        search_entry.place(x=200, y=80)
        search_entry.bind("<Key>", self.search)

        style = Style()
        style.theme_use('default')
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
        style.map("Treeview", background=[("selected", "#347083")])

        self.treeview = Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        self.treeview['columns'] = ('date', 'time', 'Name', 'mobno', 'totprice')
        self.treeview.column("#0", anchor=W, width=50)
        self.treeview.column("date", anchor=W, width=80)
        self.treeview.column("time", anchor=W, width=80)
        self.treeview.column("Name", anchor=W, width=200)
        self.treeview.column("mobno", anchor=W, width=130)
        self.treeview.column("totprice", anchor=W, width=70)
        
        self.treeview.heading("#0", anchor=CENTER, text="Sl.No.")
        self.treeview.heading("date", anchor=W, text="Date")
        self.treeview.heading("time", anchor=W, text="Time")
        self.treeview.heading("Name", anchor=W, text="Name")
        self.treeview.heading("mobno", anchor=W, text="Mobile No.")
        self.treeview.heading("totprice", anchor=W, text="Price")

        count = 0
        for i in os.listdir("bills/"):
            file = open(f"bills/{i}", "r")
            raw = file.readlines()
            values = (raw[1].split()[2], raw[1].split()[3], raw[3][17:-1], raw[4][17:-1], raw[-1].split()[-1])
            if count%2 == 0:
                self.treeview.insert(parent='', index="end", iid=count, text=str(count+1), values=values, tags=("evenrows"))
            else:
                self.treeview.insert(parent='', index="end", iid=count, text=str(count+1), values=values, tags=("oddrows"))
            count+=1

        self.treeview.pack(padx=10, pady=20, fill=Y)
        self.treeview.bind("<Double-1>", self.open_file)

        tree_scroll.config(command=self.treeview.yview)

        self.treeview.tag_configure('oddrows', background="white")
        self.treeview.tag_configure('evenrows', background="lightblue")

        exit_btn = Button(frame, text="EXIT", command=self.exit, width=10, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        exit_btn.place(x=280, y=450)

    def search(self, event):
        names = []
        contents = []
        for i in os.listdir("bills/"):
            file = open(f"bills/{i}", "r")
            raw = file.readlines()
            contents.append(tuple(raw))
            names.append(raw[3][17:-2].lower())

        for i in self.treeview.get_children():
            self.treeview.delete(i)
        
        for i in range(len(names)):
            if names[i].startswith(self.search_name.get().lower()):
                values = (contents[i][1].split()[2], contents[i][1].split()[3], contents[i][3][17:-1], contents[i][4][17:-1], contents[i][-1].split()[-1])

                if i%2 == 0:
                    self.treeview.insert(parent='', index="end", iid=i, text=str(i+1), values=values, tags=("evenrows"))
                else:
                    self.treeview.insert(parent='', index="end", iid=i, text=str(i+1), values=values, tags=("oddrows"))

        print(f"Search for name {self.search_name.get()}")

    def open_file(self, event):
        print(self.treeview.selection()[0])

        c = 0
        for i in os.listdir("bills/"):
            if c == int(self.treeview.selection()[0]):
                file = "notepad.exe" + " bills\\" + i
                os.system(file)
            c+=1

    def exit(self):
        self.root.destroy()
        call(['python', 'dashboard_pharmasist.py'])


def main():
    root = Tk()
    obj = view_bills(root)
    root.mainloop()

main()
