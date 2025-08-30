import pickle
from tkinter import *
from tkinter import messagebox as mb
from subprocess import call

class login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1919x1079+0+0")
        self.root.title("MEDICAL STORE MANAGEMENT SYSTEM ~ ABHIRUP RUDRA")
        bg_colour = "#16fad8"
        fg_colour = "#fa23ab"
        title = Label(self.root, text="MEDICAL STORE MANAGEMENT SYSTEM", bd=12, relief="groove", bg=bg_colour, fg="black", font=("times new roman", 35, "bold"), pady=2).pack(fill=X)

        #--------------------------VARIABLES--------------------------#

        self.username = StringVar()
        self.password = StringVar()
        self.id = IntVar()

        #--------------------------LOGIN FRAME--------------------------#

        f1 = LabelFrame(self.root, text="LOGIN AREA", font=("times new roman", 30, "bold"), bd=12, relief="groove", fg="black",  bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1, height=690)

        username_label = Label(f1, text="USERNAME", bg=bg_colour, font = ("times new roman", 24, "bold"), padx=10, pady=10)
        username_label.place(x=200, y=100)

        username_entry = Entry(f1, width=40, textvariable=self.username, font=("arial", 19), bd=7, relief="sunken")
        username_entry.place(x=500, y=110)

        password_label = Label(f1, text="PASSWORD", bg=bg_colour, font = ("times new roman", 24, "bold"), padx=10, pady=10)
        password_label.place(x=200, y=200)

        password_entry = Entry(f1, width=40, textvariable=self.password, font=("arial", 19), bd=7, relief="sunken")
        password_entry.place(x=500, y=210)
        password_entry.bind("<Return>", self.submit_login)

        submit_btn = Button(f1, text="SUBMIT", command=lambda: self.submit_login(None), width=10, bd=7, relief="groove", font=("arial", 17, "bold"), cursor="hand2")
        submit_btn.place(x=600, y=400)
        
    #--------------------------FUNCTIONS--------------------------#

    def submit_login(self, e):
        try:
            file = open("userdata.bin", "rb")
            user_pass = pickle.load(file)
            file.close()

            username = [i.split(",")[5] for i in user_pass]

            if self.username.get() in username:
                self.id = username.index(self.username.get())

                if user_pass[self.id].split(',')[1] == "admin" and self.password.get() == user_pass[self.id].split(',')[6]:
                    print("Successful Login as admin")
                    self.root.destroy()
                    with open("adminlogin.bin", "wb") as file:
                        pickle.dump(str(self.username.get()), file, protocol=2)
                    call(['python', 'dashboard_admin.py'])

                elif self.password.get() == user_pass[self.id].split(',')[6]:
                    print("Login successful")
                    with open("userlogin.bin", "wb") as file:
                        pickle.dump(user_pass[self.id], file)
                    self.root.destroy()
                    call(['python', 'dashboard_pharmasist.py'])
            
                else:
                    print("Either password or username is incorrect")
                    mb.showerror("Username or Password Wrong", "The Username or Password you have entered is wrong.\nTry again.")

            else:
                print("Either password or username is incorrect")
                mb.showerror("Username or Password Wrong", "The Username or Password you have entered is wrong.\nTry again.")

        except:
            print("Login informations (files) are missing. Pls contact the software owner")
            mb.showerror("Login Files Missing", "Some files required for login is missing. Please contact the owner.")


def main():
    root = Tk()
    obj = login_Window(root)
    root.mainloop()

main()