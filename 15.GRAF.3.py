for A in range(1, 1000):
    if all([(((y + 7*x !=36) or(A>x-2))or(A<y+27))for x in range(1, 1000) for y in range(1, 1000)]) == True:
        print(A)