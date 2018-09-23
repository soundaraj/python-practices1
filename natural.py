def nat():
    li = range(1,100)
    count = 0
    d = list(input("enter \n"))
    for i in d:
        if i in li:
            count += 1
    print(count)
nat()
    
