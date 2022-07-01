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