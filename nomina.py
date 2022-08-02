import re

nomina=[]
answers = ['si','no']
question_1 = ""

def checkAnswers (userInput):
    
    if question_1 not in answers:
        print ('>>> RESPONDE EN MINUSCULA - si o no - <<< ')
        return False
    else:
        return True

def checkNumbers (userInput):
    
    try:
        int(userInput)
    except:
        print (">>> POR FAVOR SEÑOR USUARIO, INGRESAR UNICAMENTE NUMEROS <<<")
        return False
    return True

def checkCharacters (userInput):
    
    pattern = re.compile("[A-Za-z]+")
    pattern.fullmatch(userInput)
    # if a match is found
    if pattern.fullmatch(userInput) is not None:
        return True
    else:
        # if no match is found
        print (">>> POR FAVOR SEÑOR USUARIO, INGRESAR UNICAMENTE LETRAS <<<")     
    return False

def inputID():
    inputNotOK = False
    document = 0
    
    while not inputNotOK:
        document = input("INGRESA TU NUMERO DE DOCUMENTO, POR FAVOR: ")
        inputNotOK = checkNumbers(document)
    return int(document)

def inputWorkedDays():
    inputNotOK = False
    days = 0

    while not inputNotOK:
        days = input("INGRESE EL NUMERO DE DIAS TRABAJADOS: ")
        inputNotOK = checkNumbers(days)
    return int(days) 

def inputName():
    inputNotOK = False
    name = ""
    
    while not inputNotOK:
        name = input ("INGRESA SOLAMENTE TU PRIMER NOMBRE: ")
        inputNotOK = checkCharacters(name)
    return name

def inputSecondName():
    inputNotOk = False
    name = ""
    
    while not inputNotOk:
        name = input("INGRESA SOLAMENTE TU SEGUNDO NOMBRE: ")
        inputNotOk = checkCharacters(name)
    return name

def inputSurName():
    inputNotOK = False
    name = ""
    
    while not inputNotOK:
        name = input ("INGRESA SOLAMENTE TU PRIMER APELLIDO: ")
        inputNotOK = checkCharacters(name)
    return name

def inputSecondSurname():
    inputNotOk = False
    name = ""
    
    while not inputNotOk:
        name = input("INGRESA SOLAMENTE TU SEGUNDO APELLIDO: ")
        inputNotOk = checkCharacters(name)
    return name

question_1 = str(input("QUIERE IMPRIMIR SU NOMINA si/no: "))

if checkAnswers (question_1):
    
    while (question_1 == "si"):
        documento = inputID()
        nombres = inputName()
        secondname = inputSecondName()
        apellidos = inputSurName()
        secondSurname = inputSecondSurname()
        dias_trabajados = inputWorkedDays()
        salario = 35000
        salario_base = salario*dias_trabajados
        salario_total = (salario_base-((salario_base*0.04)*2)) + 117100
        
        for i in range(1):
            nomina.append(documento)
            nomina.append(nombres)
            nomina.append(secondname)
            nomina.append(apellidos)
            nomina.append(secondSurname)
            nomina.append(salario)
            nomina.append(dias_trabajados)
            nomina.append(salario_total)

        question_1 = str (input("CONTINUAR si/no: "))
    
    counter = 0
    for item in nomina:
        if counter % 8 == 0:
            print("*************************************************\n")
        print(item)
        counter += 1
        
x = open ("IMPRESION,txt","a")
x.write (str(nomina))