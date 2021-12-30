number  = (1, 3, 4, 5, 6, 8)
string  = "Iloveu"
count   = 0


for i in range(1, 201):

    if not((i % 20 == 0) or (i == 0)):
        if (i%11) not in number:
            print(".", end="")
        else:
            print(string[count%6], end="")
            count += 1
    else:
        if (i%11) in number:
            print(string[count%6])
            count += 1
        else:       
            print(".")
