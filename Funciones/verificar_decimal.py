def Verificar_decimal(n):
    '''
    Verificar_decimal( n => int ó float)

    La función convierte a string el número pasado por parámetro, para evaluar si n es un float
    que termina en 0, o un float con números decimales
    '''
    #Convirtiendo n a string
    texto_n = str(n)
    #Recorriendo el string de n 
    for ind,letra in enumerate(texto_n):
        #Verificando si el string de n contiene un "." y despues un "0"
        if letra == "." and texto_n[ind+1] == "0": return True
    return False
    