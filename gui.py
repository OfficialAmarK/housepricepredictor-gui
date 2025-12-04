import tkinter as tk
from tkinter import messagebox

# ----------------------------------------- PRICE PREDICTION FUNCTION ------------------------------------------

def predict_price():
    try:
        # Get user input
        b = int(bed.get())         
        ba = int(bath.get())      
        s = float(size.get())      
        p = int(park.get())        
        c = int(cond.get())        
        y = int(year_var.get())   

        base_price = s*4500 + b*80000 + ba*50000 + p*70000 + c*30000

        # year choose krne ke liye
        # House loses 1.2% value per year older than 2025
        year_factor = (1 - 0.012) ** (2025 - y)

        final_price = base_price * year_factor

        #result aayege
        messagebox.showinfo("Estimated Price",
                            f"🏡 Estimated Price (Year {y}): ₹{final_price:,.0f}")

    except ValueError:
        messagebox.showerror("Error", "Please fill all fields correctly!")

#interface of gui
root = tk.Tk()
root.title("🏠 House Price Predictor")
root.geometry("380x460")
root.config(bg="#709D9B")

#labels or buttons 
labels = ["Bedrooms", "Bathrooms", "Size (sqft)", "Parking (0/1)", "Condition (1-5)"]
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text, bg="#DCE6F1", fg="#130F54",
             font=("Segoe UI", 10, "bold")).place(x=40, y=60 + i*50)

    entry = tk.Entry(root, width=12, bd=2, justify='center')
    entry.place(x=220, y=60 + i*50)
    entries.append(entry)

# Unpack entry boxes
bed, bath, size, park, cond = entries

# YEAR DROPDOWN per year
tk.Label(root, text="Construction Year", bg="#DCE6F1", fg="#130F54",
         font=("Segoe UI",10,"bold")).place(x=40, y=60 + 5*50)

# Dropdown with years 2000–2025
year_var = tk.StringVar()
year_var.set("2025")

year_menu = tk.OptionMenu(root, year_var, *list(range(2000, 2025+1)))
year_menu.config(width=10)
year_menu.place(x=220, y=60 + 5*50)

# PREDICT BUTTON
tk.Button(root, text="Predict Price 💰", bg="#2563EB", fg="white",
          font=("Segoe UI", 11, "bold"), width=20,
          activebackground="#1D4ED8",
          command=predict_price).place(x=90, y=380)

root.mainloop()