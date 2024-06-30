def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32.0

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32.0) * 5.0 / 9.0

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32.0) * 5.0 / 9.0 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9.0 / 5.0 + 32.0

def main():
    print("Temperature Conversion Program")
    print("-------------------------------")

    while True:
        temperature = float(input("Enter temperature value: "))
        unit = input("Enter temperature unit (C/F/K): ").upper()

        if unit == "C":
            print("Converting Celsius to Fahrenheit and Kelvin...")
            fahrenheit = celsius_to_fahrenheit(temperature)
            kelvin = celsius_to_kelvin(temperature)
            print(f"{temperature}°C is equal to {fahrenheit}°F and {kelvin}K")
        elif unit == "F":
            print("Converting Fahrenheit to Celsius and Kelvin...")
            celsius = fahrenheit_to_celsius(temperature)
            kelvin = fahrenheit_to_kelvin(temperature)
            print(f"{temperature}°F is equal to {celsius}°C and {kelvin}K")
        elif unit == "K":
            print("Converting Kelvin to Celsius and Fahrenheit...")
            celsius = kelvin_to_celsius(temperature)
            fahrenheit = kelvin_to_fahrenheit(temperature)
            print(f"{temperature}K is equal to {celsius}°C and {fahrenheit}°F")
        else:
            print("Invalid temperature unit. Please enter C, F, or K.")

        response = input("Do you want to convert another temperature? (Y/N): ").upper()
        if response != "Y":
            break

if __name__ == "__main__":
    main()