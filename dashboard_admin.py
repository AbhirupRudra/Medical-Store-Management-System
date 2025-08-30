import pickle
from tkinter import *
from tkinter import messagebox as mb
from subprocess import call
import sys


class dashboard_admin():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1919x1079+0+0")
        self.root.title("MEDICAL STORE MANAGEMENT SYSTEM ~ ABHIRUP RUDRA")
        bg_colour = "#16fad8"
        fg_colour = "#fa23ab"
        title = Label(self.root, text="DASHBOARD ~ ADMIN", bd=12, relief="groove", bg=bg_colour, fg="black", font=("times new roman", 35, "bold"), pady=2).pack(fill=X)

        #--------------------------VARIABLES--------------------------#

        #--------------------------DASHBOARD AREA--------------------------#
        f1 = Frame(self.root, bd=12, relief="groove",  bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1, height=690)

        add_user_btn = Button(f1, text="ADD USER", command=self.add_user, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        add_user_btn.place(x=400, y=100, height=100, width=300)

        view_user_btn = Button(f1, text="VIEW USER", command=self.view_user, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        view_user_btn.place(x=400, y=230, height=100, width=300)

        update_user_btn = Button(f1, text="UPDATE USER", command=self.update_user, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        update_user_btn.place(x=400, y=360, height=100, width=300)

        profile_btn = Button(f1, text="PROFILE", command=self.profile, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        profile_btn.place(x=730, y=100, height=100, width=300)

        logout_btn = Button(f1, text="LOGOUT", command=self.logout, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        logout_btn.place(x=730, y=230, height=100, width=300)

        exit_btn = Button(f1, text="EXIT", command=self.exit, bd=12, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        exit_btn.place(x=730, y=360, height=100, width=300)


    def add_user(self):
        print("add user")
        self.root.destroy()
        call(['python', 'add_user.py'])

    def view_user(self):
        print("view user")
        self.root.destroy()
        call(['python', 'view_users.py'])

    def update_user(self):
        print("update user")
        self.root.destroy()
        call(['python', 'update_user.py'])

    def profile(self):
        print("profile")
        self.root.destroy()
        call(['python', 'admin_profile.py'])

    def logout(self):
        print("logout")
        self.root.destroy()
        with open("adminlogin.bin", "wb") as file:
            pickle.dump("", file, protocol=2)
        call(['python', 'login_window.py'])

    def exit(self):
        print("exit")
        with open("adminlogin.bin", "wb") as file:
            pickle.dump("", file, protocol=2)
        sys.exit()
        
        

def main():
    root = Tk()
    obj = dashboard_admin(root)
    root.mainloop()

main()