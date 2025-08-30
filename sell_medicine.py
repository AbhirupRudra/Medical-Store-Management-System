import pickle
import tempfile
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Treeview, Style
from subprocess import call
from datetime import datetime
import os
from plyer import notification

class sell_medicine:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1919x1079+0+0")
        self.root.title("MEDICAL STORE MANAGEMENT SYSTEM ~ ABHIRUP RUDRA")
        bg_colour = "#16fad8"
        fg_colour = "#fa23ab"
        title = Label(self.root, text="DASHBOARD ~ PHARMASIST", bd=12, relief="groove", bg=bg_colour, fg="black", font=("times new roman", 35, "bold"), pady=2).pack(fill=X)

        #--------------------------VARIABLES--------------------------#

        self.search_med_name = StringVar()
        self.medicine_id = StringVar()
        self.medicine_name = StringVar()
        self.comp_name = StringVar()
        self.ppm = IntVar()
        self.qty = IntVar()
        self.count = 0
        self.index = -1

        self.mob_num = IntVar()
        self.name = StringVar()
        self.dr_name = StringVar()
        self.num = 0
        self.file_name = StringVar()
        self.total = 0
        self.tot = IntVar()

        #--------------------------VIEW USER FRAME--------------------------#

        f1 = Frame(self.root, bd=12, relief="groove",  bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1, height=690)

        search_entry = Entry(f1, width=31, textvariable=self.search_med_name, font=("arial", 15), bd=5, relief="groove")
        search_entry.place(x=30, y=10)
        search_entry.bind("<Key>", self.search)

        tree_frame1 = Frame(f1, bg="white")
        tree_frame1.place(x=30, y=70, height=550, width=350)
        
        tree_frame2 = Frame(f1, bg="white")
        tree_frame2.place(x=400, y=330, height=250, width=570)

        tree_scroll1 = Scrollbar(tree_frame1)
        tree_scroll1.pack(side=RIGHT, fill=Y)

        tree_scroll2 = Scrollbar(tree_frame2)
        tree_scroll2.pack(side=RIGHT, fill=Y)

        style = Style()
        style.theme_use('default')
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
        style.map("Treeview", background=[("selected", "#347083")])

        self.treeview1 = Treeview(tree_frame1, yscrollcommand=tree_scroll1.set, selectmode="browse", height=510)
        self.treeview1.pack(fill=Y)
        self.treeview1.bind("<Double-1>", self.select_med)

        self.treeview2 = Treeview(tree_frame2, yscrollcommand=tree_scroll2.set, selectmode="extended")
        self.treeview2.pack(fill=Y)
        self.treeview2.bind("<Double-1>", self.delete)

        self.treeview1['columns'] = ('medname', 'qty')

        self.treeview1.column("#0", anchor=W, width=90)
        self.treeview1.column("medname", anchor=W, width=160)
        self.treeview1.column("qty", anchor=W, width=80)

        self.treeview1.heading("#0", text="Med ID", anchor=CENTER)
        self.treeview1.heading("medname", text="Mediciine Name", anchor=W)
        self.treeview1.heading("qty", text="Quantity", anchor=W)
        
        tree_scroll1.config(command=self.treeview1.yview)

        self.treeview1.tag_configure('oddrows', background="white")
        self.treeview1.tag_configure('evenrows', background="lightblue")

        med_id_label = Label(f1, text="Medicine ID", font=("arial", 15, "bold"), bg=bg_colour, fg="black")
        med_id_label.place(x=400, y=50)

        med_id_entry = Entry(f1, width=30, textvariable=self.medicine_id, font=("arial", 12), bd=5, relief="groove", state="disabled", disabledbackground="white", disabledforeground="black")
        med_id_entry.place(x=400, y=90)

        med_name_label = Label(f1, text="Medicine Name", font=("arial", 15, "bold"), bg=bg_colour, fg="black")
        med_name_label.place(x=400, y=140)

        med_name_entry = Entry(f1, width=30, textvariable=self.medicine_name, font=("arial", 12), bd=5, relief="groove", state="disabled", disabledbackground="white", disabledforeground="black")
        med_name_entry.place(x=400, y=180)

        comp_name_label = Label(f1, text="Company Name", font=("arial", 15, "bold"), bg=bg_colour, fg="black")
        comp_name_label.place(x=400, y=230)

        comp_name_entry = Entry(f1, width=30, textvariable=self.comp_name, font=("arial", 12), bd=5, relief="groove", state="disabled", disabledbackground="white", disabledforeground="black")
        comp_name_entry.place(x=400, y=270)

        price_per_med_label = Label(f1, text="Price Per Medicine", font=("arial", 15, "bold"), bg=bg_colour, fg="black")
        price_per_med_label.place(x=700, y=50)

        price_per_med_entry = Entry(f1, width=30, textvariable=self.ppm, font=("arial", 12), bd=5, relief="groove", state="disabled", disabledbackground="white", disabledforeground="black")
        price_per_med_entry.place(x=700, y=90)

        quantity_label = Label(f1, text="Quantity Required", font=("arial", 15, "bold"), bg=bg_colour, fg="black")
        quantity_label.place(x=700, y=140)

        quantity_entry = Entry(f1, width=30, textvariable=self.qty, font=("arial", 12), bd=5, relief="groove")
        quantity_entry.place(x=700, y=180)

        add_cart_btn = Button(f1, text="ADD TO CART", command=self.add_to_cart, width=15, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        add_cart_btn.place(x=750, y=265)

        self.treeview2['columns'] = ("name", "ppu", "units", "totprice")

        self.treeview2.column("#0", anchor=CENTER, width=50)
        self.treeview2.column("name", anchor=W, width=180)
        self.treeview2.column("ppu", anchor=W, width=100)
        self.treeview2.column("units", anchor=W, width=90)
        self.treeview2.column("totprice", anchor=W, width=130)

        self.treeview2.heading("#0", text="SL.No.", anchor=CENTER)
        self.treeview2.heading("name", text="Medicine Name", anchor=W)
        self.treeview2.heading("ppu", text="Price Per Unit", anchor=W)
        self.treeview2.heading("units", text="No. of Units", anchor=W)
        self.treeview2.heading("totprice", text="Total Price", anchor=W)

        tree_scroll2.config(command=self.treeview2.yview)

        self.treeview2.tag_configure('oddrows', background="white")
        self.treeview2.tag_configure('evenrows', background="lightblue")

        total_price_label = Label(f1, text="TOTAL PRICE", font=("arial", 15, "bold"), bg=bg_colour, fg="black")
        total_price_label.place(x=520, y=600)

        total_price_entry = Entry(f1, width=20, textvariable=self.tot, font=("arial", 12), bd=5, relief="groove", state="disabled", disabledbackground="white", disabledforeground="black")
        total_price_entry.place(x=700, y=600)

        profile_frame = Frame(f1, bg=bg_colour)
        profile_frame.place(x=1050, y=20, height=620, width=400)

        title2 = Label(profile_frame, text="PROFILE", font=("times new roman", 30, "bold"), bg=bg_colour, fg="black")
        title2.pack(fill=X)

        mob_num_label = Label(profile_frame, text="Mobile Number*", font=("times new roman", 15, "bold"), bg=bg_colour, fg="black")
        mob_num_label.place(x=10, y=70)

        mob_num_entry = Entry(profile_frame, width=30, textvariable=self.mob_num, font=("arial", 12), bd=5, relief="groove")
        mob_num_entry.place(x=10, y=100)

        name_label = Label(profile_frame, text="Name*", font=("times new roman", 15, "bold"), bg=bg_colour, fg="black")
        name_label.place(x=10, y=150)

        name_entry = Entry(profile_frame, width=30, textvariable=self.name, font=("arial", 12), bd=5, relief="groove")
        name_entry.place(x=10, y=180)

        dr_name_label = Label(profile_frame, text="Doctor Name*", font=("times new roman", 15, "bold"), bg=bg_colour, fg="black")
        dr_name_label.place(x=10, y=230)

        dr_name_entry = Entry(profile_frame, width=30, textvariable=self.dr_name, font=("arial", 12), bd=5, relief="groove")
        dr_name_entry.place(x=10, y=260)

        self.create_bill_btn = Button(profile_frame, text="CREATE\nBILL", command=self.create_bill, width=20, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        self.create_bill_btn.place(x=10, y=350, height=100, width=100)

        print_bill_btn = Button(profile_frame, text="PRINT\nBILL", command=self.print_bill, width=20, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        print_bill_btn.place(x=150, y=350, height=100, width=100)

        clear_all_btn = Button(profile_frame, text="CLEAR\nALL", command=self.clear_all, width=20, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        clear_all_btn.place(x=10, y=470, height=100, width=100)

        exit_btn = Button(profile_frame, text="EXIT", command=self.logout, width=20, bd=7, relief="groove", font=("arial", 12, "bold"), cursor="hand2")
        exit_btn.place(x=150, y=470, height=100, width=100)

    def search(self, event):
        file = open("medicine.bin", "rb")
        medicine_raw = pickle.load(file)
        file.close()

        for i in self.treeview1.get_children():
            self.treeview1.delete(i)

        for i in range(len(medicine_raw)):
            medicine_values = medicine_raw[i]

            if medicine_values.split(',')[1].lower().startswith(self.search_med_name.get()):
                medicine = (medicine_values.split(',')[1], medicine_values.split(',')[3])

                if i%2 == 0:
                    self.treeview1.insert(parent='', index="end", iid=i, text=medicine_values.split(',')[0], values=medicine, tags=("evenrows"))
                else:
                    self.treeview1.insert(parent='', index="end", iid=i, text=medicine_values.split(',')[0], values=medicine, tags=("oddrows"))

    def select_med(self, event):
        file = open("medicine.bin", "rb")
        medicine_raw = pickle.load(file)
        file.close()

        selected = self.treeview1.focus()
        details = self.treeview1.item(selected)["text"]
        print(details)

        medicine_id = [i.split(',')[0] for i in medicine_raw]

        self.index = medicine_id.index(details)

        self.medicine_id.set(medicine_raw[self.index].split(',')[0])
        self.medicine_name.set(medicine_raw[self.index].split(',')[1])
        self.comp_name.set(medicine_raw[self.index].split(',')[2])
        self.ppm.set(medicine_raw[self.index].split(',')[4])
        self.qty.set(0)

    def add_to_cart(self):
        file = open("medicine.bin", "rb")
        medicine_raw = pickle.load(file)
        file.close()

        booked_names = []
        for i in self.treeview2.get_children():
            booked_names.append(self.treeview2.item(i)["values"][0])

        if self.index != -1 :
            medicine_values = medicine_raw[self.index].split(',')
            if medicine_values[1] in booked_names:
                print("This medicine is already included in the bill. If you want to alter first delete the name from below by double clicking on it.")
                mb.showerror("Invalid medicine", "This medicine is already in cart.\nIf you want to alter first delete the name from below by double clicking on it.")

            else:
                if self.qty.get() > 0:
                    if self.qty.get() > int(medicine_values[3]):
                        print("Not in stock")
                        mb.showerror("Not in Stock", "The amount entered is not in stock.")

                    else:
                        values = (medicine_values[1], medicine_values[4], self.qty.get(), str(int(self.qty.get())*int(medicine_values[4])))

                        self.total+=int(self.qty.get())*int(medicine_values[4])
                        self.tot.set(self.total)

                        if self.count%2 == 0:
                            self.treeview2.insert(parent='', index="end", iid=self.count, text=str(self.count+1), values=values, tags=("evenrows"))
                        else:
                            self.treeview2.insert(parent='', index="end", iid=self.count, text=str(self.count+1), values=values, tags=("oddrows"))
                        self.count+=1
                        print("Added to cart")

                        medicine_values = str(medicine_values[0]) + "," + str(medicine_values[1]) + "," + str(medicine_values[2]) + "," + str(int(medicine_values[3])-self.qty.get()) + "," + str(medicine_values[4])

                        file = open("medicine.bin", "wb")

                        del medicine_raw[self.index]

                        medicine_raw.insert(self.index, medicine_values)

                        pickle.dump(medicine_raw, file, protocol=2)
                else:
                    print("Enter no. of units required.")
                    mb.showerror("Enter Quantity", "Enter the quantity of units required.")
        else:
            print("Search and select medicine first.")
            mb.showerror("Medicine not selected", "Search and Select the medicine fiest.")

    def delete(self, event):
        selected = self.treeview2.selection()

        file = open("medicine.bin", "rb")
        medicine_raw = pickle.load(file)
        file.close()

        med_name = [i.split(",")[1] for i in medicine_raw]

        file = open("medicine.bin", "wb")

        for i in selected:
            values = medicine_raw[med_name.index(self.treeview2.item(i)["values"][0])].split(',')
            values = str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(int(values[3])+int(self.treeview2.item(i)["values"][2])) + "," + str(values[4])

            print("hlo = ", values.split(',')[4])
            self.total = self.total - int(self.treeview2.item(i)["values"][2])*int(values.split(',')[4])
            self.tot.set(self.total)
            print(self.total)

            del medicine_raw[med_name.index(self.treeview2.item(i)["values"][0])]

            medicine_raw.insert(med_name.index(self.treeview2.item(i)["values"][0]), values)

            print(med_name.index(self.treeview2.item(i)["values"][0]))

            self.treeview2.delete(i)
            self.count-=1

        pickle.dump(medicine_raw, file, protocol=2)
        
        values = []
        for i in self.treeview2.get_children():
            values.append(self.treeview2.item(i)["values"])
            self.treeview2.delete(i)
        
        for i in range(len(values)):
            if i%2 == 0:
                self.treeview2.insert(parent='', index="end", iid=i, text=str(i+1), values=values[i], tags=("evenrows"))
            else:
                self.treeview2.insert(parent='', index="end", iid=i, text=str(i+1), values=values[i], tags=("oddrows"))

    def create_bill(self):
        now = datetime.now()
        dt_str = now.strftime("%d-%m-%Y %H-%M-%S")

        self.file_name = "bills/" + str(dt_str) + "@" + str(self.num) + ".txt"
        self.num+=1

        booked = []
        for i in self.treeview2.get_children():
            booked.append(self.treeview2.item(i)["values"])

        dt_str = dt_str.replace("-", "/", 2)
        dt_str = dt_str.replace("-", ":", 2)  

        file_content = f"""
DATE : {dt_str}
=========================================================================================
NAME :           {self.name.get()}
MOBILE :         {self.mob_num.get()}
DOCTOR NAME :    {self.dr_name.get()}
=========================================================================================
 
"""
        for i in booked:
            file_content+= f"{i[0]}          {i[2]}           {i[3]}\n"
        
        file_content+= f"Total payable amount = Rs. {self.tot.get()}"

        file = open(str(self.file_name), "w")
        file.write(file_content)
        file.close()

        print("Bill Created successfully")
        notification.notify(title = "MEDICAL STORE MANAGEMENT SYSTEM", message = f"Bill is created successfully", timeout = 5)

        self.create_bill_btn.config(state="disabled")

    def print_bill(self):
        new_file = tempfile.mktemp('.txt')
        content = []
        with open(self.file_name, "r")as f:
            content = f.readlines()
        open(new_file, "w").writelines(content)
        os.startfile(new_file, 'print')
        print("Successfully requested for printing")
        notification.notify(title = "MEDICAL STORE MANAGEMENT SYSTEM", message = f"Bill is Printed successfully", timeout = 5)

    def clear_all(self):
        for i in self.treeview2.get_children():
            self.treeview2.delete(i)

        self.name.set("")
        self.dr_name.set("")
        self.mob_num.set(0)
        self.file_name = ""

        self.create_bill_btn.config(state="normal")
        self.total = 0
        self.tot.set(0)

    def logout(self):
        self.root.destroy()
        call(['python', 'dashboard_pharmasist.py'])

def main():
    root = Tk()
    obj = sell_medicine(root)
    root.mainloop()

main()
