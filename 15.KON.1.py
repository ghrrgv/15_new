#При каком наимелньшем А выражение истинно при лбом х

for A in range(1, 1000):
    for x in range(1,1000):
        if ((x&79!=0)<=((x&64==0)<=(x&A!=0))) == False:
            break
    else:
        print(A)