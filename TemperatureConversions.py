#CS175L
#Andrew Fisher
#Temperature Conversions

def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    kelvin = ((fahrenheit - 32) * (5/9)) + 273.15
    return kelvin
    pass

def convertToCentigrade(fahrenheit):
    centigrade = ((fahrenheit - 32) * (5/9))
    return centigrade
    pass

def doConversion():
    fahrenheit = getFahrenheit()
    kelvin = convertToKelvin(fahrenheit)
    centigrade = convertToCentigrade(fahrenheit)
    print(f'Fahrenheit: {fahrenheit} Kelvin: {kelvin:.2f} Centigrade: {centigrade:.2f}')
    pass

def repeat():
    conversions = int(input("How many conversions would you like to do this time? "))
    for x in range(conversions):
        doConversion()
    pass

def controlLoop():
    response = str(input("Do you want to do some conversions(Yes or No)? "))
    if response == "yes" or "Yes":
        repeat()
    pass

def getFahrenheit():
    fahrenheit = int(input("Enter Fahrenheit temperature (must be -50 to 130): "))
    while fahrenheit < -50 or fahrenheit > 130:
        fahrenheit = int(input("Please re-enter: "))
    return fahrenheit
    pass

# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
