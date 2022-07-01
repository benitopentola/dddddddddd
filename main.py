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