notas = []

for i in range(3):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)

print(f"El promedio es: {promedio:.2f}")
