def conversion_centigrados():
    centigrados = float(input("Ingrese la temperatura en grados Centigrados"))

    # Conversion a grados Fahrenheit
    fahrenheit = centigrados * 9/5 + 32
    print("La temperatura en grados Fahrenheit es:", fahrenheit) 
   
    # Conversion a grados Kelvin 
    Kelvin = centigrados + 273.15
    print("La temperatura en grados Kelvin es:", Kelvin)
    
conversion_centigrados()    
