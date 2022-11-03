from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
name = input("Ingresa el nombre del archivo: ")

try:
    file = open(name, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    file.close()
    file = open(name + '.hist', 'wt')
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        c = counters[char]
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')
    file.close()
except IOError:
    print("Error: ", strerror(IOError.errno))