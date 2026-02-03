print("Temperature Converter 🌡️")

choice = input("Convert from (C)elsius or (F)ahrenheit?").lower()

if choice == "c":
  celsius = float(input("Enter temperature in Celsius: "))
  fahrenheit = (celsius * 9/5) +32
  print(f"{celsius}°C is {fahrenheit}°F")
elif choice == "f":
  fahrenheit = float(input("Enter temperature in Fahrenheit: ")
  celsius = (fahrenheit - 32) * 5/9
  print(f"{fahrenheit}°F is {celsius}°C")
else:
  print("Invalid choice. Please enter C or F.")
