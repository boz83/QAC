def sevenNotFive(x,y):
    numbers = []
    for num in range(x,y):
        if num % 7 == 0 and num % 5 != 0:
            numbers.append(num)
    return numbers