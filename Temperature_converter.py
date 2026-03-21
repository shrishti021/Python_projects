# Temperature Converter App
# INTERMEDIATE
# 20 pts
# 📌 A weather app needs to display temperatures in Celsius, Fahrenheit, and Kelvin. Build conversion functions.
# 🎯 Task: Write a function convert_temp(value, from_unit, to_unit) that converts between C, F, and K. Handle invalid unit inputs with a clear error message.
# Temperature Converter
# Formulas:
# C to F: (C * 9/5) + 32
# F to C: (F - 32) * 5/9
# C to K: C + 273.15
# K to C: K - 273.15

def convert_temp(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    value_units = ["C", "F", "K"]
    if from_unit not in value_units or to_unit not in value_units:
        return "Error: Invalid unit! Use 'C', 'F', or 'K'."
    
    # 🔁 Convert input → Celsius (base unit)
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5/9
    elif from_unit == "K":
        celsius = value - 273.15

    # 🔁 Convert Celsius → target unit
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return  (value * 9/5) + 32
    elif to_unit == "K":
        return value + 273.15


# Test it:
print(convert_temp(100, "C", "F"))  # should be 212.0
print(convert_temp(32, "F", "C"))   # should be 0.0
print(convert_temp(0, "C", "K"))    # should be 273.15
print(convert_temp(50, "X", "C"))   # Error