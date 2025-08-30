import pickle
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from subprocess import call

class pharmasist_profile():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1919x1079+0+0")
        self.root.title("MEDICAL STORE MANAGEMENT SYSTEM ~ ABHIRUP RUDRA")
        bg_colour = "#16fad8"
        fg_colour = "#fa23ab"
        title = Label(self.root, text="DASHBOARD ~ PHARMASIST", bd=12, relief="groove", bg=bg_colour, fg="black", font=("times new roman", 35, "bold"), pady=2).pack(fill=X)

        #--------------------------VARIABLES--------------------------#
        
        file = open("userlogin.bin", "rb")
        lst = pickle.load(file)
        file.close()

        self.details = lst.split(',')

        file = open("userdata.bin", "rb")
        lst = pickle.load(file)
        file.close()

        userid = [i.split(',')[5] for i in lst]
        self.index = userid.index(self.details[5])

        self.name = StringVar()
        self.DOB = StringVar()
        self.mobile = StringVar()
        self.email = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.address = StringVar()

        #--------------------------LOGIN FRAME--------------------------#

        f1 = Frame(self.root, bd=12, relief="groove",  bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1, height=690)

        frame = Frame(f1, bg="white")
        frame.place(x=400, y=50, height=500, width=700)

        title2 = Label(frame, text="PROFILE", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title2.pack(fill=X)

        user_role_label = Label(frame, text="User Role", font=("arial", 15, "bold"), bg="white", fg="black")
        user_role_label.place(x=50, y=60)

        self.combo_box = Combobox(frame, values=["admin", "Pharmasist"])
        self.combo_box.place(x=50, y=100, width=280)
        self.combo_box.set("admin")

        name_label = Label(frame, text="Name", font=("arial", 15, "bold"), bg="white", fg="black")
        name_label.place(x=50, y=160)

        name_entry = Entry(frame, width=280, textvariable=self.name, font=("arial", 12), bd=5, relief="groove")
        name_entry.place(x=50, y=200, width=280)

        DOB_label = Label(frame, text="DOB (DATE OF BIRTH)", font=("arial", 15, "bold"), bg="white", fg="black")
        DOB_label.place(x=50, y=260)

        DOB_entry=DateEntry(frame,selectmode='day',textvariable=self.DOB)
        DOB_entry.place(x=50, y=300, width=280)

        mobile_label = Label(frame, text="Mobile Number", font=("arial", 15, "bold"), bg="white", fg="black")
        mobile_label.place(x=50, y=360)

        mobile_entry = Entry(frame, width=280, textvariable=self.mobile, font=("arial", 12), bd=5, relief="groove")
        mobile_entry.place(x=50, y=400, width=280)

        email_label = Label(frame, text="Email Address", font=("arial", 15, "bold"), bg="white", fg="black")
        email_label.place(x=350, y=60)

        email_entry = Entry(frame, width=280, textvariable=self.email, font=("arial", 12), bd=5, relief="groove")
        email_entry.place(x=350, y=100, width=280)

        username_label = Label(frame, text="Username", font=("arial", 15, "bold"), bg="white", fg="black")
        username_label.place(x=350, y=160)

        username_entry = Entry(frame, width=280, textvariable=self.username, font=("arial", 12), bd=5, relief="groove")
        username_entry.place(x=350, y=200, width=280)

        password_label = Label(frame, text="Password", font=("arial", 15, "bold"), bg="white", fg="black")
        password_label.place(x=350, y=260)

        password_entry = Entry(frame, width=280, textvariable=self.password, font=("arial", 12), bd=5, relief="groove")
        password_entry.place(x=350, y=300, width=280)

        address_label = Label(frame, text="Address", font=("arial", 15, "bold"), bg="white", fg="black")
        address_label.place(x=350, y=360)

        address_entry = Entry(frame, width=280, textvariable=self.address, font=("arial", 12), bd=5, relief="groove")
        address_entry.place(x=350, y=400, width=280)

        save_btn = Button(frame, text="SAVE", command=self.save, width=10, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        save_btn.place(x=230, y=450)

        exit_btn = Button(frame, text="EXIT", command=self.exit, width=10, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        exit_btn.place(x=350, y=450)

        self.name.set(self.details[0])
        self.combo_box.set(self.details[1])
        self.DOB.set(self.details[2])
        self.mobile.set(self.details[3])
        self.email.set(self.details[4])
        self.username.set(self.details[5])
        self.password.set(self.details[6])
        self.address.set(self.details[7])

    def save(self):
        try:
            file = open("userdata.bin", "rb")
            lst = pickle.load(file)
            file.close()

            userid = [i.split(',')[5] for i in lst]

            if self.username.get() in userid:
                mb.showerror("Invalid Username", "The username you entered is already in use pls try another.")
            else:
                del lst[self.index]

                new = str(self.name.get())+','+str(self.combo_box.get())+','+str(self.DOB.get())+','+str(self.mobile.get())+','+str(self.email.get())+','+str(self.username.get())+','+str(self.password.get())+','+str(self.address.get())

                lst.insert(self.index, new)

                file = open("userdata.bin", "wb")
                pickle.dump(lst, file, protocol=2)
                file.close()

                file = open("userlogin.bin", "wb")
                pickle.dump(new, file, protocol=2)
                file.close()

                print("Successfully Saved")
                mb.showinfo("Added Successfully", "Changes successfully saved")

        except:
            print("Some problem has been occured while saving the data. Please try later.")
            mb.showerror("ERROR", "Some problem  has occured while saving the file. Please try again later.")

    def exit(self):
        self.root.destroy()
        call(['python', 'dashboard_pharmasist.py'])


def main():
    root = Tk()
    obj = pharmasist_profile(root)
    root.mainloop()

main()