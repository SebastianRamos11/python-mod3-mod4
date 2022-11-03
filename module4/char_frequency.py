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
    for char in counters.keys():
        cnt = counters[char]
        if cnt > 0:
            print(char, '->', cnt)

except IOError as e:
    print("Error:", strerror(e.errno))