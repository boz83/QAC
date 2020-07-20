n=int(input(('Please input a positive integer: ')))

def multiplicationgrid(n):
  for x in range(1,n+1):
        for y in range(1,n+1):
            print ('{:3}'.format(x*y), end='\t')
        print()
  return

print(multiplicationgrid(n))

