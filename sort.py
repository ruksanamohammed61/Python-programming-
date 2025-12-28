try:
    name = input("Enter file name: ")
    f = open(name, "r")

    n = input("Enter new file name to write data: ")
    f1 = open(n, "a")

    v = []  # list to store words

    for i in f.readlines():
        p = i.split()
        v = v + p

    z = []
    for i in v:
        z.append(i.lower())

    u = sorted(z)

    f1.write('\n'.join(u))  # write after everything is ready

    f1.close()
    f.close()

    print("Data has been written to", n)

except FileNotFoundError as e:
    print(e)
