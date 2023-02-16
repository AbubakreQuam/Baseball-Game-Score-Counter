data = []
result = 0
ops = []
ops =input(str("Enter list: "))
list(ops)

if len(ops) > 1000 or len(ops) < 1:
    print("Invalid Input, it has exceeded maximum input length")
else:
    for a in ops:
        if a == "C":
            #Performing C operation
            postion = len(data)
            previous = (data[postion - 1 ])
            del data[postion - 1]
        elif a == "D":
            #Performing D operation
            postion = len(data)
            previous = (data[postion-1])
            data.append(int(previous) * 2)
        elif a == "+":
            #Performing + operation
            postion = len(data)
            previous1 = (data[postion-1])
            previous2 = (data[postion-2])
            sum = int(previous1) + int(previous2)
            data.append(sum)
        else:
            #Performing others operation
            data.append(int(a))
        
        
    for res in data:
        result += res
    print(ops)
    print(data)
    print(result)



