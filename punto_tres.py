Dinero = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")

print(Dinero.get(moneda.title(), "La divisa no está."))
precio_dolar = float(input("Ingresa el costo del dólar en pesos: "))
dolares = float(input("Ingresa la cantidad de dólares: "))
pesos = dolares * precio_dolar
print(f"Los {dolares} dólares equivalen a {pesos} pesos")