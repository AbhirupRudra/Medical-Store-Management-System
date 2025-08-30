import pickle
from tkinter import *
from tkinter import messagebox as mb
from subprocess import call

class add_medicine():
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

        #--------------------------ADD MEDICINE FRAME--------------------------#

        f1 = Frame(self.root, bd=12, relief="groove",  bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1, height=690)

        frame = Frame(f1, bg="white")
        frame.place(x=400, y=50, height=500, width=700)

        title2 = Label(frame, text="ADD MEDICINE", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title2.pack(fill=X)

        medicine_id_label = Label(frame, text="Medicine ID*", font=("arial", 15, "bold"), bg="white", fg="black")
        medicine_id_label.place(x=50, y=60)

        id_entry = Entry(frame, width=280, textvariable=self.medicine_id, font=("arial", 12), bd=5, relief="groove")
        id_entry.place(x=50, y=100, width=280)

        medicine_name_label = Label(frame, text="Medicine Name*", font=("arial", 15, "bold"), bg="white", fg="black")
        medicine_name_label.place(x=50, y=160)

        name_entry = Entry(frame, width=280, textvariable=self.medicine_name, font=("arial", 12), bd=5, relief="groove")
        name_entry.place(x=50, y=200, width=280)

        compane_name_label = Label(frame, text="Company Name*", font=("arial", 15, "bold"), bg="white", fg="black")
        compane_name_label.place(x=50, y=260)

        compane_name_entry = Entry(frame, width=280, textvariable=self.company_name, font=("arial", 12), bd=5, relief="groove")
        compane_name_entry.place(x=50, y=300, width=280)

        quantity_label = Label(frame, text="Quantity*", font=("arial", 15, "bold"), bg="white", fg="black")
        quantity_label.place(x=50, y=360)

        quantity_entry = Entry(frame, width=280, textvariable=self.quantity, font=("arial", 12), bd=5, relief="groove")
        quantity_entry.place(x=50, y=400, width=280)

        price_label = Label(frame, text="Price Per Count*", font=("arial", 15, "bold"), bg="white", fg="black")
        price_label.place(x=350, y=60)

        price_entry = Entry(frame, width=280, textvariable=self.price, font=("arial", 12), bd=5, relief="groove")
        price_entry.place(x=350, y=100, width=280)

        save_btn = Button(frame, text="SAVE", command=self.save, width=10, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        save_btn.place(x=230, y=450)

        exit_btn = Button(frame, text="EXIT", command=self.exit, width=10, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        exit_btn.place(x=350, y=450)

    def save(self):
        try:
            file = open("medicine.bin", "rb")
            medicine_raw = pickle.load(file)
            file.close()

            medicine_id = [i.split(",")[0] for i in medicine_raw]
            medicine_name = [i.split(",")[1] for i in medicine_raw]


            index = -1
            if self.medicine_id.get() in medicine_id:
                print("This id is already in use with other medicine.\nIf you want to update the medicine, go to update medicine section.")
                mb.showerror("Invalid Medicine ID", "This medicine ID is already in use.\nIf you want to update the medicine, go to \"update medicine\" section.")
                index = medicine_id.index(self.medicine_id.get())

            elif self.medicine_name.get() in medicine_name:
                print("This medicine is already present with other id.\nIf you want to update the medicine, go to update medicine section.")
                mb.showerror("Invalid Medicine Name", "This medicine is already present with other id.\nIf you want to update the medicine, go to \"update medicine\" section.")

            else:
                new = str(self.medicine_id.get()) + "," + str(self.medicine_name.get()) + "," + str(self.company_name.get()) + "," + str(self.quantity.get()) + "," + str(self.price.get())

                medicine_raw.append(new)

                file = open("medicine.bin", "wb")
                pickle.dump(medicine_raw, file, protocol=2)
                file.close()

                print("Saved Successfully")
                mb.showinfo("Added Successfully", "Medicine successfully added")
        except:
            print("Some problem has been occured while saving the data. Please try later.")
            mb.showerror("ERROR", "Some problem has occured while saving the file. Please try again later.")

    def exit(self):
        print("exit")
        self.root.destroy()
        call(['python', 'dashboard_pharmasist.py'])

def main():
    root = Tk()
    obj = add_medicine(root)
    root.mainloop()

main()