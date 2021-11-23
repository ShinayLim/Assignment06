def inputValues():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))

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