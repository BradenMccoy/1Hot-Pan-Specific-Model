file = open("orders-raw.txt", "r")

lines = file.readlines()
for i in lines:
    print(i)

file.close