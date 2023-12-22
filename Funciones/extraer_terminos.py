def Recorrer_op(letra):
    '''
    Recorrer_op( letra => str )

    La función recibe un carácter string para evaluar si coincide con alguna de las operaciones específicadas
    '''
    #Creando una lista con las distintos caracteres que representan una operación matemática
    operaciones = ["+","-","x","/"]
    #Recorriendo los elementos de la lista 
    for op in operaciones:
        #Evaluando los carácteres de la lista con la letra pasada como parámetro
        if op == letra: return True
    return False

def Recorrer_op_negativas(letras):
    '''
    Recorrer_op_negativas( letras => str )

    La función recibe dos carácter string para evaluar si coincide con alguna de las operaciones específicadas
    '''
    #Creando una lista con las distintos caracteres que representan una operación matemática negativa
    operaciones_negativas = ["x-","/-"]
    #Recorriendo los elementos de la lista 
    for op in operaciones_negativas:
        #Evaluando los carácteres de la lista con las letras pasadas como parámetro
        if op == letras: return True
    return False

def Extraer_terminos(texto):
    '''
    Extraer_terminos( texto => str )

    La función recibe un string como parámetro, en donde evalua si contiene caracteres que representen
    una operación matemática, si es así, devuelve los terminos de la operación a realizar.

    Si el parámetro recibido no cumple con los requisitos para ser una operación matemática, la función
    devolverá un string 

    return tuple(término1,operación,término2)
    '''
    #inicializando localmente el parámetro recibido
    texto = texto
    #Creando una varieble la cual permite saber si el primer termino es negativo
    negativo = False

    #Verificando si el primer término de la operacion es negativo
    if Recorrer_op(texto[0]): 
        #Si es así, actualiza el texto para no generar errores en la función 
        texto = texto[:0] + texto[1:]
        negativo = True
    #Recorriendo el texto recibido
    for i,l in enumerate(texto):
        #Pasando el carácter como parámetro de la función Recorrer_op 
        validacion_op =  Recorrer_op(l)
        #Pasando el carácter y su siguiente como parámetro de la función Recorrer_op_negativas
        validacion_op_negativa = Recorrer_op_negativas(texto[i:i+2])
        #Validando si la operación metemática contiene una operación negativa
        if validacion_op and validacion_op_negativa:
            #Generandp el primer término de la operación
            termino1 = texto[0:i]
            #Generandp la operación matemática (en este caso negativa) a realizar en la operación
            op = texto[i:i+2]
            #Generandp el segundo término de la operación
            termino2 = texto[i+2:len(texto)]
            #Validando si el primer término es negativo o no
            if negativo: return "-"+termino1,op,termino2
            return termino1,op,termino2
        #Validando si la operación metemática contiene una operación
        elif validacion_op:
            #Generandp el primer término de la operación
            termino1 = texto[0:i]
            #Generandp la operación matemática a realizar en la operación
            op = texto[i:i+1]
            #Generandp el segundo término de la operación
            termino2 = texto[i+1:len(texto)]
            #Validando si el primer término es negativo o no
            if negativo: return "-"+termino1,op,termino2
            return termino1,op,termino2
    #Si no encuentra ninguna operación matemática devuelve el siguiente mensaje
    return "No es una operación matemática"


