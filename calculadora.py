#importando la librería sys
import sys
#Agregando la ruta de los módulos usados al sys.path
sys.path.append('c:\\Users\\juanm\\OneDrive\\Desktop\\Otalorin\\Python\\Practica Modulos\\Funciones')
#Importando los módulos locales
from extraer_terminos import Extraer_terminos 
from generar_resultado import Generar_resultado
from verificar_decimal import Verificar_decimal

def Calculadora(texto, resultado = False):
    '''
    Calculadora( texto => str, resultado)

    La función recibe un texto como parámetro, el texto debe contener una operación matemática para que
    se ejecute correctamente

    Nota: El segundo parámetro que recibe la funcón es para el funcionamiento interno de la función.
    Por ende, no es necesario rellenar este parametro
    '''
    #Verificando si el usuario de sea salir de la función calculadora
    if texto.lower() == "salir": 
       #Imprimiendo un mensaje de confirmación
       print("cerrado correctamente")
    else:
       #inicializando la variable resul localmente
       resul = 0
       #Verificando si el segundo parámetro esta en uso. Es decir verificando si hay un resultado anterior
       if not type(resultado) == bool: 
          #Agregando el resultado al texto de la operación
          texto_nuevo = str(resultado)+texto
          #Desempaquetando el 1° término (t1), la operación matemática a realizar (op) y el 2° término (t2)
          #haciendo uso de la función Extraer_terminos
          t1,op,t2 = Extraer_terminos(texto_nuevo)
          #Convirtiendo el primer y segundo término a un dato float
          a, b = float(t1), float(t2)
          #Ingresando las partes de la operación a la función Generar_resultado() y guardandolo en la variable resul
          resul = Generar_resultado(op,a,b)

       #Este código se ejecuta en el primer ciclo de la función
       else:
         #Desempaquetando el 1° término (t1), la operación matemática a realizar (op) y el 2° término (t2)
         #haciendo uso de la función Extraer_terminos
         t1,op,t2 = Extraer_terminos(texto)
         #Convirtiendo el primer y segundo término a un dato float
         a, b = float(t1), float(t2)
         #Ingresando las partes de la operación a la función Generar_resultado() y guardandolo en la variable resul
         resul = Generar_resultado(op,a,b)

       #Verificando si el resultado es un float con un solo decimal 0, por medio de la función Verificar_decimal()
       if Verificar_decimal(resul):
         #Redondeando resul, para eliminar el decimal inecesario
         resul = round(resul)
         #Ejecutando un nuevo ciclo de la función, el cual hace uso del segundo parámetro, para guardar el resultado
         Calculadora(input(f"El resultado es: {resul}"),resul)
       else: 
         Calculadora(input(f"El resultado es: {resul}"),resul)
    
    
#Imprimiendo un mensaje para el usuario
print('Escriba "salir" para cerrar la calculadora')