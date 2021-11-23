def inputValues():
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))
    c = float(input("Enter third value: "))
    d = float(input("Enter fourth value: "))
    
    if a < b:
        a,b = b,a
    if a < c:
        a,c = c,a
    if a < d:
        a,d = d,a
    if b < c:
        b,c = c,b
    if b < d:
        b,d = d,b
    if c < d:
        c,d = d,c
    
    print (a, ">", b, ">", c, ">", d)

inputValues()