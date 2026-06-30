import pandas as pd

car_details = {
    "Car_ID": [101, 102, 103, 104, 105],
    "Brand": ["Maruti", "Hyundai", "Tata", "Honda", "Mahindra"],
    "Name": ["Swift", "Creta", "Nexon", "City", "Scorpio"],
    "Price": [650000, 1200000, 950000, 1400000, 1800000],
    "Fuel_Type": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel"],
    "Mileage": [24, 21, 23, 18, 16]
}

df = pd.DataFrame(car_details)

print("Car Details:")
print(df)