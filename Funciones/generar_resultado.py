#Importando el modúlo funciones matemáticas
import funciones_matematicas

def Generar_resultado(op,a,b):
    '''
    Generar_resultado( op => str , a => int ó float , b => int ó float)

    La función evalua el parámetro op para así saber cual operación 
    matemática realizar con los parámetros a y b
    '''
    if op == "+": return funciones_matematicas.Sumar(a,b)
    elif op == "-": return funciones_matematicas.Restar(a,b)
    elif op == "x": return funciones_matematicas.Multiplicar(a,b)
    #Si es una operación negativa el segundo número se pasa negativo
    elif op == "x-": return funciones_matematicas.Multiplicar(a,-b)
    elif op == "/": return funciones_matematicas.Dividir(a,b)
    #Si es una operación negativa el segundo número se pasa negativo
    elif op == "/-": return funciones_matematicas.Dividir(a,-b)
