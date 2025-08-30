import pickle
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Treeview, Style
from subprocess import call

class view_medicine:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1919x1079+0+0")
        self.root.title("MEDICAL STORE MANAGEMENT SYSTEM ~ ABHIRUP RUDRA")
        bg_colour = "#16fad8"
        fg_colour = "#fa23ab"
        title = Label(self.root, text="DASHBOARD ~ PHARMASIST", bd=12, relief="groove", bg=bg_colour, fg="black", font=("times new roman", 35, "bold"), pady=2).pack(fill=X)

        #--------------------------VARIABLES--------------------------#

        file = open("medicine.bin", "rb")
        medicine_raw = pickle.load(file)
        file.close()

        #--------------------------VIEW USER FRAME--------------------------#

        f1 = Frame(self.root, bd=12, relief="groove",  bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1, height=690)

        frame = Frame(f1, bg="white")
        frame.place(x=400, y=50, height=500, width=700)

        tree_frame = Frame(frame, bg="white")
        tree_frame.place(y=50, x=0, width=680)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        title2 = Label(frame, text="VIEW MEDICINES", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title2.pack(fill=X)

        style = Style()
        style.theme_use('default')
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
        style.map("Treeview", background=[("selected", "#347083")])

        self.treeview = Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        self.treeview['columns'] = ('MedID', 'Name', 'CompName', 'Quantity', 'Price')
        self.treeview.column("#0", anchor=W, width=50)
        self.treeview.column("MedID", anchor=W, width=100)
        self.treeview.column("Name", anchor=W, width=200)
        self.treeview.column("CompName", anchor=W, width=150)
        self.treeview.column("Quantity", anchor=W, width=70)
        self.treeview.column("Price", anchor=W, width=70)
        
        self.treeview.heading("#0", anchor=CENTER, text="Sl.No.")
        self.treeview.heading("MedID", anchor=W, text="Medicine ID")
        self.treeview.heading("Name", anchor=W, text="Name")
        self.treeview.heading("CompName", anchor=W, text="Company Name")
        self.treeview.heading("Quantity", anchor=W, text="Quantity")
        self.treeview.heading("Price", anchor=W, text="Price")

        for i in range(len(medicine_raw)):
            medicine_values = medicine_raw[i]
            medicine_values = tuple(medicine_values.split(','))

            if i%2 == 0:
                self.treeview.insert(parent='', index="end", iid=i, text=str(i+1), values=medicine_values, tags=("evenrows"))
            else:
                self.treeview.insert(parent='', index="end", iid=i, text=str(i+1), values=medicine_values, tags=("oddrows"))

        self.treeview.pack(padx=10, pady=20, fill=Y)
        self.treeview.bind('<Double-1>', self.delete)

        tree_scroll.config(command=self.treeview.yview)

        self.treeview.tag_configure('oddrows', background="white")
        self.treeview.tag_configure('evenrows', background="lightblue")

        exit_btn = Button(frame, text="EXIT", command=self.exit, width=10, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        exit_btn.place(x=280, y=450)

    def delete(self, event):
        f = mb.askyesno("Delete?", "Do you want to delete the medicine??")
        if f:
            selected = self.treeview.selection()

            file = open("medicine.bin", "rb")
            medicine_raw = pickle.load(file)
            file.close()

            for i in selected:
                del medicine_raw[int(i)]
                self.treeview.delete(i)
                
            file = open("medicine.bin", "wb")
            pickle.dump(medicine_raw, file)
            file.close()

            print("Successfully deleted")
            mb.showinfo("Deleted Successfully", "Successfully deleted the medicine.")

            for i in self.treeview.get_children():
                self.treeview.delete(i)

            for i in range(len(medicine_raw)):
                medicine_values = medicine_raw[i]
                medicine_values = tuple(medicine_values.split(','))

                if i%2 == 0:
                    self.treeview.insert(parent='', index="end", iid=i, text=str(i+1), values=medicine_values, tags=("evenrows"))
                else:
                    self.treeview.insert(parent='', index="end", iid=i, text=str(i+1), values=medicine_values, tags=("oddrows"))

    def exit(self):
        self.root.destroy()
        call(['python', 'dashboard_pharmasist.py'])




def main():
    root = Tk()
    obj = view_medicine(root)
    root.mainloop()

main()
