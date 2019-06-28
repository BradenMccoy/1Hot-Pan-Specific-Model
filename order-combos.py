file = open("orders-raw.txt", "r")
output = open("order_pairs.txt", "a+")


lines = file.readlines()
for i in lines:
    for j in lines:
        output.write(i)
        output.write(j)
    

file.close
output.close