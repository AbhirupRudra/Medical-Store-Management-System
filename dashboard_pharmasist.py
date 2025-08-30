import pickle
from tkinter import *
from tkinter import messagebox as mb
from subprocess import call
import sys


class dashboard_medicine():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1919x1079+0+0")
        self.root.title("MEDICAL STORE MANAGEMENT SYSTEM ~ ABHIRUP RUDRA")
        bg_colour = "#16fad8"
        fg_colour = "#fa23ab"
        title = Label(self.root, text="DASHBOARD ~ PHARMASIST", bd=12, relief="groove", bg=bg_colour, fg="black", font=("times new roman", 35, "bold"), pady=2).pack(fill=X)

        #--------------------------VARIABLES--------------------------#

        #--------------------------DASHBOARD AREA--------------------------#
        f1 = Frame(self.root, bd=12, relief="groove",  bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1, height=690)

        add_medicine_btn = Button(f1, text="ADD MEDICINE", command=self.add_medicine, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        add_medicine_btn.place(x=400, y=100, height=100, width=300)

        view_medicine_btn = Button(f1, text="VIEW MEDICINE", command=self.view_medicine, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        view_medicine_btn.place(x=400, y=230, height=100, width=300)

        update_medicine_btn = Button(f1, text="UPDATE MEDICINE", command=self.update_medicine, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        update_medicine_btn.place(x=400, y=360, height=100, width=300)

        sell_medicine_btn = Button(f1, text="SELL MEDICINE", command=self.sell_medicine, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        sell_medicine_btn.place(x=730, y=100, height=100, width=300)

        view_bills_btn = Button(f1, text="VIEW BILLS", command=self.view_bills, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        view_bills_btn.place(x=730, y=230, height=100, width=300)

        profile_btn = Button(f1, text="PROFILE", command=self.profile, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        profile_btn.place(x=730, y=360, height=100, width=300)

        logout_btn = Button(f1, text="LOGOUT", command=self.logout, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        logout_btn.place(x=550, y=490, height=100, width=300)


    def add_medicine(self):
        print("add user")
        self.root.destroy()
        call(['python', 'add_medicine.py'])

    def view_medicine(self):
        print("view user")
        self.root.destroy()
        call(['python', 'view_medicine.py'])

    def update_medicine(self):
        print("update user")
        self.root.destroy()
        call(['python', 'update_medicine.py'])

    def sell_medicine(self):
        print("sell medicine")
        self.root.destroy()
        call(['python', 'sell_medicine.py'])

    def view_bills(self):
        print("view bills")
        self.root.destroy()
        call(['python', 'view_bills.py'])
        
    def profile(self):
        print("profile")
        self.root.destroy()
        call(['python', 'pharmasist_profile.py'])

    def logout(self):
        print("Logout")
        file = open("userlogin.bin", "wb")
        pickle.dump("", file, protocol=2)
        file.close()
        self.root.destroy()
        call(['python', 'login_window.py'])
        

def main():
    root = Tk()
    obj = dashboard_medicine(root)
    root.mainloop()

main()