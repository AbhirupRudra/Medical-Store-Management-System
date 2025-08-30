import pickle
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Treeview, Style
from subprocess import call

class view_users:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1919x1079+0+0")
        self.root.title("MEDICAL STORE MANAGEMENT SYSTEM ~ ABHIRUP RUDRA")
        bg_colour = "#16fad8"
        fg_colour = "#fa23ab"
        title = Label(self.root, text="DASHBOARD ~ ADMIN", bd=12, relief="groove", bg=bg_colour, fg="black", font=("times new roman", 35, "bold"), pady=2).pack(fill=X)

        #--------------------------VARIABLES--------------------------#

        file = open("userdata.bin", "rb")
        userdata_raw = pickle.load(file)
        file.close()

        #--------------------------VIEW USER FRAME--------------------------#

        f1 = Frame(self.root, bd=12, relief="groove",  bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1, height=690)

        frame = Frame(f1, bg="white")
        frame.place(x=400, y=50, height=500, width=700)

        tree_frame = Frame(frame, bg="white")
        tree_frame.place(y=50, x=0)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        title2 = Label(frame, text="VIEW USER", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title2.pack(fill=X)

        style = Style()
        style.theme_use('default')
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
        style.map("Treeview", background=[("selected", "#347083")])

        self.treeview = Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        self.treeview['columns'] = ('Name', 'Role', 'DOB', 'Mobno', 'email', 'uname', 'pass', 'address')
        self.treeview.column("#0", anchor=W, width=30)
        self.treeview.column("Name", anchor=W, width=120)
        self.treeview.column("Role", anchor=W, width=70)
        self.treeview.column("DOB", anchor=W, width=60)
        self.treeview.column("Mobno", anchor=W, width=70)
        self.treeview.column("email", anchor=W, width=120)
        self.treeview.column("uname", anchor=W, width=60)
        self.treeview.column("pass", anchor=W, width=60)
        self.treeview.column("address", anchor=W, width=70)

        self.treeview.heading("#0", text="SL.No.", anchor=CENTER)
        self.treeview.heading("Name", text="Name", anchor=W)
        self.treeview.heading("Role", text="Role", anchor=W)
        self.treeview.heading("DOB", text="Date Of Birth", anchor=W)
        self.treeview.heading("Mobno", text="Mobile", anchor=W)
        self.treeview.heading("email", text="Email", anchor=W)
        self.treeview.heading("uname", text="Username", anchor=W)
        self.treeview.heading("pass", text="Password", anchor=W)
        self.treeview.heading("address", text="Address", anchor=W)
        
        
        for i in range(len(userdata_raw)):
            userdata_values = userdata_raw[i]
            userdata_values = tuple(userdata_values.split(','))

            if i%2 == 0:
                self.treeview.insert(parent='', index="end", iid=i, text=str(i+1), values=userdata_values, tags=("evenrows"))
            else:
                self.treeview.insert(parent='', index="end", iid=i, text=str(i+1), values=userdata_values, tags=("oddrows"))

        self.treeview.pack(padx=10, pady=20, fill=Y)
        self.treeview.bind('<Double-1>', self.delete)

        tree_scroll.config(command=self.treeview.yview)

        self.treeview.tag_configure('oddrows', background="white")
        self.treeview.tag_configure('evenrows', background="lightblue")

        exit_btn = Button(frame, text="EXIT", command=self.exit, width=10, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        exit_btn.place(x=280, y=450)


    def delete(self, event):
        f = mb.askyesno("Delete?", "Do you want to delete the user??")
        if f:
            selected = self.treeview.selection()

            file = open("userdata.bin", "rb")
            userdata_raw = pickle.load(file)
            file.close()

            for i in selected:
                print(i)
                del userdata_raw[int(i)]
                self.treeview.delete(i)
                
            file = open("userdata.bin", "wb")
            pickle.dump(userdata_raw, file)
            file.close()

            print("Successfully deleted")
            mb.showinfo("Deleted Successfully", "Successfully deleted the user.")

            for i in self.treeview.get_children():
                self.treeview.delete(i)

            for i in range(len(userdata_raw)):
                userdata_values = userdata_raw[i]
                userdata_values = tuple(userdata_values.split(','))

                if i%2 == 0:
                    self.treeview.insert(parent='', index="end", iid=i, text=str(i+1), values=userdata_values, tags=("evenrows"))
                else:
                    self.treeview.insert(parent='', index="end", iid=i, text=str(i+1), values=userdata_values, tags=("oddrows"))

    def exit(self):
        self.root.destroy()
        call(['python', 'dashboard_admin.py'])



def main():
    root = Tk()
    obj = view_users(root)
    root.mainloop()

main()