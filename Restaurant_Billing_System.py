import tkinter as tk
from tkinter import messagebox

# Menu items and their prices
menu = {
    1: {"item": "Rice", "price": 15.00},
    2: {"item": "Dal", "price": 10.00},
    3: {"item": "Ruti", "price": 10.00},
    4: {"item": "Porita", "price": 8.00},
    5: {"item": "Mixed Vegetable", "price": 20.00},
    6: {"item": "Singara", "price": 10.00},
    7: {"item": "Somucha", "price": 10.00},
    8: {"item": "Sandwich", "price": 30.00},
    9: {"item": "Pasta", "price": 30.00},
    10: {"item": "Coffee", "price": 20.00},
    11: {"item": "Tea", "price": 15.00},
    12: {"item": "Fried Chicken", "price": 8.00},
    13: {"item": "Fried Rice", "price": 30.00},
    14: {"item": "Burger", "price": 50.00},
    15: {"item": "Special Ruti", "price": 25.00},
    16: {"item": "Grill Chicken", "price": 100.00},
    17: {"item": "Shorma", "price": 90.00},
    18: {"item": "Jelabi", "price": 10.00},
    19: {"item": "Muglai", "price": 30.00},
    20: {"item": "Chula But", "price": 15.00}
}

# Function to calculate the total price
def calculate_total(order):
    total = 0
    for item_number, quantity in order.items():
        price = menu[item_number]["price"]
        total += price * quantity
    return total

# Function to calculate tax
def calculate_tax(total):
    return total * 0.02  # 5% tax

# Function to generate the bill
def generate_bill(order):
    total = calculate_total(order)
    tax = calculate_tax(total)
    final_total = total + tax

    bill_text = "***** BILL *****\n"
    bill_text += f"{'Item':<20}{'Qty':<5}{'Price':<10}{'Total'}\n"
    bill_text += "-" * 40 + "\n"

    for item_number, quantity in order.items():
        item_name = menu[item_number]["item"]
        price = menu[item_number]["price"]
        item_total = price * quantity
        bill_text += f"{item_name:<20}{quantity:<5}${price:<10.2f}${item_total:.2f}\n"

    bill_text += "-" * 40 + "\n"
    bill_text += f"{'Subtotal':<30}${total:.2f}\n"
    bill_text += f"{'Tax (2%)':<30}${tax:.2f}\n"
    bill_text += f"{'Total Amount':<30}${final_total:.2f}\n"
    bill_text += "-" * 40

    return bill_text

# Function to handle button clicks for adding items to order
def add_item():
    try:
        item_number = int(item_var.get())
        quantity = int(quantity_var.get())

        if item_number < 1 or item_number > 20:
            messagebox.showerror("Invalid Item", "Please select a valid item number (1-20).")
            return

        if quantity <= 0:
            messagebox.showerror("Invalid Quantity", "Quantity must be greater than 0.")
            return

        if item_number in order:
            order[item_number] += quantity
        else:
            order[item_number] = quantity

        item_var.set('')
        quantity_var.set('')

        update_order_list()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for item number and quantity.")

# Function to update the displayed order list
def update_order_list():
    order_list_text.delete(1.0, tk.END)
    for item_number, quantity in order.items():
        item_name = menu[item_number]["item"]
        order_list_text.insert(tk.END, f"{item_name}: {quantity}\n")

# Function to generate and display the bill
def show_bill():
    if not order:
        messagebox.showwarning("No Items", "Please add items to the order first.")
        return

    bill_text = generate_bill(order)
    bill_textbox.delete(1.0, tk.END)
    bill_textbox.insert(tk.END, bill_text)

# Function to clear the order
def clear_order():
    order.clear()
    order_list_text.delete(1.0, tk.END)
    bill_textbox.delete(1.0, tk.END)



# Creating the main application window
root = tk.Tk()
root.title('CUET Cafetatia')
root.geometry('400x500')
root.configure(background='navy blue')
root.resizable(0,0)





# Global variables for storing user input and order
order = {}

# Define input fields
item_var = tk.StringVar()
quantity_var = tk.StringVar()

# Create the GUI components
menu_label = tk.Label(root, text="Select Menu Item (1-20):")
menu_label.grid(row=0, column=0)

item_entry = tk.Entry(root, textvariable=item_var, width=5)
item_entry.grid(row=0, column=1)

quantity_label = tk.Label(root, text="Enter Quantity:")
quantity_label.grid(row=1, column=0)

quantity_entry = tk.Entry(root, textvariable=quantity_var, width=5)
quantity_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add to Order", command=add_item)
add_button.grid(row=2, column=0, columnspan=2)

order_list_label = tk.Label(root, text="Order List:")
order_list_label.grid(row=3, column=0, columnspan=2)

order_list_text = tk.Text(root, height=10, width=30)
order_list_text.grid(row=4, column=0, columnspan=2)

bill_button = tk.Button(root, text="Generate Bill", command=show_bill)
bill_button.grid(row=5, column=0, columnspan=2)

clear_button = tk.Button(root, text="Clear Order", command=clear_order)
clear_button.grid(row=6, column=0, columnspan=2)

bill_label = tk.Label(root, text="Generated Bill:")
bill_label.grid(row=7, column=0, columnspan=2)

bill_textbox = tk.Text(root, height=10, width=50)
bill_textbox.grid(row=8, column=0, columnspan=2)

# Run the GUI application
root.mainloop()
