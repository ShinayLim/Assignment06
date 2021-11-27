def inputValues():
    value1= float(input("Enter first value: "))
    value2 = float(input("Enter second value: "))
    value3 = float(input("Enter third value: "))
    value4 = float(input("Enter fourth value: "))
 
    if value1 < value2:
        value1,value2 = value2,value1
    if value1 < value3:
        value1,value3 = value3,value1
    if value1 < value4:
        value1,value4= value4,value1
    if value2 < value3:
        value2,value3 = value3,value2
    if value2 < value4:
        value2,value4 = value4,value2
    if value3 < value4:
        value3,value4 = value4,value3
    print("\n")
    print("Arrangement of values in \033[1m descending order \033[0m is:" )
    print(value1, ">", value2, ">", value3, ">", value4)
    print("\n")

inputValues()