from stack import Stack

print("Bienvenido al sistema de recordatorios")

stack1Tipo = Stack(5)
stack1Tipo.push("Colegio")
stack2Tipo = Stack(5)
stack2Tipo.push("Otro")
stack2Tipo.push("Universidad")
stack2Tipo.push("Trabajo")
stack2Tipo.push("Personal")


stack1Materia = Stack(10)
stack1Materia.push("Matemáticas")
stack2Materia = Stack(10)
stack2Materia.push("Otra")
stack2Materia.push("Ejercicio")
stack2Materia.push("Limpieza")
stack2Materia.push("Física")
stack2Materia.push("Química")
stack2Materia.push("Biología")
stack2Materia.push("Historia")
stack2Materia.push("Literatura")
stack2Materia.push("Inglés")


stack1Dificultad = Stack(5)
stack1Dificultad.push("Fácil")
stack2Dificultad = Stack(5)
stack2Dificultad.push("Muy difícil")
stack2Dificultad.push("Difícil")
stack2Dificultad.push("Media")


stack1Longitud = Stack(5)
stack1Longitud.push("Corta")
stack2Longitud = Stack(5)
stack2Longitud.push("Muy larga")
stack2Longitud.push("Larga")
stack2Longitud.push("Media")


def tipoRecordatorio():
    print("Seleccione el tipo de recordatorio que desea crear")
    print("Navege por el menu con las teclas 'a' y 'd' y seleccione con 'w'")
    print("Tipo de recordatorio: " + stack1Tipo.peek())
    while input() != "w":
        if input() == "a":
            stack2Tipo.push(stack1Tipo.pop())
            print("Tipo de recordatorio: " + stack1Tipo.peek())
        elif input() == "d":
            stack1Tipo.push(stack2Tipo.pop())
            print("Tipo de recordatorio: " + stack1Tipo.peek())
        else:
            print("Opción no válida")
    
    
    return stack1Tipo.peek()

def materiaRecordatorio():
    print("Seleccione el tipo de materia del recordatorio")
    print("Navege por el menu con las teclas 'a' y 'd' y seleccione con 'w'")
    print("Materia: " + stack1Materia.peek())
    while input() != "w":
        if input() == "a":
            stack2Materia.push(stack1Materia.pop())
            print("Materia: " + stack1Materia.peek())
        elif input() == "d":
            stack1Materia.push(stack2Materia.pop())
            print("Materia: " + stack1Materia.peek())
        else:
            print("Opción no válida")
    
    
    return stack1Materia.peek()

def dificultadRecordatorio():
    print("Seleccione la dificultad del recordatorio")
    print("Navege por el menu con las teclas 'a' y 'd' y seleccione con 'w'")
    print("Dificultad: " + stack1Dificultad.peek())
    while input() != "w":
        if input() == "a":
            stack2Dificultad.push(stack1Dificultad.pop())
            print("Dificultad: " + stack1Dificultad.peek())
        elif input() == "d":
            stack1Dificultad.push(stack2Dificultad.pop())
            print("Dificultad: " + stack1Dificultad.peek())
        else:
            print("Opción no válida")
    
    
    return stack1Dificultad.peek()

def longitudRecordatorio():
    print("Seleccione la longitud del recordatorio")
    print("Navege por el menu con las teclas 'a' y 'd' y seleccione con 'w'")
    print("Longitud: " + stack1Longitud.peek())
    while input() != "w":
        if input() == "a":
            stack2Longitud.push(stack1Longitud.pop())
            print("Longitud: " + stack1Longitud.peek())
        elif input() == "d":
            stack1Longitud.push(stack2Longitud.pop())
            print("Longitud: " + stack1Longitud.peek())
        else:
            print("Opción no válida")
    
    
    return stack1Longitud.peek()

tipoRecordatorio()
materiaRecordatorio()
dificultadRecordatorio()
longitudRecordatorio()
descripcion = input("Ingrese la descripción o comentario del recordatorio: ")

print("Recordatorio creado con éxito")
print("Tipo: " + stack1Tipo.peek())
print("Materia: " + stack1Materia.peek())
print("Dificultad: " + stack1Dificultad.peek())
print("Longitud: " + stack1Longitud.peek())
print("Descripción: " + descripcion)
