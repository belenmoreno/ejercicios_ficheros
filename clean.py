fd = open ("programa.py", "r")
fd2 = open ("programa.txt", "w")
line = fd.readline()
#print(line)
while line:
    if line[0] != "#":
        print(line)
        fd2.write(line)
    line = fd.readline()