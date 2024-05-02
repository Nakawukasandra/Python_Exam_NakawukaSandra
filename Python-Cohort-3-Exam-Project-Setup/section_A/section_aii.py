def celsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsiusToFahrenheit(celsius)
        print("Temperature in Fahrenheit:", fahrenheit)
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheitToCelsius(fahrenheit)
        print("Temperature in Celsius:", celsius)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

