from os import strerror

class StudentsDataException(Exception):
    pass

class ErrorLine(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self, message)

class FileEmpty(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self, message)

dic = {}
name = input("Ingresa el nombre del archivo: ")

try:
    file = open(name, "rt")
    lines = file.readlines()    
    file.close()
    if len(lines) == 0:
        raise FileEmpty("Error: El archivo está vacío")
    for i in range(len(lines)):
        temp = lines[i].split()
        if len(temp) != 3:
            raise ErrorLine("Error: línea incorrecta en el archivo: " + str(i + 1))
        name = temp[0] + ' ' + temp[1]
        if name not in dic:
            dic[name] = float(temp[2])
        else:
            dic[name] += float(temp[2])
except FileEmpty as fe:
    print(fe)
    exit(1)
except ErrorLine as errl:
    print(errl)
    exit(2)
except IOError as e:
    print("Error: No se puede abrir el archivo: ", strerror(e.errno))
    exit(e.errno)

for key in sorted(dic.keys()):
    print(key, dic[key])