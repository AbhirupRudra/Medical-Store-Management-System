import pickle
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from subprocess import call

class add_user():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1919x1079+0+0")
        self.root.title("MEDICAL STORE MANAGEMENT SYSTEM ~ ABHIRUP RUDRA")
        bg_colour = "#16fad8"
        fg_colour = "#fa23ab"
        title = Label(self.root, text="DASHBOARD ~ ADMIN", bd=12, relief="groove", bg=bg_colour, fg="black", font=("times new roman", 35, "bold"), pady=2).pack(fill=X)

        #--------------------------VARIABLES--------------------------#
        
        self.name = StringVar()
        self.DOB = StringVar()
        self.mobile = IntVar()
        self.email = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.address = StringVar()
        self.searchusername = StringVar()
        self.id = IntVar()

        #--------------------------LOGIN FRAME--------------------------#

        f1 = Frame(self.root, bd=12, relief="groove",  bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1, height=690)

        frame = Frame(f1, bg="white")
        frame.place(x=400, y=50, height=550, width=700)

        title2 = Label(frame, text="UPDATE USER", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title2.pack(fill=X)

        search_label = Entry(frame, width=25, textvariable=self.searchusername, font=("arial", 15), bd=5, relief="groove")
        search_label.place(x=130, y=70)

        search_btn = Button(frame, text="SEARCH", command=self.search, width=8, bd=5, relief="groove", font=("arial", 10, "bold"), cursor="hand2")
        search_btn.place(x=450, y=71)

        user_role_label = Label(frame, text="User Role", font=("arial", 15, "bold"), bg="white", fg="black")
        user_role_label.place(x=50, y=110)

        self.combo_box = Combobox(frame, values=["admin", "Pharmasist"])
        self.combo_box.place(x=50, y=150, width=280)
        self.combo_box.set("admin")

        name_label = Label(frame, text="Name", font=("arial", 15, "bold"), bg="white", fg="black")
        name_label.place(x=50, y=210)

        name_entry = Entry(frame, width=280, textvariable=self.name, font=("arial", 12), bd=5, relief="groove")
        name_entry.place(x=50, y=250, width=280)

        DOB_label = Label(frame, text="DOB (DATE OF BIRTH)", font=("arial", 15, "bold"), bg="white", fg="black")
        DOB_label.place(x=50, y=310)

        self.DOB_entry=DateEntry(frame,selectmode='day',textvariable=self.DOB)
        self.DOB_entry.place(x=50, y=350, width=280)

        mobile_label = Label(frame, text="Mobile Number", font=("arial", 15, "bold"), bg="white", fg="black")
        mobile_label.place(x=50, y=410)

        mobile_entry = Entry(frame, width=280, textvariable=self.mobile, font=("arial", 12), bd=5, relief="groove")
        mobile_entry.place(x=50, y=450, width=280)

        email_label = Label(frame, text="Email Address", font=("arial", 15, "bold"), bg="white", fg="black")
        email_label.place(x=350, y=110)

        email_entry = Entry(frame, width=280, textvariable=self.email, font=("arial", 12), bd=5, relief="groove")
        email_entry.place(x=350, y=150, width=280)

        username_label = Label(frame, text="Username", font=("arial", 15, "bold"), bg="white", fg="black")
        username_label.place(x=350, y=210)

        username_entry = Entry(frame, width=280, textvariable=self.username, font=("arial", 12), bd=5, relief="groove")
        username_entry.place(x=350, y=250, width=280)

        password_label = Label(frame, text="Password", font=("arial", 15, "bold"), bg="white", fg="black")
        password_label.place(x=350, y=310)

        password_entry = Entry(frame, width=280, textvariable=self.password, font=("arial", 12), bd=5, relief="groove")
        password_entry.place(x=350, y=350, width=280)

        address_label = Label(frame, text="Address", font=("arial", 15, "bold"), bg="white", fg="black")
        address_label.place(x=350, y=410)

        address_entry = Entry(frame, width=280, textvariable=self.address, font=("arial", 12), bd=5, relief="groove")
        address_entry.place(x=350, y=450, width=280)

        save_btn = Button(frame, text="SAVE", command=self.save, width=10, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        save_btn.place(x=230, y=500)

        exit_btn = Button(frame, text="EXIT", command=self.exit, width=10, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        exit_btn.place(x=350, y=500)

    def search(self):
        print(f"search for name {self.searchusername.get()}")
        file = open("userdata.bin", "rb")
        userdata_raw = pickle.load(file)

        username = [i.split(',')[5] for i in userdata_raw]

        if self.searchusername.get() in username:
            self.id = username.index(self.searchusername.get())
            details = userdata_raw[self.id].split(',')
            self.name.set(details[0])
            self.combo_box.set(details[1])
            self.DOB.set(details[2])
            self.mobile.set(int(details[3]))
            self.email.set(details[4])
            self.username.set(details[5])
            self.password.set(details[6])
            self.address.set(details[7])
        
        else:
            print("Not Found")
            mb.showinfo("NOT FOUND", "The username you searched is not found.")
            self.name = StringVar()
            self.DOB = StringVar()
            self.mobile = IntVar()
            self.email = StringVar()
            self.username = StringVar()
            self.password = StringVar()
            self.address = StringVar()

    def save(self):
        try:
            file = open("userdata.bin", "rb")
            lst = pickle.load(file)
            file.close()       
            
            username = [i.split(',')[5] for i in lst]

            if self.combo_box.get() == "admin":
                print("You cannot change admins profile.\nIf you want to change your profile go to the \"PROFILE\" section.")
                mb.showerror("ERROR", "You cannot edit admin's profile.\nIf you want to change your profile go to the \"PROFILE\" section.")

            else:
                if self.username.get() != username[self.id] and self.username.get() in username:
                    print("This username is already in use. Try another.")
                    mb.showerror("Invalid Username", "The username you entered is already in use pls try another.")

                else:
                    del lst[self.id]

                    new = str(self.name.get())+','+str(self.combo_box.get())+','+str(self.DOB_entry.get_date().strftime("%d-%m-%Y"))+','+str(self.mobile.get())+','+str(self.email.get())+','+str(self.username.get())+','+str(self.password.get())+','+str(self.address.get())

                    lst.insert(self.id, new)

                    file = open("userdata.bin", "wb")
                    pickle.dump(lst, file, protocol=2)
                    file.close()

                    print("Successfully Saved")
                    mb.showinfo("Saved Successfully", "User successfully saved")

        except:
            print("Some problem has been occured while saving the data. Please try later.")
            mb.showerror("ERROR", "Some problem has occured while saving the file. Please try again later.")

    def exit(self):
        self.root.destroy()
        call(['python', 'dashboard_admin.py'])

def main():
    root = Tk()
    obj = add_user(root)
    root.mainloop()

main()