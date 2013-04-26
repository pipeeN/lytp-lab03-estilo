a = 4

def FuncionEspecial(N):
    num = eval(input("Ingrese un numero: "))
    if type(num) is int:
        print("Ingresaste un valor entero")
    elif type(num) is complex:
        print("Ingresaste un valor complejo")

FuncionEspecial(3)
