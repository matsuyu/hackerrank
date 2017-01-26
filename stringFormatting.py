def print_formatted(number):
    width=len('{:b}'.format(n))
    for num in range(1,number+1): 
        for base in 'doXb':
            print('{0:{width}{base}}'.format(num,base=base, width=width), end=' ')
        print()
