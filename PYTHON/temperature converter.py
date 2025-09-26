def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice in [1, 2, 3, 4]:
            temp = float(input("Enter temperature: "))
            if choice == 1:
                print(f"{temp} Celsius = {celsius_to_fahrenheit(temp)} Fahrenheit")
            elif choice == 2:
                print(f"{temp} Fahrenheit = {fahrenheit_to_celsius(temp)} Celsius")
            elif choice == 3:
                print(f"{temp} Celsius = {celsius_to_kelvin(temp)} Kelvin")
            elif choice == 4:
                print(f"{temp} Kelvin = {kelvin_to_celsius(temp)} Celsius")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()