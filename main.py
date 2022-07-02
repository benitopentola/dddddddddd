class Miclase:
  print("Culo")
  pass # Implementar más tarde
for letra in "python":
  if letra=="h":
      continue
  print("Viendo letra: " + letra)
Miclase()
email=input("introduce tu email, por favor: ")

for i in email:
  if i=="@":
    arroba=True
    break;
else:
    arroba=False
print(arroba)

#prueba eval

number = 88

square_number = eval('number * number')

print(square_number)

print('Básicamente evalua si la oración es valida en python')
print('Creo')

#prueba exec

program = 'a = 555\nb=9595\nprint("Sum =", a+b*3)'
exec(program)
print('Ejecuta metodos creados de manera dinamica')


#pruebas filter
print('PRUEBA FILTER')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Devuelve TRUE si el numero es par.
# Number tan solo es una variable dentro de esto.
def check_even(number):
    if number % 2 == 0:
          return True
    return False
# Extrae los numeros que sean true con el filter.
even_numbers_iterator = filter(check_even, numbers)

even_numbers = list(even_numbers_iterator)

print(even_numbers)

#PRUEBAS FLOAT

numero222 = 25

float_number = float(numero222)

print(float_number)

# Output: 25.0

