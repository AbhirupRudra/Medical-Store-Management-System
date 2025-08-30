import pickle
from tkinter import *
from tkinter import messagebox as mb
from subprocess import call

class update_medicine():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1919x1079+0+0")
        self.root.title("MEDICAL STORE MANAGEMENT SYSTEM ~ ABHIRUP RUDRA")
        bg_colour = "#16fad8"
        fg_colour = "#fa23ab"
        title = Label(self.root, text="DASHBOARD ~ PHARMASIST", bd=12, relief="groove", bg=bg_colour, fg="black", font=("times new roman", 35, "bold"), pady=2).pack(fill=X)

        #--------------------------VARIABLES--------------------------#

        self.medicine_id = StringVar()
        self.medicine_name = StringVar()
        self.company_name = StringVar()
        self.quantity = IntVar()
        self.price = IntVar()
        self.search_med_name = StringVar()
        self.index = -1

        #--------------------------ADD MEDICINE FRAME--------------------------#

        f1 = Frame(self.root, bd=12, relief="groove",  bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1, height=690)

        frame = Frame(f1, bg="white")
        frame.place(x=400, y=50, height=570, width=700)

        title2 = Label(frame, text="UPDATE MEDICINE", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title2.pack(fill=X)

        search_label = Entry(frame, width=25, textvariable=self.search_med_name, font=("arial", 15), bd=5, relief="groove")
        search_label.place(x=130, y=70)

        search_btn = Button(frame, text="SEARCH", command=self.search, width=8, bd=5, relief="groove", font=("arial", 10, "bold"), cursor="hand2")
        search_btn.place(x=450, y=71)

        medicine_id_label = Label(frame, text="Medicine ID", font=("arial", 15, "bold"), bg="white", fg="black")
        medicine_id_label.place(x=50, y=110)

        id_entry = Entry(frame, width=280, textvariable=self.medicine_id, font=("arial", 12), bd=5, relief="groove")
        id_entry.place(x=50, y=150, width=280)

        medicine_name_label = Label(frame, text="Medicine Name", font=("arial", 15, "bold"), bg="white", fg="black")
        medicine_name_label.place(x=50, y=210)

        name_entry = Entry(frame, width=280, textvariable=self.medicine_name, font=("arial", 12), bd=5, relief="groove")
        name_entry.place(x=50, y=250, width=280)

        compane_name_label = Label(frame, text="Company Name", font=("arial", 15, "bold"), bg="white", fg="black")
        compane_name_label.place(x=50, y=310)

        compane_name_entry = Entry(frame, width=280, textvariable=self.company_name, font=("arial", 12), bd=5, relief="groove")
        compane_name_entry.place(x=50, y=350, width=280)

        quantity_label = Label(frame, text="Quantity", font=("arial", 15, "bold"), bg="white", fg="black")
        quantity_label.place(x=50, y=410)

        quantity_entry = Entry(frame, width=280, textvariable=self.quantity, font=("arial", 12), bd=5, relief="groove")
        quantity_entry.place(x=50, y=450, width=280)

        price_label = Label(frame, text="Price Per Count", font=("arial", 15, "bold"), bg="white", fg="black")
        price_label.place(x=350, y=110)

        price_entry = Entry(frame, width=280, textvariable=self.price, font=("arial", 12), bd=5, relief="groove")
        price_entry.place(x=350, y=150, width=280)

        save_btn = Button(frame, text="SAVE", command=self.save, width=10, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        save_btn.place(x=230, y=510)

        exit_btn = Button(frame, text="EXIT", command=self.exit, width=10, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        exit_btn.place(x=350, y=510)


    def search(self):
        print(f"Search for medicine id {self.search_med_name.get()}")

        file = open("medicine.bin", "rb")
        medicine_raw = pickle.load(file)
        file.close()

        medicine_id = [i.split(",")[0] for i in medicine_raw]

        if self.search_med_name.get() in medicine_id:
            self.index = medicine_id.index(self.search_med_name.get())
            self.medicine_id.set(medicine_raw[self.index].split(",")[0])
            self.medicine_name.set(medicine_raw[self.index].split(",")[1])
            self.company_name.set(medicine_raw[self.index].split(",")[2])
            self.quantity.set(int(medicine_raw[self.index].split(",")[3]))
            self.price.set(int(medicine_raw[self.index].split(",")[4]))

        else:
            print("Not Found")
            self.medicine_id = StringVar()
            self.medicine_name = StringVar()
            self.company_name = StringVar()
            self.quantity = IntVar()
            self.price = IntVar()

    def save(self):
        try:
            file = open("medicine.bin", "rb")
            medicine_raw = pickle.load(file)
            file.close()

            medicine_id = [i.split(",")[0] for i in medicine_raw]\
            
            if self.medicine_id.get() != medicine_id[self.index] and self.medicine_id.get() in medicine_id:
                print("This medicine id is already in use. Try another.")
                mb.showerror("Invalid Medicine ID", "This medicine ID is already in use.\nIf you want to update the medicine, go to \"update medicine\" section.")

            else:
                del medicine_raw[self.index]

                new = str(self.medicine_id.get()) + "," + str(self.medicine_name.get()) + "," + str(self.company_name.get()) + "," + str(self.quantity.get()) + "," + str(self.price.get())

                medicine_raw.insert(self.index, new)

                file = open("medicine.bin", "wb")
                pickle.dump(medicine_raw, file, protocol=2)
                file.close()

                print("Saved Successfully")
                mb.showinfo("Saved Successfully", "Medicine successfully saved")
        
        except:
            print("Some problem has been occured while saving the data. Please try later.")
            mb.showerror("ERROR", "Some problem  has occured while saving the file. Please try again later.")

    def exit(self):
        print("exit")
        self.root.destroy()
        call(['python', 'dashboard_pharmasist.py'])



def main():
    root = Tk()
    obj = update_medicine(root)
    root.mainloop()

main()