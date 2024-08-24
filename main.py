from tkinter import *
import random
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#0A7CFF")
        self.root.title("Restaurant Billing System")

        title = Label(self.root, text="Restaurant Billing System", bd=12, relief=RIDGE, font=("Arial Black", 20), bg="#A569BD", fg="white")
        title.pack(fill=X)

        # Variables
        self.snacks_vars = [IntVar() for _ in range(7)]
        self.main_course_vars = [IntVar() for _ in range(7)]
        self.snacks_hygiene_vars = [IntVar() for _ in range(7)]

        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.bill_no = StringVar()
        self.bill_no.set(str(random.randint(1000, 9999)))
        self.phone = StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Customer details
        details = LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#A569BD", fg="white", relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        Label(details, text="Customer Name", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=0, padx=15)
        Entry(details, borderwidth=4, width=30, textvariable=self.c_name).grid(row=0, column=1, padx=8)
        Label(details, text="Contact No.", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=2, padx=10)
        Entry(details, borderwidth=4, width=30, textvariable=self.phone).grid(row=0, column=3, padx=8)
        Label(details, text="Bill.No.", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=4, padx=10)
        Entry(details, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5, padx=8)

        # Menu
        self.create_menu_section("Starter", ["Samosa", "Paneer Tikka", "Chicken Tikka", "Vegetable Pakora", "Papdi Chaat", "Tomato Soup", "Masala Papad"], self.snacks_vars, 5, 180)
        self.create_menu_section("Main Course", ["Butter Chicken", "Pasta", "Basmati Rice", "Paneer Masala", "Palak Paneer", "Daal", "Chole Bhature"], self.main_course_vars, 340, 180)
        self.create_menu_section("Snacks", ["Noodles", "Aloo Tikki Chaat", "Dahi Vada", "Pav Bhaji", "Bhel Puri", "Soup", "Pokara"], self.snacks_hygiene_vars, 677, 180)

        # Bill area
        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#E5B4F3")
        billarea.place(x=1010, y=188, width=330, height=372)
        Label(billarea, text="Bill Area", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#E5B4F3", fg="#6C3483").pack(fill=X)
        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Billing menu
        billing_menu = LabelFrame(self.root, text="Billing Summary", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#A569BD", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        self.create_billing_summary(billing_menu)

        # Buttons
        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#6C3483")
        button_frame.place(x=830, width=500, height=95)
        Button(button_frame, text="Total Bill", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", command=self.total).grid(row=0, column=0, padx=12)
        Button(button_frame, text="Clear Field", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", command=self.clear).grid(row=0, column=1, padx=10, pady=6)
        Button(button_frame, text="Exit", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", width=8, command=self.exit).grid(row=0, column=2, padx=10, pady=6)

        self.intro()

    def create_menu_section(self, section_name, items, variables, x, y):
        section = LabelFrame(self.root, text=section_name, font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483", relief=GROOVE, bd=10)
        section.place(x=x, y=y, height=380, width=325)
        for i, item in enumerate(items):
            Label(section, text=item, font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=i, column=0, pady=11)
            Entry(section, borderwidth=2, width=15, textvariable=variables[i]).grid(row=i, column=1, padx=10)

    def create_billing_summary(self, frame):
        labels = ["Total Snacks Price", "Total Grocery Price", "Total Hygiene Price", "Snacks Tax", "Grocery Tax", "Hygiene Tax"]
        variables = [self.total_sna, self.total_gro, self.total_hyg, self.a, self.b, self.c]
        for i, (label, var) in enumerate(zip(labels, variables)):
            row, col = divmod(i, 2)
            Label(frame, text=label, font=("Arial Black", 11), bg="#A569BD", fg="white").grid(row=row, column=col*2)
            Entry(frame, width=30, borderwidth=2, textvariable=var).grid(row=row, column=col*2+1, padx=10, pady=7)

    def total(self):
        if self.c_name.get() == "" or self.phone.get() == "":
            messagebox.showerror("Error", "Fill the complete Customer Details!!")
            return

        self.calculate_section_total(self.snacks_vars, [120, 40, 10, 20, 30, 60, 15], self.total_sna, self.a, 0.05)
        self.calculate_section_total(self.main_course_vars, [42, 120, 113, 160, 55, 480, 76], self.total_gro, self.b, 0.01)
        self.calculate_section_total(self.snacks_hygiene_vars, [30, 180, 130, 500, 85, 100, 20], self.total_hyg, self.c, 0.10)

        total_bill = sum(float(var.get().split()[0]) for var in [self.total_sna, self.total_gro, self.total_hyg]) + \
                     sum(float(var.get().split()[0]) for var in [self.a, self.b, self.c])
        self.total_all_bil = f"{total_bill} Rs"

        self.billarea()

    def calculate_section_total(self, variables, prices, total_var, tax_var, tax_rate):
        total_price = sum(var.get() * price for var, price in zip(variables, prices))
        total_var.set(f"{total_price} Rs")
        tax_var.set(f"{round(total_price * tax_rate, 3)} Rs")

    def intro(self):
        self.txtarea.delete(1.0, END)
        self.txtarea.insert(END, "\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
        self.txtarea.insert(END, f"\n\nBill no. : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone No. : {self.phone.get()}")
        self.txtarea.insert(END, "\n====================================\n")
        self.txtarea.insert(END, "\nProduct\t\tQty\tPrice\n")
        self.txtarea.insert(END, "\n====================================\n")

    def billarea(self):
        self.intro()
        self.add_section_to_bill("Snacks", ["Samosa", "Paneer Tikka", "Chicken Tikka", "Vegetable Pakora", "Papdi Chaat", "Tomato Soup", "Masala Papad"], self.snacks_vars, [120, 40, 10, 20, 30, 60, 15])
        self.add_section_to_bill("Main Course", ["Butter Chicken", "Pasta", "Basmati Rice", "Paneer Masala", "Palak Paneer", "Daal", "Chole Bhature"], self.main_course_vars, [42, 120, 113, 160, 55, 480, 76])
        self.add_section_to_bill("Snacks", ["Noodles", "Aloo Tikki Chaat", "Dahi Vada", "Pav Bhaji", "Bhel Puri", "Soup", "Pokara"], self.snacks_hygiene_vars, [30, 180, 130, 500, 85, 100, 20])

        self.txtarea.insert(END, f"\n------------------------------------")
        self.txtarea.insert(END, f"\n Total Price : \t\t{self.total_all_bil}")
        self.txtarea.insert(END, f"\n\nThank you for shopping with us!")

    def add_section_to_bill(self, section_name, items, variables, prices):
        for item, var, price in zip(items, variables, prices):
            if var.get() != 0:
                self.txtarea.insert(END, f"\n{item}\t\t{var.get()}\t{var.get() * price}")

    def clear(self):
        self.txtarea.delete(1.0, END)
        self.c_name.set("")
        self.phone.set("")
        self.bill_no.set(str(random.randint(1000, 9999)))
        for var_list in [self.snacks_vars, self.main_course_vars, self.snacks_hygiene_vars]:
            for var in var_list:
                var.set(0)
        for var in [self.total_sna, self.total_gro, self.total_hyg, self.a, self.b, self.c]:
            var.set("")
        self.intro()

    def exit(self):
        if messagebox.askyesno("Exit", "Do you really want to exit?"):
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()
