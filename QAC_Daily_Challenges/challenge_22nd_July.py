def function(input):
    x = input.split(' ') #converts input to a list 
    x = set(x)  # removes dublicates + sorts items
    x = sorted(x)
    result = '' #converts back into a string
    for i in x:
        result = result + i + ' ' # loop appends each item with white space between
    return result
    