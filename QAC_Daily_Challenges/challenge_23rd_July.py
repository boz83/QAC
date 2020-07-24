def sum(a):
    numbers=[]
    numbers.append(a)
    for i in range(1,4):
        numbers.append(int(str(numbers[i-1])+str(a)))
    return sum(numbers)