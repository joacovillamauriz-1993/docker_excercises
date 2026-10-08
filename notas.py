alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]

contAprob = 0
sumaNotas = 0
for alumno in alumnos:
    nota = alumno["nota"]

    if nota >= 5:
        estado = "Aprobad@"
        contAprob += 1
    else: 
        estado = "Suspens@"
    
    print(f"{alumno["nombre"].upper()}: {nota} -> {estado} ")
    sumaNotas += float(nota)

    

print(f"\nTotal estudiantes: {len(alumnos)}")
print(f"Estudiantes aprobadxs: {contAprob}")
print(f"Estudiantes suspensxs: {len(alumnos) - contAprob}")
print(f"Media de la clase: {sumaNotas/len(alumnos)}")