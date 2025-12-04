House Price Predictor (Python + Tkinter)

A simple desktop application that calculates an estimated house price based on user-entered property details. The app uses a clean Tkinter GUI and a custom pricing formula with year-based depreciation.

📌 Features

GUI built using Tkinter

Takes inputs for:

Bedrooms

Bathrooms

House size (sqft)

Parking (0/1)

Condition rating (1–5)

Construction year (2000–2025)

Applies a pricing formula:

base_price = size*4500 + bedrooms*80000 + bathrooms*50000
             + parking*70000 + condition*30000


Includes 1.2% yearly depreciation for houses older than 2025

Shows final estimated price in a popup

Handles invalid inputs with error messages

🚀 How to Run

Install Python 3.x

Save the script as house_price_predictor.py

Run the file:

python house_price_predictor.py

📂 Project Structure
housepricepredictor-gui/
│
├── house_price_predictor.py
└── README.md

🛠 Requirements

No external libraries required.
Only built-in modules:

tkinter

messagebox
