
def temperature_converter():
    temperatura = float(input('por favor ingresa en datos númericos los grados que quieres convertir: '))
    unidad = str(input("por favor coloca 'c' para celcius o 'f' para fahrenheit: "))


    if isinstance(temperatura,(int, float)) and isinstance(unidad, str):
        if unidad == 'c':
            print(f'la temperatura convertida es: {(temperatura * 9 / 5) + 32}°f')
        elif unidad == 'f':
            print(f'la temperatura convertida es: {(temperatura - 32) * 5/9}°c')

temperature_converter()