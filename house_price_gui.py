import tkinter as tk
from tkinter import messagebox


                #CALCULATION PART
def predict():
    try:
        b, ba, s = int(bed.get()), int(bath.get()), float(size.get())
        p, c = int(park.get()), int(cond.get())
        price = s*4500 + b*80000 + ba*50000 + p*70000 + c*30000
# b → bedrooms,ba → bathrooms,s → size ,p → parking c → condition
        messagebox.showinfo("Result", f"🏡 Estimated Price: ₹{price:,.0f}")
    except:
        messagebox.showerror("Error", "Fill all fields correctly!")

                    #GUI WINDOW 

root = tk.Tk()
root.title("🏠 House Price Predictor")
root.geometry("360x380")
root.config(bg="#709D9B")


fields = [("Bedrooms",1),("Bathrooms",2),("Size (sqft)",3),("Parking (0/1)",4),("Condition (1-5)",5)]
vars = [] #entry list where entry boxex will store
for i,(t,r) in enumerate(fields):
    tk.Label(root,text=t,bg="#DCE6F1",fg="#130F54",font=("Segoe UI",10,"bold")).place(x=40,y=60+i*50)
vars = [tk.Entry(root,width=10,bd=2,justify='center') for _ in fields]
for i,v in enumerate(vars): v.place(x=220,y=60+i*50)
bed,bath,size,park,cond = vars
tk.Button(root,text="Predict Price 💰",bg="#2563EB",fg="white",font=("Segoe UI",11,"bold"),
          activebackground="#1D4ED8",width=20,command=predict).place(x=80,y=320)
root.mainloop()
