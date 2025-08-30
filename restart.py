import pickle
import os

lst = [
    "Admin,admin,12-12-2006,9876543210,admin@gmail.com,admin,admin,India",
]

file = open("userdata.bin", "wb")
pickle.dump(lst, file)
file.close()

medicines = []
file = open("medicine.bin", "wb")
pickle.dump(medicines, file)
file.close()

file = open("userlogin.bin", "wb")
pickle.dump("", file)
file.close()

file = open("adminlogin.bin", "wb")
pickle.dump("", file)
file.close()

if os.path.exists("bills") == False:
    os.mkdir("bills")

for i in os.listdir("bills/"):
    os.remove(f"bills/{i}")
    