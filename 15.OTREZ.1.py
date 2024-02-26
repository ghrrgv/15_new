P = list(range(3, 19))
Q = list(range(11, 24))
A = []
for x in range(1, 50):
    if (((x in P)and(x in Q))<=(x in A)) == False: # чтобы найти
# минимальную длинну отрезка А, нужно понять в каких вариантах функция ложная
# так найдутся границы допустимого
        A.append(x)
print(A)