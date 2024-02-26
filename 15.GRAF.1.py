#при каких А выражение всегда истинно при любом х и у (положительных)
for A in range(1, 1000):
    A_podoshel = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((17*x - 3*y + 17 != 0) or (A < x) or (A < y)) == False:
                A_podoshel = False
                break
        if A_podoshel == False: # чтобы код быстрее закончил работу
            break
    if A_podoshel:
        print(A)