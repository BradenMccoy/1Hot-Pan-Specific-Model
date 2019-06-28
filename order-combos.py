file = open("orders-raw.txt", "r")
output = open("output.txt", "a+")


lines = file.readlines()
for i in lines:
    output.write("New Base:\n")
    for j in lines:
        output.write(i)
        
        output.write(j)
    output.write("\n")

file.close
output.close