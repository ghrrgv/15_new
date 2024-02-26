for A in range(1, 1000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y-13*x < A) or (x >88) or (y >77)) == False:
                break
        if ((y - 13 * x < A) or (x > 88) or (y > 77)) == False: # нужно чтобы выкинула и с х и с у
            break
    else: # выполняется только после полного выполнении цикла
        print(A)